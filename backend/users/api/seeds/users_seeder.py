from ...models import Rol, Usuario
from Dependencia.models import UnidadRegional, Dependencia
import json

def seed_data(file='users/api/seeds/users_seeder.json'):
    
    print("Seeding Users data...")
    with open(file, encoding='utf-8') as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        if obj['model'] == 'app.Rol':
            create_rol(obj)
        elif obj['model'] == 'app.Usuario':
            if obj['fields']['rol'] == 1:
                create_super_user(obj)
            else:
                create_user(obj)

def create_rol(obj):
    try:
        Rol.objects.get_or_create(
            id=obj['pk'],
            rol=obj['fields']['rol']
        )
    except:
        return


def create_super_user(obj):
    try:
        Usuario.objects.create_superuser(
            # id = obj['pk'],
            username = obj['fields']['username'],
            email = obj['fields']['email'],
            rol = Rol.objects.get(id=obj['fields']['rol']),
            password = obj['fields']['password']
        )
    except:
        return

def create_user(obj):
    try:
        Usuario.objects.create_user(
            email=obj['fields'].get('email'),
            username=obj['fields'].get('username'),
            nombres=obj['fields'].get('nombres'),
            apellidos=obj['fields'].get('apellidos'),
            rol=Rol.objects.get(id=obj['fields'].get('rol')),
            unidad_regional=UnidadRegional.objects.get(id=obj['fields'].get('unidad_regional')),
            jurisdiccion=Dependencia.objects.get(id=obj['fields'].get('jurisdiccion')),
            password=obj['fields'].get('password')
        )
    except:
        return