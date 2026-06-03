# api_gestion_de_trasporte-
proyecto para la evaluacion de apis desde ceros individual para ADSO

# Aclaraciones en Readme 

- Informacion general 
    - Sistema de gestion de trasporte 
    - Cristian David Barrera 
    - 

- Tecnologias utilizadas
    - Python 
    - Django 
    - PostgreSQL
    - Swagger 

- Instalaciones 
   ## Instalación

### Clonación del repositorio

```bash
git clone https://github.com/CristianBarrera512/api_gestion_de_trasporte-.git
PS C:\Users\Aprendiz Tarde\OneDrive> cd .\api_django_yoplay\
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

```bash
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu_clave_secreta
DEBUG=True
DB_NAME=mi_base_datos
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

### Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### Ejecutar servidor

```bash
python manage.py runserver
```

### Acceder a la aplicación

```text
http://127.0.0.1:8000/
```

## Guia de Aprendizaje 
Desarrollo de APIs CRUD con Django y postgreSQL

## Objetivo General
Diseñar e implementar una API CRUD utilizando Django y PostgreSQL que permita resolver un
problema específico del mundo real, aplicando buenas prácticas de desarrollo,
documentación y control de versiones.

### Caracteristicas del proyecto 

- Base de Datos 
    - Diseñp del modelo relacional
    - Creacion de esquema (schema) en postgresSQL
    - implementacion de minimo 8 tablas.
    - cada tabla debera contener como minimo:
        activo 
        fecha_creacion
        fecha_modificacion 
    - minimo 4 relaciones entre tablas 

- Backend
    - Python
    - Django
    - Django REST Framework
    - PostgreSQL

- Configuracion 
    implementar
    - archivo .env
    - variables de entorno 
    - configuracion de conexion a PostgreSQL

## Obligacion de tener  

- 1 Swagger para documentación
- 2 Versionado de API
- 3 Respuestas JSON estandarizadas
- 4 Paginación
- 5 Filtros
- 6 Ordenamiento
- 7 Soft Delete
- 8 Auditoría de registros
- 9 Autenticación JWT
- 10 Roles y permisos
- 11 Relaciones anidadas (Nested Serializers)
- 12 Exportación de información (Excel o CSV)
- 13 Logging de operaciones



## Características Implementadas

- [ ] Swagger para documentación
- [ ] Versionado de API
- [ ] Respuestas JSON estandarizadas
- [ ] Paginación
- [ ] Filtros
- [ ] Ordenamiento
- [ ] Soft Delete
- [ ] Auditoría de registros
- [ ] Autenticación JWT
- [ ] Roles y permisos
- [ ] Relaciones anidadas (Nested Serializers)
- [ ] Exportación de información (Excel o CSV)
- [ ] Logging de operaciones