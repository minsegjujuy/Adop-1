# Generated by Django 4.2 on 2023-04-11 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Procedimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSecuestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_secuestro', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Secuestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fk_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procedimiento.procedimiento')),
                ('fk_tipo_secuestro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Secuestro.tiposecuestro')),
            ],
        ),
    ]
