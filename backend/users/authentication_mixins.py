from .authentication import ExpiringTokenAuthentication
from rest_framework.authentication import get_authorization_header


class Authentication(object):
    
    def get_user(self,request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
                print(token)
            except:
                return None
            
            token_expire = ExpiringTokenAuthentication()
            try:
                user, token = token_expire.authenticate_credentials(token)
                # print(token)
            except:
                message = token_expire.authenticate_credentials(token)
                print(message)
        return None
    
    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        return super().dispatch(request, *args, **kwargs)