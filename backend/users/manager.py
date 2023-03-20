from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(
            self,email,
            username,
            nombres=None,
            apellidos=None,
            rol=None,
            regional=None,
            jurisdiccion=None,
            password=None,
            usuario_activo=True
    ):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico!')
        
        usuario = self.model(
            username = username, 
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
            rol = rol,
            regional=regional,
            jurisdiccion=jurisdiccion,
            usuario_activo = usuario_activo
        )
        
        if jurisdiccion is None:
            usuario.jurisdiccion = regional
        
        usuario.set_password(password)
        
        usuario.save()
        
        return usuario
    
    def create_superuser(self, username, email, nombres=None, apellidos=None, rol='administrador', password=None):
        
        usuario = self.create_user(
            email,
            username = username, 
            nombres = nombres, 
            apellidos = apellidos,
            rol = rol,
            password = password,
        )
        
        usuario.is_superuser = True
        
        usuario.save()
        
        return usuario