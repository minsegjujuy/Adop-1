# Generated by Django 4.1.7 on 2023-03-22 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Operativos', '0002_alter_operativo_dependenciaop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operativo',
            old_name='dependenciaOP',
            new_name='dependencia',
        ),
    ]
