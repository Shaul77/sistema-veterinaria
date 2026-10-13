# Sistema de Gestion Veterinaria

Proyecto desarrollado en Django y Django REST Framework para la administracion de una clinica veterinaria, utilizando MySQL como base de datos relacional. Corresponde a la Evaluacion 3 del curso de desarrollo backend.

El sistema cuenta con un portal web con inicio de sesion, vistas protegidas para el personal de la clinica y una API RESTful completa para la administracion de los registros.

---

## Funcionalidades principales

### 1. Seguridad y Control de Acceso
* **Autenticacion:** Inicio de sesion y cierre de sesion seguro usando el sistema de usuarios de Django.
* **Proteccion de rutas:** Si un usuario sin registrar intenta ingresar a las zonas privadas (`/dashboard/` o `/reporte/`), el sistema bloquea el acceso de inmediato y lo redirige a la pantalla de login (`302 Found`).
* **Variables de entorno:** La clave secreta del proyecto y las contraseñas de la base de datos se manejan en un archivo `.env` para no exponer datos sensibles.

### 2. Vistas Protegidas del Sistema
* **Panel de Control (FBV):** Vista basada en funcion (`/dashboard/`) protegida con `@login_required`. Muestra tarjetas con el resumen en tiempo real del total de dueños, mascotas, veterinarios y atenciones registradas.
* **Reporte de Atenciones (CBV):** Vista basada en clase (`/reporte/`) protegida con `LoginRequiredMixin`. Muestra la tabla con el historial de atenciones medicas, fechas y diagnosticos de los pacientes.

### 3. API RESTful (CRUD)
Se implementaron los endpoints necesarios con Django REST Framework para gestionar el modelo de dueños:

* **GET /api/duenos/**: Lista todos los dueños registrados en formato JSON (Codigo 200).
* **POST /api/duenos/**: Permite ingresar y registrar un nuevo dueño en el sistema (Codigo 201).
* **GET /api/duenos/<id>/**: Consulta la informacion detallada de un dueño en particular por su ID (Codigo 200).
* **PUT /api/duenos/<id>/**: Actualiza los datos completos de un dueño existente (Codigo 200).
* **PATCH /api/duenos/<id>/**: Modifica campos individuales de un dueño (Codigo 200).
* **DELETE /api/duenos/<id>/**: Borra permanentemente el registro de la base de datos (Codigo 204).

---

## Tecnologias utilizadas

* Python 3.13
* Django
* Django REST Framework
* MySQL
* mysqlclient / PyMySQL
* HTML / CSS
* Git y GitHub

---

## Estructura de URLs del proyecto

| Ruta | Tipo | Acceso | Descripcion |
| --- | --- | --- | --- |
| `/` | Publica | Abierto | Pagina de bienvenida al sistema |
| `/login/` | Publica | Abierto | Formulario para iniciar sesion |
| `/logout/` | Protegida | Usuario logueado | Cierre de sesion del usuario |
| `/dashboard/` | Protegida (FBV) | Solo personal | Panel principal con conteo de registros |
| `/reporte/` | Protegida (CBV) | Solo personal | Listado de atenciones medicas |
| `/api/duenos/` | API REST | Gestion de datos | Consulta general y creacion de dueños |
| `/api/duenos/<id>/` | API REST | Gestion de datos | Consulta, edicion y eliminacion por ID |

---

## Instalacion y ejecucion local

### 1. Clonar el repositorio
```bash
git clone https://github.com/Shaul77/sistema-veterinaria.git
cd sistema-veterinaria
```

### 2. Activar el entorno virtual
```bash
# En Windows (PowerShell)
.\env\Scripts\activate
```

### 3. Instalar las librerias requeridas
```bash
pip install -r requirements.txt
```

### 4. Configuracion de la base de datos
Crear un archivo llamado `.env` en la raiz del proyecto con los datos de conexion a MySQL:

```env
SECRET_KEY=tu_clave_secreta
DEBUG=True

DB_NAME=veterinaria_db
DB_USER=root
DB_PASSWORD=tu_clave_mysql
DB_HOST=127.0.0.1
DB_PORT=3306
```

### 5. Iniciar la aplicacion
```bash
python manage.py migrate
python manage.py runserver
```

El proyecto se puede abrir en el navegador ingresando a `http://127.0.0.1:8000/`.