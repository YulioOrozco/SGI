# Generated by Django 3.0.3 on 2023-11-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_SistemaGestionInventario', '0012_auto_20231104_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='correo_soy_sena',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]