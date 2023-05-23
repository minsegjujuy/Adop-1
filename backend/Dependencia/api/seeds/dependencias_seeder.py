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

def create_unidad_regional(obj):
    UnidadRegional.objects.create(
        id = obj['pk'],
        unidad_regional = obj['fields']['unidad_regional']
    )
    
def create_dependencia(obj):
    Dependencia.objects.create(
        id = obj['pk'],
        fk_inspectora = obj['fields']['fk_inspectora'],
        fk_unidad_regional = UnidadRegional.objects.get(id=obj['fields']['fk_unidad_regional']),
        jurisdiccion = obj['fields']['jurisdiccion']
    )