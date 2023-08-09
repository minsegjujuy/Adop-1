from Personal.models import Personal, Jerarquia, Categoria, SubCategoria, Funcionario
from Persona.models import Persona
from Dependencia.models import Dependencia, UnidadRegional
from Persona.api.seeds.persona_seeder import create_persona
import json


def seed_data(file_path="Personal/api/seeds/personal_seeder.json"):
    print("Seeding Personal data...")
    with open(file_path, encoding="utf-8") as json_file:
        data = json_file.read()

    for obj in json.loads(data):
        model = obj["model"]
        if model == "app.Jerarquia":
            create_jerarquia(obj)
        elif model == "app.Personal":
            create_personal(obj)
        elif model == "app.Categoria":
            create_categoria(obj)
        elif model == "app.SubCategoria":
            create_sub_categoria(obj)
        elif model == "app.Persona":
            create_persona(obj)
        elif model == "app.Funcionario":
            create_funcionario(obj)


def create_jerarquia(obj):
    try:
        Jerarquia.objects.get_or_create(
            id=obj["pk"],
            nombre=obj["fields"]["nombre"],
            nombre_largo=obj["fields"]["nombre_largo"],
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")


def create_personal(obj):
    try:
        Personal.objects.get_or_create(
            legajo=obj["fields"]["legajo"],
            fk_persona=Persona.objects.get(cuil=obj["fields"]["cuil"]),
            fk_jerarquia=Jerarquia.objects.get(id=obj["fields"]["fk_jerarquia"]),
            fk_destino=None,
            fk_jurisdiccion=None,
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")


def create_categoria(obj):
    try:
        Categoria.objects.get_or_create(
            id=obj["pk"],
            nombre=obj["fields"]["nombre"],
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")


def create_sub_categoria(obj):
    try:
        SubCategoria.objects.get_or_create(
            id=obj["pk"],
            nombre=obj["fields"]["nombre"],
            fk_categoria=Categoria.objects.get(id=obj["fields"]["fk_categoria"]),
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")


def create_funcionario(obj):
    try:
        Funcionario.objects.get_or_create(
            id=obj["pk"],
            fk_persona=Persona.objects.get(cuil=obj["fields"]["fk_persona"]),
            fk_categoria=SubCategoria.objects.get(id=obj["fields"]["fk_categoria"]),
            fecha_inicio=obj["fields"]["fecha_inicio"],
            fecha_fin=obj["fields"]["fecha_fin"],
        )
    except KeyError as e:
        print(f"El campo {e} no existe en el modelo.")
