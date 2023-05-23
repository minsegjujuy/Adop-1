# Generated by Django 4.2 on 2023-05-23 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Operativos', '0001_initial'),
        ('Dependencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependenciaoperativos',
            name='fk_operativo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operativos.operativo'),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='fk_inspectora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dependencia.inspectora'),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='fk_unidad_regional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.unidadregional'),
        ),
    ]
