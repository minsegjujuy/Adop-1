from datetime import datetime, date
from Persona.models import Persona
import json

def seed_data(file_path='Persona/api/seeds/persona_seeder.json'):
    
    print("Seeding Persona data...")
    with open(file_path, encoding='utf-8') as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        model = obj['model']
        if model == 'app.Persona':
            create_persona(obj)
    
def create_persona(obj):
    fecha = obj['fields']['fecha_nacimiento']
    if fecha != None:
        Persona.objects.get_or_create(
            cuil = obj['fields']['cuil'],
            dni = obj['fields']['dni'],
            nombre_apellido = obj['fields']['nombre_apellido'],
            fecha_nacimiento = datetime.strptime(fecha, "%Y-%m-%d").date()
        )
    else:
        Persona.objects.get_or_create(
            cuil = obj['fields']['cuil'],
            dni = obj['fields']['dni'],
            nombre_apellido = obj['fields']['nombre_apellido'],
            fecha_nacimiento = fecha
        )