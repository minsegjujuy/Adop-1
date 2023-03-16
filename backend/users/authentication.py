from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ExpiringTokenAuthentication(TokenAuthentication):
    
    def expired_in(self,token):
        time_elapsed = timezone.now() - token.created
        
        left_time = settings.TOKEN_EXPIRED_AFTER_MINUTES - time_elapsed
        print(left_time)
        return left_time
    
    def is_token_expired(self,token):
        time = self.expired_in(token)
        return time > settings.TOKEN_EXPIRED_AFTER_MINUTES
    
    def token_expired_handler(self,token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            print("TOKEN EXPIRADO")
        return is_expire
    
    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
        except self.get_model().DoesNotExist():
            raise AuthenticationFailed('Token Invalido.')
        
        if not token.user.is_active:
            raise AuthenticationFailed('Usuario no activo o eliminado.')

        is_expired = self.token_expired_handler(token)
        if is_expired:
            raise AuthenticationFailed('Su token ha expirado.')
        
        return (token.user, token) 
            