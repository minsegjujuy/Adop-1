from django.db import models


class Inspectora(models.Model):
    pass


class UnidadRegional(models.Model):
    unidad_regional = models.CharField(max_length=23, default="")


class Dependencia(models.Model):
    fk_unidad_regional = models.ForeignKey("UnidadRegional", on_delete=models.CASCADE)
    fk_inspectora = models.ForeignKey("Inspectora", on_delete=models.CASCADE, null=True)
    jurisdiccion = models.CharField(null=False, max_length=100)
    # activar luego de la primera migracion
    # operativos = models.ManyToManyField('DependenciaOperativos', db_table='dependencia_operativos', related_name='operativos') #comentar para la primera migracion


class DependenciaOperativos(models.Model):
    fk_dependencia = models.ForeignKey("Dependencia.Dependencia", on_delete=models.CASCADE)
    fk_operativo = models.ForeignKey("Operativos.Operativo", on_delete=models.CASCADE)
