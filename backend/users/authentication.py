from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.contrib.sessions.models import Session
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False
    
    def expired_in(self,token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(minutes=settings.TOKEN_EXPIRED_AFTER_MINUTES) - time_elapsed
        return left_time
    
    def is_token_expired(self,token):
        print(self.expired_in(token))
        # print(self.expired_in(token) < timedelta(minutes=0))
        return self.expired_in(token) < timedelta(minutes=0)
    
    def token_expired_handler(self,token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            self.expired = True
            user = token.user
            # all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
            # if all_sessions.exists():
            #     for session in all_sessions:
            #         session_data = session.get_decoded()
            #         if user.id == (session_data.get('_auth_user_id')):
            #             session.delete()
            token.delete()
            
            token = self.get_model().objects.create(user = user)
            
        return is_expire, token
    
    def authenticate_credentials(self, key):
        message, token, user = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token Invalido.'
            self.expired = True
        # print(token)
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario no activo o eliminado.'

            is_expired = self.token_expired_handler(token)
            if is_expired:
                message = 'Su token ha expirado.'
        
        return (user, token, message, self.expired) 
            