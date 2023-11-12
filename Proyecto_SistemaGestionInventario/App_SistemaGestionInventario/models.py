from django.db import models
from .choices import *

# Create your models here.

class Usuario(models.Model):
    id = models.BigAutoField(primary_key = True)
    nombre_1 = models.CharField(max_length=80)
    nombre_2 = models.CharField(max_length=80, blank=True, null=True)
    apellido_1 = models.CharField(max_length=80)
    apellido_2 = models.CharField(max_length=80, blank=True, null=True)
    id_tipo_documento = models.CharField(max_length=11, choices=tipo_documento, default='C.C')
    numero_documento = models.CharField(max_length=80, blank=False, null=False, unique=True)
    correo_sena = models.EmailField(blank=True, null=True, unique=True)
    correo_soy_sena = models.EmailField(blank=False, null=False, unique=True)
    celular_1 = models.CharField(max_length=80, unique=True)
    celular_2 = models.CharField(max_length=80, blank=True, null=True)
    id_rol = models.CharField(max_length=5, choices=rol, default='I.C')
    fecha_inicio_contrato = models.DateField()
    fecha_fin_contrato = models.DateField(blank=True, null=True)
    id_area_instrtuctor = models.CharField(max_length=6, choices=area, default='Soft')
    firma_electronica = models.ImageField()
    estado_cuenta = models.CharField(max_length=1, choices=estado_cuenta_usuario, default='A')
    
    class Meta():
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def nombre_completo(self):
        return "{} {}".format(self.nombre_1, self.apellido_1)

    def __str__(self):
        return self.nombre_completo()



class Materiales(models.Model):
    id = models.BigAutoField(primary_key = True)
    tipo_material = models.CharField(max_length=7, choices=tipo_material, default='Devo')
    nombre_material = models.CharField(max_length=40)
    modelo_material = models.CharField(max_length=40)
    ubicacion_material = models.CharField(max_length=7, choices=ubicacion_material, default='Z1')
    valor_material = models.IntegerField()
    estado_material = models.CharField(max_length=6, choices=estado_material, default="Dis")
    especificacion_tecnica_material = models.CharField(max_length=150)
    instructor_ecargado_material = models.ForeignKey(Usuario, related_name='encargado_material', null=False, blank=False, on_delete=models.CASCADE)
    codigo_barras_original_material = models.CharField(max_length=50, blank=False, null=False, unique=True)
    codigo_barras_sena_material = models.CharField(max_length=50, blank=False, null=False, unique=True)
    encargado_registrar_material = models.ForeignKey(Usuario, related_name='encargado_ingresar_consumible_sistema', null=False, blank=False, on_delete=models.CASCADE)
    fecha_ingreso_material = models.DateField(auto_now_add=True)
    actualizacion_material = models.DateField(auto_now_add=True)
    
    class Meta():
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

    def material_instructor(self):
        return '{} - {} - {}'.format(self.nombre_material, self.codigo_barras_sena_material, self.instructor_ecargado_material)
    
    def __str__(self):
        return self.material_instructor()
    

class Clientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    rol = models.CharField(max_length=5, choices=recibe_material, default='I.P')
    tipo_documento = models.CharField(max_length=11, choices=tipo_documento, default='C.C')
    numero_documento = models.IntegerField(blank=False, null=False, unique=True)
    primer_nombre = models.CharField(max_length=25, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=25, blank=True, null=True)
    primer_apellido = models.CharField(max_length=25, blank=False, null=False)
    segundo_apellido = models.CharField(max_length=25, blank=True, null=True, default='')
    correo_soy_sena = models.EmailField(blank=False, null=False, unique=True)
    primer_telefono = models.IntegerField(blank=False, null=False, unique=True)
    segundo_telefono = models.IntegerField(blank=True, null=True, default='')
    numero_ficha = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingres_sistema = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def nombre_cliente(self):
        return '{}  {} - {} - {}'.format(self.primer_nombre, self.primer_apellido, self.numero_documento, self.rol,)
    
    def __str__(self):
        return self.nombre_cliente()



class PrestamosConsumibles(models.Model):
    id = models.BigAutoField(primary_key=True)
    encargado_registra_prestamo_consumible = models.ForeignKey(Usuario, blank=False, null=False, on_delete=models.CASCADE)
    recibe_prestamo_prestamo_consumible = models.ForeignKey(Clientes, null=False, blank=False, on_delete=models.CASCADE)
    ubicacion_prestamo_prestamo_consumible = models.CharField(max_length=5, choices=ubicacion_material, default='N.A')
    material_otorgado_prestamo_consumible = models.ForeignKey(Materiales, null=False, blank=False, on_delete=models.CASCADE)
    fecha_entrega_prestamo_consumible = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = 'Prestamo consumible'
        verbose_name_plural = 'Prestamos Consumibles'
    
    def formato_prestamo(self):
        return '{} - {}'.format(self.id, self.material_otorgado_prestamo_consumible)

    def __str__(self):
        return self.formato_prestamo()



