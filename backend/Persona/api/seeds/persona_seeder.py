from datetime import datetime, date
from Persona.models import Persona
import json

def seed_data(file_path='Persona/api/seeds/persona_seeder.json') -> None:
    print("Seeding Persona data...")
    with open(file_path, encoding='utf-8') as json_file:
        data = json_file.read()
        
    personas = [obj for obj in json.loads(data) if obj['model'] == 'app.Persona']
    for persona in personas:
        create_persona(persona)
    
def create_persona(obj):
    try:
        fecha = obj['fields']['fecha_nacimiento']
        fecha_nacimiento = datetime.strptime(fecha, "%Y-%m-%d").date() if fecha else None
        Persona.objects.get_or_create(
            cuil=obj['fields']['cuil'],
            dni=obj['fields']['dni'],
            nombre_apellido=obj['fields']['nombre_apellido'],
            fecha_nacimiento=fecha_nacimiento
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")