# Generated by Django 3.0.3 on 2023-10-16 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_SistemaGestionInventario', '0002_auto_20231015_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='rol',
            field=models.CharField(choices=[('1', 'Instructor de planta'), ('2', 'Instructor contratista'), ('3', 'Aprendiz'), ('4', 'Administrativo')], default='1', max_length=1),
        ),
    ]