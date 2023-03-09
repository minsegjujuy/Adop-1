# Generated by Django 4.1.7 on 2023-03-09 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dependencia', '0001_initial'),
        ('Operativos', '0001_initial'),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.inspectora'),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='fk_unidad_regional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.unidadregional'),
        ),
    ]
