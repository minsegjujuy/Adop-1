# Generated by Django 4.2.2 on 2023-06-16 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jurisdiccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inspectora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadRegional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_regional', models.CharField(default='', max_length=23)),
            ],
        ),
        migrations.CreateModel(
            name='DependenciaOperativos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.dependencia')),
            ],
        ),
    ]
