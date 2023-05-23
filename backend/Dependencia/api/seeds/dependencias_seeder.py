from typing import Dict
from Dependencia.models import Dependencia, UnidadRegional, Inspectora
import json

def seed_data(file_path='Dependencia/api/seeds/dependencias_seeder.json'):
    
    print("Seeding UURR data...")
    with open(file_path, encoding='utf-8') as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        model = obj['model']
        if model == 'app.UnidadRegional':
            create_unidad_regional(obj)
        elif model == 'app.Dependencia':
            create_dependencia(obj)

def create_unidad_regional(obj: Dict) -> None:
    try:
        UnidadRegional.objects.create(
            id=obj.get('pk'),
            unidad_regional=obj.get('fields', {}).get('unidad_regional')
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")
    
def create_dependencia(obj):
    try:
        Dependencia.objects.create(
            id = obj['pk'],
            fk_inspectora = obj['fields']['fk_inspectora'],
            fk_unidad_regional = UnidadRegional.objects.get(id=obj['fields']['fk_unidad_regional']),
            jurisdiccion = obj['fields']['jurisdiccion']
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")