from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Documentacion",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
    path('api/',include('users.api.routes-auth')),
    path('api/',include('users.api.router')),
    # path('api/',include('Dependencia.api.router')),
    # path('api/',include('Ley.api.router')),
    # path('api/',include('Operativos.api.router')),
    # path('api/',include('Persona.api.router')),
    # path('api/',include('Personal.api.router')),
    # path('api/',include('Procedimiento.api.router')),
    # path('api/',include('Secuestro.api.router')),
    path('api/',include('Servicio.api.router')),
    path('api/',include('Vigilancia.api.router')),
]
