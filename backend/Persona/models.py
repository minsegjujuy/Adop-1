from django.db import models


class Persona(models.Model):
    cuil = models.BigIntegerField(primary_key=True)
    dni = models.BigIntegerField()
    nombre_apellido = models.CharField(max_length=100, null=False)
    fecha_nacimiento = models.DateField(null=True)

    # SELECT pn.cuil, pn.dni, CONCAT(pn.nombre,' ',pn.apellido) as nombre_apellido, pn.fecha_nacimiento FROM central_policia.public.personas pn INNER JOIN central_policia.personal.personal pl on pl.cuil = pn.cuil and pn.fallecido='N';
    # SELECT pl.legajo, pl.cuil, pl.id_jerarquia as fk_jerarquia, pl.id_dependencia=null as fk_destino, pl.id_tipo_funcion=null as fk_jurisdiccion FROM central_policia.personal.personal pl INNER JOIN central_policia.public.personas pn on pl.cuil = pn.cuil and pn.fallecido='N';