class PrestamosDevolutivos(models.Model):
    id = models.BigAutoField(primary_key=True)
    encargado_registra_material_devolutivo = models.ForeignKey(Usuario, blank=False, null=False, on_delete=models.CASCADE)
    recibe_prestamo_material_devolutivo = models.ForeignKey(Clientes, blank=False, null=False, on_delete=models.CASCADE)
    ubicacion_prestamo_material_devolutivo = models.CharField(max_length=5, choices=ubicacion_material, default='Bod')
    material_otorgado_devolutivo = models.ForeignKey(Materiales, null=False, blank=False, on_delete=models.CASCADE)
    fecha_entrega_material_devolutivo = models.DateField(auto_now_add=True)
    fecha_devolucion_material_devolutivo = models.DateField(blank=False, null=False)

    class Meta():
        verbose_name = 'Prestamo Devolutivo'
        verbose_name_plural = 'Prestamos Devolutivos'

    def formato_prestamo(self):
        return '{} - {}'.format(self.id, self.material_otorgado_devolutivo)
    
    def __str__(self):
        return self.formato_prestamo()
    


'''

MODELO DEL PIN (CAMBIAR CONTRASENA)

class Pin(models.Model):
    usuario = models. models.ForeignKey(Usuario, blank=False, null=False, on_delete=models.CASCADE)
    pin = models.CharField(max_length=6, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    expiracion = models.DateTimeField()

    def __str__(self):
        return self.pin
        

class MaterialesConsumibles(models.Model):
    id = models.BigAutoField(primary_key = True)
    nombre_material_consumible = models.CharField(max_length=40)
    modelo_material_consumible = models.CharField(max_length=40)
    ubicacion_material_consumible = models.CharField(max_length=40)
    valor_material_consumible = models.IntegerField()
    estado_material_consumible = models.CharField(max_length=1, choices=estado_material, default="1")
    especificacion_tecnica_material_consumible = models.CharField(max_length=150)
    instructor_encargado_material_consumible = models.ForeignKey(Usuario, null=False, blank=True, on_delete=models.CASCADE)
    codigo_barras_original_material_consumible = models.IntegerField()
    codigo_barras_sena_material_consumible = models.IntegerField()
    encargado_registrar_material_consumible = models.ForeignKey(Usuario, related_name='encargado_ingresar_material_consumible_sistema', null=False, blank=True, on_delete=models.CASCADE)
    fecha_ingreso_material_consumible = models.DateField(auto_now_add=True)
    actualizacion_material_consumible = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = 'material consumible'
        verbose_name_plural = 'materiales consumibles'

    def __str__(self):
        return self.nombre_material_consumible



class MaterialesDevolutivos(models.Model):
    id = models.BigAutoField(primary_key = True)
    nombre_material_devolutivo = models.CharField(max_length=40)
    modelo_material_devolutivo = models.CharField(max_length=40)
    ubicacion_material_devolutivo = models.CharField(max_length=1, choices=ubicacion_material, default='1')
    valor_material_devolutivo = models.IntegerField()
    estado_material_devolutivo = models.CharField(max_length=1, choices=estado_material, default='1')
    especificacion_tecnica_material_devolutivo = models.CharField(max_length=150)
    instructor_encargado_material_devolutivo = models.ForeignKey(Usuario, null=False, blank=True, on_delete=models.CASCADE)
    codigo_barras_original_material_devolutivo = models.IntegerField()
    codigo_barras_sena_material_devolutivo = models.IntegerField()
    encargado_registrar_material_devolutivo = models.ForeignKey(Usuario, related_name='encargado_ingresar_material_devolutivo_sistema', null=False, blank=True, on_delete=models.CASCADE)
    fecha_ingreso_material_devolutivo = models.DateField(auto_now_add=True)
    actualizacion_material_devolutivo = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = 'material devolutivo'
        verbose_name_plural = 'materiales devolutivos'

    def __str__(self):
        return self.nombre_material_devolutivo



class Garantia(models.Model):
    #PK ID_Codigo_garantia
    nombre_encargado_reparacion = models.CharField(max_length=80)
    id_encargado_reparacion = models.CharField(max_length=80)
    nombre_material = models.CharField(max_length=80)
    estado_material = models.CharField(max_length=80)
    ubicacion_prestado = models.CharField(max_length=80)
    tiempo_reparacion = models.CharField(max_length=80)
    cantidad_materiales = models.IntegerField()
    tipo_elemento = models.CharField(max_length=80, default="Consumible")
    #FK ID_Codigo_material_devolutivo
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    class Meta():
        verbose_name = 'garantia'
        verbose_name_plural = ' Garantias'
    
    def __str__(self):
        return self.tipo_elemento

class Pedidos(models.Model):
    #PK ID_Codigo_pedidos
    nombre_material = models.CharField(max_length=80)
    stock_material = models.IntegerField()
    tipo_material= models.CharField(max_length=80)
    #FK ID_Codigo_elemento_devolutivo
    #FK ID_Codigo_elemento_consumible
    #FK ID_Codigo_intructor

class Bajas(models.Model):
    #PK ID_Codigo_baja
    nombre_material = models.CharField(max_length=80)
    fecha_baja = models.DateField()
    motivo_baja  = models.CharField(max_length=80)
    ultima_persona_uso = models.CharField(max_length=80)
    #FK ID_Codigo_elemento_devolutivo

class Prestamos_devolutivos(models.Model):
    #PK Id_Codigo_prestamso

    persona_recibe_material = models.CharField(max_length=1, choices=recibe_material, default='1')
    nombre_1 = models.CharField(max_length=80, default='')
    nombre_2 = models.CharField(max_length=80, blank=True)
    apellido_1 = models.CharField(max_length=80, default='')
    apellido_2 = models.CharField(max_length=80, default='', blank=True)
    correo_soy_sena = models.EmailField(default='')
    correo_sena = models.EmailField(blank=True)
    celular_1 = models.CharField(max_length=80, default='')
    celular_2 = models.CharField(max_length=80, blank=True)
    numero_ficha = models.CharField(max_length=20, blank = True)
    nombre_material_prestado = models.ForeignKey(MaterialesDevolutivos, null=False, on_delete=models.CASCADE)
    estado_material_prestado  = models.CharField(max_length=1, choices=estado_material, default='2')
    ubicacion_prestado = models.CharField(max_length=1, choices=ubicacion_material)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField()
    instructor_encargado_prestamo_devolutivo = models.ForeignKey(Usuario, related_name='instructor_encargado_prestamo_devolutivo', null=False, blank=True, on_delete=models.CASCADE, default='')
    instructor_recibe_prestamo_devolutivo = models.ForeignKey(Usuario,  related_name='instructor_recibe_prestamo_devolutio', blank=True, on_delete=models.CASCADE)
    
    #FK ID_Codigo_elemento_devolutivo
    #FK ID_Codigo_monitor
    #Fk ID_Codigo_instructor 

    class Meta():
        verbose_name = 'Prestamos_devolutivos'
        verbose_name_plural = 'Prestamos devolutivos'

class Prestamos_consumible(models.Model):
    #PK Id_Codigo_prestamso
    instructor_encargado = models.ForeignKey(Usuario, null=False, blank=True, on_delete=models.CASCADE)
    persona_recibe_material = models.CharField(max_length=1, choices=recibe_material, default='1')
    nombre_1 = models.CharField(max_length=80, default='')
    nombre_2 = models.CharField(max_length=80, blank=True)
    apellido_1 = models.CharField(max_length=80, default='')
    apellido_2 = models.CharField(max_length=80, default='', blank=True)
    correo_soy_sena = models.EmailField(default='')
    correo_sena = models.EmailField(blank=True)
    celular_1 = models.CharField(max_length=80, default='')
    celular_2 = models.CharField(max_length=80, blank=True)
    numero_ficha = models.CharField(max_length=20, blank = True)
    nombre_material_prestado = models.ForeignKey(MaterialesConsumibles, blank=True, null=False, on_delete=models.CASCADE)
    estado_material_prestado  = models.CharField(max_length=1, choices=estado_material, default='6')
    ubicacion_prestado = models.CharField(max_length=1, choices=ubicacion_material)
    fecha_prestamo_consumible = models.DateField(auto_now_add=True)
    
    #FK ID_Codigo_elemento_devolutivo
    #FK ID_Codigo_monitor
    #Fk ID_Codigo_instructor 
    class Meta():
        verbose_name = 'Prestamos_cosumible'
        verbose_name_plural = 'Prestamos consumibles'
'''