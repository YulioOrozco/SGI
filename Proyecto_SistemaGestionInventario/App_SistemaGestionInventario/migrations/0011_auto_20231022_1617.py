# Generated by Django 3.0.3 on 2023-10-22 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_SistemaGestionInventario', '0010_usuario_estado_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='rol',
            field=models.CharField(choices=[('I.P', 'Instructor de planta'), ('I.C', 'Instructor contratista'), ('M', 'Aprendiz'), ('ADM', 'Administrativo')], default='I.P', max_length=5),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tipo_documento',
            field=models.CharField(choices=[('C.C', 'Cedula de ciudadania'), ('P.E', 'Permiso especial'), ('Pasaporte', 'Pasaporte'), ('C.E', 'Cedula de extranjeria'), ('T.I', 'Tarjeta de identidad'), ('R.C', 'Registro civil')], default='C.C', max_length=11),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='estado_material',
            field=models.CharField(choices=[('Dis', 'Disponible'), ('Pres', 'Prestamo'), ('Gar', 'Garantia'), ('Sop', 'Soporte'), ('DB', 'De baja'), ('Entr', 'Entregado')], default='Dis', max_length=6),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='tipo_material',
            field=models.CharField(choices=[('Consu', 'Consumible'), ('Devo', 'Devolutivo')], default='Devo', max_length=7),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='ubicacion_material',
            field=models.CharField(choices=[('Bod', 'Bodega'), ('Z1', 'Zona 1'), ('Z2', 'Zona 2'), ('Z3', 'Zona 3'), ('Z4', 'Zona 4'), ('Z5', 'Zona 5'), ('Z6', 'Zona 6'), ('Admin', 'Administrativos'), ('N.A', 'No aplica'), ('Comp', 'Competencia')], default='Z1', max_length=7),
        ),
        migrations.AlterField(
            model_name='prestamosconsumibles',
            name='ubicacion_prestamo_prestamo_consumible',
            field=models.CharField(choices=[('Bod', 'Bodega'), ('Z1', 'Zona 1'), ('Z2', 'Zona 2'), ('Z3', 'Zona 3'), ('Z4', 'Zona 4'), ('Z5', 'Zona 5'), ('Z6', 'Zona 6'), ('Admin', 'Administrativos'), ('N.A', 'No aplica'), ('Comp', 'Competencia')], default='N.A', max_length=5),
        ),
        migrations.AlterField(
            model_name='prestamosdevolutivos',
            name='ubicacion_prestamo_material_devolutivo',
            field=models.CharField(choices=[('Bod', 'Bodega'), ('Z1', 'Zona 1'), ('Z2', 'Zona 2'), ('Z3', 'Zona 3'), ('Z4', 'Zona 4'), ('Z5', 'Zona 5'), ('Z6', 'Zona 6'), ('Admin', 'Administrativos'), ('N.A', 'No aplica'), ('Comp', 'Competencia')], default='Bod', max_length=5),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='celular_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo_sena',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado_cuenta',
            field=models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_fin_contrato',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_area_instrtuctor',
            field=models.CharField(choices=[('Soft', 'Software')], default='Soft', max_length=6),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_rol',
            field=models.CharField(choices=[('I.P', 'Instructor de planta'), ('I.C', 'Instructor contratista'), ('M', 'Monitor')], default='I.C', max_length=5),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_tipo_documento',
            field=models.CharField(choices=[('C.C', 'Cedula de ciudadania'), ('P.E', 'Permiso especial'), ('Pasaporte', 'Pasaporte'), ('C.E', 'Cedula de extranjeria'), ('T.I', 'Tarjeta de identidad'), ('R.C', 'Registro civil')], default='C.C', max_length=11),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numero_documento',
            field=models.CharField(max_length=80),
        ),
    ]
