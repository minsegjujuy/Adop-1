from ...models import Rol, Usuario
from Dependencia.models import UnidadRegional, Dependencia
import json

def seed_data():
    
    print("Seeding Users data...")
    with open('users/api/seeds/users_seeder.json', encoding='utf-8') as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        model = obj['model']
        fields = obj['fields']

        if model == 'app.Rol':
            Rol.objects.create(
                id = obj['pk'],
                rol = fields['rol']
            )
        elif model == 'app.Usuario':
            if fields['rol'] == 1:
                Usuario.objects.create_superuser(
                    # id = obj['pk'],
                    username = fields['username'],
                    email = fields['email'],
                    rol = Rol.objects.get(id=fields['rol']),
                    password = fields['password']
                )
            else:
                Usuario.objects.create_user(
                    # id = obj['pk'],
                    email = fields['email'],
                    username = fields['username'],
                    nombres = fields['nombres'],
                    apellidos = fields['apellidos'],
                    rol = Rol.objects.get(id=fields['rol']),
                    unidad_regional = UnidadRegional.objects.get(id=fields['unidad_regional']),
                    jurisdiccion = Dependencia.objects.get(id=fields['jurisdiccion']),
                    password=fields['password']
                )