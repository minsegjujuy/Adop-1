# Generated by Django 4.2 on 2023-04-17 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Operativos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_recurso', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_recursos', models.IntegerField()),
                ('fk_operativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operativos.operativo')),
                ('fk_tipo_recurso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Servicio.tiporecurso')),
                ('fk_tipo_servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Servicio.tiposervicio')),
            ],
        ),
    ]
