from django.urls import path
from users.api.views import (
    UserView,
    Login,
    Logout
)

urlpatterns = [
    path('auth/login/', Login.as_view(), name='UserLogin'),
    path('auth/logout/', Logout.as_view(), name='UserLogout'),
]
