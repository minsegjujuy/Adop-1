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
            # pass
        elif model == 'app.Personal':
            create_personal(obj)

def create_jerarquia(obj):
    try:
        Jerarquia.objects.get_or_create(
            id = obj['pk'],
            nombre = obj['fields']['nombre'],
            nombre_largo = obj['fields']['nombre_largo']
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")

def create_personal(obj):
    try:
        Personal.objects.get_or_create(
            legajo = obj['fields']['legajo'],
            fk_persona = Persona.objects.get(cuil=obj['fields']['cuil']),
            fk_jerarquia = Jerarquia.objects.get(id=obj['fields']['fk_jerarquia']),
            fk_destino = None,
            fk_jurisdiccion = None,
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")