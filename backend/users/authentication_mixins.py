from .authentication import ExpiringTokenAuthentication
from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class Authentication(object):
    user = None
    user_token_expired = False
    
    def get_user(self,request):
        token = get_authorization_header(request).split()
        if token != []:
            try:
                token = token[1].decode()
                # print(token)
            except:
                return None
            
            token_expire = ExpiringTokenAuthentication()
            user,token,message,self.user_token_expired = token_expire.authenticate_credentials(token)
            
            if user is not None and token is not None:
                self.user = user
                return user
            
            return message
        
        return None
    
    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        # print(user)
        if user is not None:
            if type(user)==str:
                response = Response(
                    {
                        'error':user,
                        'expired': self.user_token_expired
                    }, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'aplication/json'
                response.renderer_context = {}
                return response
            # print(self.user_token_expired)
            if not self.user_token_expired:
                return super().dispatch(request, *args, **kwargs)
            
        response =  Response(
            {
                'error': 'No se han enviado las credenciales.',
                'expired': self.user_token_expired
            }, 
            status = status.HTTP_400_BAD_REQUEST
        )
        
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'aplication/json'
        response.renderer_context = {}
        
        return response