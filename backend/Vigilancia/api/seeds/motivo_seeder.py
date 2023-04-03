from ...models import MotivoVigilancia
import json

def seed_data():
    
    print("Seeding Motivo data...")
    with open('Vigilancia/api/seeds/motivo_seeder.json', encoding='utf-8') as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        model = obj['model']
        fields = obj['fields']

        if model == 'app.Motivo':
            MotivoVigilancia.objects.create(
                id = obj['pk'],
                motivo = fields['motivo']
            )