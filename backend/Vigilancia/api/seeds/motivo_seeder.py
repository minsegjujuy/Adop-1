from ...models import Motivo
import json

def seed_data(file_path='Vigilancia/api/seeds/motivo_seeder.json'):
    
    print("Seeding Motivo data...")
    with open(file_path, encoding='utf-8') as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        model = obj['model']
        if model == 'app.Motivo':
            create_motivo(obj)

def create_motivo(obj):
    Motivo.objects.get_or_create(
        id = obj['pk'],
        motivo = obj['fields']['motivo']
    )