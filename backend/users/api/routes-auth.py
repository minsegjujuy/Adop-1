from django.urls import path
from users.api.views import (
    UserView,
    Login,
    Logout,
    RefreshToken
)

urlpatterns = [
    path('auth/login/', Login.as_view(), name='UserLogin'),
    path('auth/logout/', Logout.as_view(), name='UserLogout'),
    path('auth/refresh-token/', RefreshToken.as_view(), name='RefreshToken' )
]
