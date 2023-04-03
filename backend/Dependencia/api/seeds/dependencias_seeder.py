from Dependencia.models import Dependencia, UnidadRegional, Inspectora
from django.core.management.base import BaseCommand
import json

def seed_data():
    
    print("Loading data...")
    with open('Dependencia/api/seeds/dependencias_seeder.json') as json_file:
        data = json_file.read()
        
    for obj in json.loads(data):
        model = obj['model']
        fields = obj['fields']

        if model == 'app.UnidadRegional':
            UnidadRegional.objects.create(
                id = obj['pk'],
                unidad_regional = fields['unidad_regional']
            )

        elif model == 'app.Dependencia':
            Dependencia.objects.create(
                id = obj['pk'],
                fk_inspectora = fields['fk_inspectora'],
                fk_unidad_regional = UnidadRegional.objects.get(id=fields['fk_unidad_regional']),
                jurisdiccion = fields['jurisdiccion']
            )