# Generated by Django 4.2 on 2023-04-04 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dependencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('legajo', models.IntegerField(primary_key=True, serialize=False)),
                ('domicilio', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=8, null=True)),
                ('nombre_apellido', models.CharField(default='', max_length=80)),
                ('fecha_nacimiento', models.DateTimeField(default=models.DateField(verbose_name='01/01/1999'))),
                ('estudios', models.CharField(max_length=100)),
                ('oficio', models.CharField(max_length=100)),
                ('jerarquia', models.CharField(max_length=50)),
                ('prestacion_servicios', models.IntegerField()),
                ('funcion', models.CharField(max_length=100)),
                ('escalafon', models.CharField(max_length=100)),
                ('estado_civil', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('cuil', models.CharField(max_length=11)),
                ('fk_dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.dependencia')),
            ],
        ),
    ]
