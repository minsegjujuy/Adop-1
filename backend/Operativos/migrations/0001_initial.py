# Generated by Django 4.1.7 on 2023-07-18 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dependencia', '0001_initial'),
        ('Personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jefe_cargo', models.IntegerField()),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('fecha', models.DateField()),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=13)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=13)),
                ('cant_personas_afectadas', models.IntegerField()),
                ('cant_recursos', models.IntegerField()),
                ('procedimiento', models.BooleanField()),
                ('turno', models.CharField(max_length=10)),
                ('jurisdiccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dependencia.dependencia')),
            ],
        ),
        migrations.CreateModel(
            name='OperativoPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_operativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operativos.operativo')),
                ('fk_personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personal.personal')),
            ],
        ),
    ]
