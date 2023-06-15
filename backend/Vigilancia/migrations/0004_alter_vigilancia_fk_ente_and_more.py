# Generated by Django 4.1.7 on 2023-06-15 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0006_cargo_activo_jerarquia_activo'),
        ('Vigilancia', '0003_alter_vigilancia_fk_ente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vigilancia',
            name='fk_ente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vigilancia.ente'),
        ),
        migrations.AlterField(
            model_name='vigilancia',
            name='fk_funcionario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Personal.funcionario'),
        ),
    ]
