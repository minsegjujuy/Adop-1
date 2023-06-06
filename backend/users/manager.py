from django.contrib.auth.models import BaseUserManager
import users

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
        if not self.get(username=username):
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
            usuario.set_password(password)
            usuario.save()
            return usuario
        else:
            raise ValueError('El nombre de usuario ya existe')
    
    def create_superuser(
        self, 
        username, 
        email,
        rol=1,
        password=None):
        if rol == 1:
            user_rol =  users.models.Rol.objects.get(id=rol)
        else:
            user_rol = rol
        usuario = self.create_user(
            email = email,
            username = username,
            rol = user_rol,
            password = password,
        )
        
        usuario.is_superuser = True
        
        usuario.save()
        
        return usuario