from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(
            self,
            email,
            username,
            nombres=None,
            apellidos=None,
            rol=None,
            unidad_regional=None,
            jurisdiccion=None,
            password=None,
            is_superuser=False
    ):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico!')
        
        usuario = self.model(
            username = username, 
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
            rol = rol,
            unidad_regional=unidad_regional,
            jurisdiccion=jurisdiccion,
            is_superuser = is_superuser
        )
        
        # if jurisdiccion is None:
        #     usuario.jurisdiccion = regional
        
        # print(password)
        password = make_password(password)
        # print(password)
        usuario.set_password(password)
        
        usuario.save()
        
        return usuario
    
    def create_superuser(
        self, 
        username, 
        email,
        rol=0,
        password=None):
        
        usuario = self.create_user(
            email = email,
            username = username,
            rol = rol,
            password = password,
        )
        
        usuario.is_superuser = True
        
        usuario.save()
        
        return usuario