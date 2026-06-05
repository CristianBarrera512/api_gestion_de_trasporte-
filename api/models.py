from django.db import models



class BaseModel(models.Model):
    usuario_creacion = models.CharField(max_length=150, null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=150, null=True, blank=True)
    class Meta:
        abstract = True



class Vehiculo (BaseModel):
    id_vehiculo = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=15)
    modelo = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.placa
    
    class Meta:
        db_table = 'vehiculo'


class Aseguradora(BaseModel):
    id_aseguradora = models.AutoField(primary_key=True)
    nombre_aseguradora= models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_aseguradora
    
    class Meta:
        db_table = 'aseguradora'


class Empresa(BaseModel):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'empresa'


class Documentacion(BaseModel):
    id_documentos = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50)

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero_documento
    class Meta:
        db_table = 'documentacion'


class Licencias(BaseModel):
    id_licencias = models.AutoField(primary_key=True)
    numero_licencia = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero_licencia
    class Meta:
        db_table = 'licencias'

class Conductores(BaseModel):
    id_conductores = models.AutoField(primary_key=True)
    id_aseguradora = models.ForeignKey(
        Aseguradora,
        on_delete=models.CASCADE,
        db_column='id_aseguradora'
    )
    id_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        db_column='id_empresa'
    )
    id_documento = models.ForeignKey(
        Documentacion,
        on_delete=models.CASCADE,
        db_column='id_documentos'
    )
    id_licencia = models.ForeignKey(
        Licencias,
        on_delete=models.CASCADE,
        db_column='id_lincecias'
    )
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=5)
    lugar_recidencia = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'conductores'


class Rutas (BaseModel):
    id_rutas= models.AutoField(primary_key=True)
    nombre_ruta = models.CharField(max_length=200)
    lugar_salida = models.CharField(max_length=150)
    lugar_llega = models.CharField(max_length=150)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_ruta
    class Meta:
        db_table = 'rutas'

class Viajes (BaseModel):
    id_viajes = models.AutoField(primary_key=True)
    id_ruta = models.ForeignKey(
        Rutas,
        on_delete=models.CASCADE,
        db_column='id_rutas'
    )
    
    fecha_viaje = models.DateField()
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Viaje {self.id_viajes}"
    class Meta:
        db_table = 'viajes'

class Pasajeros (BaseModel):
    id_pasajeros = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_documento = models.ForeignKey(
        Documentacion,
        on_delete=models.CASCADE,
        db_column='id_documentos'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'pasajeros'

class Boletos (BaseModel):
    id_boletos = models.AutoField(primary_key=True)
    id_pasajero = models.ForeignKey(
        Pasajeros,
        on_delete=models.CASCADE,
        db_column='id_pasajero'
    )
    id_viaje = models.ForeignKey(
        Viajes,
        on_delete=models.CASCADE,
        db_column='id_viaje'
    )
    numero_asiento = models.IntegerField()
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    fecha_compra = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('Reservado', 'Reservado'),
            ('Pagado', 'Pagado'),
            ('Cancelado', 'Cancelado')
        ],
        default='Reservado'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.numero_asiento
    class Meta:
        db_table = 'boletos'

class Estaciones (BaseModel):
    id_estaciones = models.AutoField(primary_key=True)
    nombre_estacion = models.CharField(max_length=150)
    id_rutas= models.ForeignKey(
        Rutas,
        on_delete=models.CASCADE,
        db_column='id_rutas'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre_estacion
    class Meta:
        db_table = 'estaciones'


class Mantenimiento (BaseModel):
    id_mantenimiento= models.AutoField(primary_key=True)
    id_vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete = models.CASCADE,
        db_column='id_vehiculo'
    )
    clase_matenimiento = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.clase_matenimiento
    class Meta:
        db_table = 'mantenimiento'



