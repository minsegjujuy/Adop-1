from Personal.models import Personal, Jerarquia
from Persona.models import Persona
from Dependencia.models import Dependencia, UnidadRegional
import json

def seed_data(file_path='Personal/api/seeds/personal_seeder.json'):
    
    print("Seeding Personal data...")
    with open(file_path, encoding="utf-8") as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        model = obj['model']
        if model == 'app.Jerarquia':
            create_jerarquia(obj)
            
        elif model == 'app.Personal':
            create_personal(obj)

def create_jerarquia(obj):
    Jerarquia.objects.create(
        id = obj['pk'],
        # fk_tipo_jerarquia = TipoJerarquia.objects.get(id = obj['fields']['fk_tipo_jerarquia']),
        nombre = obj['fields']['nombre'],
        nombre_largo = obj['fields']['nombre_largo']
    )

def create_personal(obj):
    Personal.objects.create(
        legajo = obj['fields']['legajo'],
        cuil = Persona.objects.get(cuil=obj['fields']['cuil']).cuil,
        # fk_tipo_funcion = TipoFuncion.objects.get(id=obj['fields']['fk_tipo_funcion']),
        fk_jerarquia = Jerarquia.objects.get(id=obj['fields']['fk_jerarquia']),
        fk_destino = None,
        fk_jurisdiccion = None,
        # fk_destino = Dependencia.objects.get(id=obj['fields']['fk_destino']),
        # fk_jurisdiccion = UnidadRegional.objects.get(id=obj['fields']['fk_jurisdiccion']),
    )