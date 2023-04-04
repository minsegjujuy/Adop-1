from Servicio.models import TipoServicio, TipoRecurso
import json

def seed_data():
    
    print("Seeding Servicio data...")
    with open('Servicio/api/seeds/servicio_seeder.json', encoding='utf-8') as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        model = obj['model']
        fields = obj['fields']

        if model == 'app.TipoServicio':
            TipoServicio.objects.create(
                id = obj['pk'],
                tipo_servicio = fields['tipo_servicio']
            )
        elif model == 'app.TipoRecurso':
            TipoRecurso.objects.create(
                id = obj['pk'],
                tipo_recurso = fields['tipo_recurso']
            )