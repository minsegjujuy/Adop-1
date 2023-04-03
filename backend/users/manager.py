from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(
            self,
            email,
            username,
            nombres,
            apellidos,
            rol,
            regional,
            jurisdiccion,
            password,
            administrador=False
    ):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico!')
        
        print(rol)
        
        if rol == 'administrador' or rol == 'general' or rol == 'operador':
                    
            usuario = self.model(
                username = username, 
                email = self.normalize_email(email),
                nombres = nombres,
                apellidos = apellidos,
                rol = rol,
                regional=regional,
                jurisdiccion=jurisdiccion,
                is_superuser = administrador
            )
            
            if jurisdiccion is None:
                usuario.jurisdiccion = regional
            
            print(password)
            password = make_password(password)
            print(password)
            usuario.set_password(password)
            
            usuario.save()
            
            return usuario
        else:
            raise ValueError('El rol ingresado no existe')
    
    def create_superuser(
        self, 
        username, 
        email, 
        nombres=None, 
        apellidos=None, 
        rol='administrador', 
        password=None):
        
        usuario = self.create_user(
            email = email,
            username = username, 
            nombres = nombres, 
            apellidos = apellidos,
            rol = rol,
            password = password,
        )
        
        usuario.is_superuser = True
        
        usuario.save()
        
        return usuario