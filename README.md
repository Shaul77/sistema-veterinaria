# 🐾 Sistema de Gestión Veterinaria — Backend API REST

Proyecto desarrollado con **Django** y **Django REST Framework (DRF)**, conectado a un motor de base de datos relacional **MySQL** a través de XAMPP. El sistema permite administrar de forma centralizada los procesos clínicos y administrativos de un centro veterinario mediante una arquitectura desacoplada, segura y escalable.

---

## 📑 Tabla de Contenidos
1. [Descripción General](#descripción-general)
2. [Arquitectura y Estructura del Proyecto](#arquitectura-y-estructura-del-proyecto)
3. [Modelo de Datos y Entidades](#modelo-de-datos-y-entidades)
4. [Tecnologías y Dependencias](#tecnologías-y-dependencias)
5. [Requisitos Previos](#requisitos-previos)
6. [Instalación y Puesta en Marcha](#instalación-y-puesta-en-marcha)
7. [Endpoints de la API y Ejemplos](#endpoints-de-la-api-y-ejemplos)
8. [Seguridad y Buenas Prácticas](#seguridad-y-buenas-prácticas)
9. [Resolución de Problemas Frecuentes](#resolución-de-problemas-frecuentes)

---

## Descripción General

Este backend expone una **API RESTful** que permite realizar operaciones de lectura y gestión de datos sobre las entidades fundamentales de una clínica veterinaria. Implementa serializadores para transformar modelos relacionales en respuestas estandarizadas en formato JSON, junto con un panel administrativo visual para la gestión interna.

El proyecto está diseñado bajo buenas prácticas:
* **Separación de responsabilidades:** lógica de negocio, serialización y enrutamiento claramente divididos.
* **Seguridad de credenciales:** uso de variables de entorno para evitar filtraciones de contraseñas.
* **Persistencia robusta:** motor relacional MySQL con integridad referencial (claves foráneas).

---

## Arquitectura y Estructura del Proyecto

El árbol de directorios del proyecto se organiza de la siguiente manera:

```text
sistema-veterinaria/
│
├── api/                        # Aplicación principal de la API
│   ├── migrations/             # Historial de migraciones hacia MySQL
│   ├── admin.py                # Registro de modelos en el panel de administración
│   ├── apps.py                 # Configuración del paquete de la app
│   ├── models.py               # Definición de tablas y relaciones ORM
│   ├── serializers.py          # Transformación de datos entre Modelos y JSON
│   ├── urls.py                 # Rutas específicas de los endpoints de la API
│   └── views.py                # Controladores y ViewSets de DRF
│
├── drf/                        # Módulo de configuración global del proyecto
│   ├── __init__.py             # Inicialización y puente PyMySQL
│   ├── asgi.py                 # Punto de entrada ASGI
│   ├── settings.py             # Configuración principal (DB, apps, middleware)
│   ├── urls.py                 # Enrutador principal del sistema
│   └── wsgi.py                 # Punto de entrada WSGI
│
├── .env.example                # Plantilla pública de variables de entorno requeridas
├── .gitignore                  # Reglas de exclusión para control de versiones Git
├── database.sql                # Respaldo estructural y datos iniciales de MySQL
├── manage.py                   # Utilidad CLI principal de Django
└── requirements.txt            # Lista de dependencias del entorno Python
```

---

## Modelo de Datos y Entidades

El sistema gestiona 4 entidades vinculadas mediante relaciones de clave foránea:

```text
   +---------------+          1 : N          +---------------+
   |     Dueno     |------------------------<|    Mascota    |
   +---------------+                         +---------------+
                                                     |
                                                     | 1 : N
                                                     v
   +---------------+          1 : N          +---------------+
   |  Veterinario  |------------------------<|AtencionMedica |
   +---------------+                         +---------------+
```

* **Dueño (`Dueno`):** Datos del cliente o tutor responsable (Nombre, RUT, Teléfono, Correo, Dirección).
* **Veterinario (`Veterinario`):** Profesional del centro médico (Nombre, Especialidad, Teléfono).
* **Mascota (`Mascota`):** Ficha del paciente animal, asociada directamente a un Dueño (Nombre, Especie, Raza, Edad).
* **Atención Médica (`AtencionMedica`):** Registro de consulta clínica, asociada a una Mascota y al Veterinario que realizó la atención (Fecha, Motivo de consulta, Diagnóstico, Tratamiento).

---

## Tecnologías y Dependencias

* **Lenguaje:** Python 3.10+
* **Framework Web:** Django (4.x / 5.x)
* **API Toolkit:** Django REST Framework
* **Base de Datos:** MySQL Server (mediante XAMPP)
* **Conector DB:** PyMySQL
* **Gestor de Variables de Entorno:** python-decouple / python-dotenv
* **Control de Versiones:** Git y GitHub

---

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de contar con:
1. **Python 3.10+** instalado y agregado al `PATH`.
2. **XAMPP** instalado (con módulos Apache y MySQL en ejecución).
3. **Git** instalado en el equipo.

---

## Instalación y Puesta en Marcha

### Paso 1: Iniciar el servidor de Base de Datos
1. Abre el panel de control de **XAMPP**.
2. Haz clic en **Start** junto a los servicios **Apache** y **MySQL**.
3. Verifica el acceso en tu navegador: `http://localhost/phpmyadmin`.

### Paso 2: Clonar el repositorio
Abre una terminal y descarga el proyecto:

```bash
git clone https://github.com/Shaul77/sistema-veterinaria.git
cd sistema-veterinaria
```

### Paso 3: Crear y activar el entorno virtual

* **En Windows (PowerShell):**
```powershell
python -m venv env
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\activate
```

* **En Linux / macOS:**
```bash
python3 -m venv env
source env/bin/activate
```

### Paso 4: Instalar las dependencias
Con el entorno virtual activo `(env)`, instala los paquetes:

```bash
pip install -r requirements.txt
```

### Paso 5: Configurar variables de entorno (`.env`)
1. Crea un archivo llamado `.env` en la raíz del proyecto tomando como base `.env.example`.
2. Completa los valores locales:

```env
SECRET_KEY=clave_secreta_django_aqui
DEBUG=True

DB_NAME=veterinaria_db
DB_USER=root
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306
```

### Paso 6: Configurar la Base de Datos
* **Opción con migraciones (Recomendada):**
  1. Crea una base de datos vacía llamada `veterinaria_db` en phpMyAdmin.
  2. Ejecuta en la terminal:
```bash
python manage.py migrate
```

* **Opción con script SQL:**
  1. Crea la base de datos `veterinaria_db` en phpMyAdmin.
  2. Entra a la pestaña **Importar**, selecciona el archivo `database.sql` de la raíz del proyecto y haz clic en **Continuar**.

### Paso 7: Iniciar el servidor
Ejecuta:

```bash
python manage.py runserver
```

El servidor quedará activo en: `[http://127.0.0.1:8000/](http://127.0.0.1:8000/)`.

---

## Endpoints de la API y Ejemplos

La API REST cuenta con una interfaz web interactiva disponible en: `[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)`.

### Endpoints Disponibles

| Método HTTP | Endpoint | Descripción | Parámetros / Payload |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/duenos/` | Listar todos los dueños | Ninguno |
| `POST` | `/api/duenos/` | Registrar un dueño | JSON con datos del dueño |
| `GET` | `/api/duenos/{id}/` | Detalle de un dueño | ID en URL |
| `GET` | `/api/veterinarios/` | Listar todos los veterinarios | Ninguno |
| `POST` | `/api/veterinarios/` | Registrar un veterinario | JSON del veterinario |
| `GET` | `/api/mascotas/` | Listar todas las mascotas | Ninguno |
| `POST` | `/api/mascotas/` | Registrar una mascota | JSON con datos y `dueno` (ID) |
| `GET` | `/api/atenciones/` | Listar atenciones clínicas | Ninguno |
| `POST` | `/api/atenciones/` | Registrar atención | JSON con `mascota` (ID) y `veterinario` (ID) |

---

### Ejemplo de Petición y Respuesta JSON

**Petición `POST` a `/api/mascotas/`:**
```json
{
  "nombre": "Rocky",
  "especie": "Canino",
  "raza": "Golden Retriever",
  "edad": 3,
  "dueno": 1
}
```

**Respuesta `201 Created`:**
```json
{
  "id": 1,
  "nombre": "Rocky",
  "especie": "Canino",
  "raza": "Golden Retriever",
  "edad": 3,
  "dueno": 1
}
```

---

## Seguridad y Buenas Prácticas

* **Variables de Entorno:** Credenciales de base de datos (`DB_USER`, `DB_PASSWORD`), host y `SECRET_KEY` se cargan en memoria y nunca se suben al repositorio.
* **Reglas en `.gitignore`:** Se excluyen del control de versiones los entornos virtuales (`env/`), archivos temporales de Python (`__pycache__/`) y archivos de configuración sensible (`.env`).
* **Plantilla `.env.example`:** Permite que cualquier evaluador clone y configure el proyecto de manera inmediata sin exponer datos reales.

---

## Resolución de Problemas Frecuentes

* **Error de conexión a la base de datos (`Can't connect to MySQL server`):**
  Asegúrate de que el servicio **MySQL** esté iniciado en XAMPP y que el puerto configurado en el archivo `.env` sea `3306`.

* **Error al activar el entorno virtual en PowerShell (`ExecutionPolicy`):**
  Ejecuta en PowerShell con permisos de usuario:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

* **Error `Table 'veterinaria_db.api_dueno' doesn't exist`:**
  Ejecuta las migraciones pendientes con `python manage.py migrate` o importa el archivo `database.sql` en phpMyAdmin.