# Generated by Django 4.1.7 on 2023-03-22 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dependencia', '0003_rename_jurisdicciones_op_dependencia_jurisdiccion_and_more'),
        ('Operativos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operativo',
            name='dependenciaOP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.dependencia'),
        ),
    ]
