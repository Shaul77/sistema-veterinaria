# 🐾 Sistema de Gestión Veterinaria — Backend API REST

Proyecto desarrollado con **Django** y **Django REST Framework (DRF)**, conectado a un motor de base de datos relacional **MySQL** a través de XAMPP. El sistema permite administrar de forma centralizada los procesos clínicos y administrativos de un centro veterinario mediante una arquitectura desacoplada, segura y escalable.

---

## 📑 Tabla de Contenidos
1. [Descripción General](#-descripción-general)
2. [Arquitectura y Estructura del Proyecto](#-arquitectura-y-estructura-del-proyecto)
3. [Modelo de Datos y Entidades](#-modelo-de-datos-y-entidades)
4. [Tecnologías y Dependencias](#-tecnologías-y-dependencias)
5. [Requisitos Previos](#-requisitos-previos)
6. [Instalación y Puesta en Marcha (Paso a Paso)](#-instalación-y-puesta-en-marcha-paso-a-paso)
7. [Endpoints de la API y Ejemplos de Uso](#-endpoints-de-la-api-y-ejemplos-de-uso)
8. [Seguridad y Buenas Prácticas Implementadas](#-seguridad-y-buenas-prácticas-implementadas)
9. [Resolución de Problemas Frecuentes](#-resolución-de-problemas-frecuentes)

---

## 📖 Descripción General

Este backend expone una **API RESTful** que permite realizar operaciones de lectura y gestión de datos sobre las entidades fundamentales de una clínica veterinaria. Implementa serializadores para transformar modelos relacionales en respuestas estandarizadas en formato JSON, junto con un panel administrativo visual para la gestión interna.

El proyecto está diseñado bajo buenas prácticas de la industria:
* **Separación de responsabilidades:** lógica de negocio, serialización y enrutamiento claramente divididos.
* **Seguridad de credenciales:** uso de variables de entorno para evitar filtraciones de contraseñas.
* **Persistencia robusta:** motor relacional MySQL con integridad referencial (claves foráneas).

---

## 🏛️ Arquitectura y Estructura del Proyecto

El árbol de directorios está organizado de la siguiente manera:

```plaintext
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

🗄️ Modelo de Datos y EntidadesEl sistema gestiona 4 entidades vinculadas mediante relaciones de clave foránea:Plaintext   +---------------+          1 : N          +---------------+
   |     Dueno     |------------------------<|    Mascota    |
   +---------------+                         +---------------+
                                                     |
                                                     | 1 : N
                                                     v
   +---------------+          1 : N          +---------------+
   |  Veterinario  |------------------------<|AtencionMedica |
   +---------------+                         +---------------+
Dueño (Dueno): Datos del cliente o tutor responsable (Nombre, RUT, Teléfono, Correo, Dirección).Veterinario (Veterinario): Profesional del centro médico (Nombre, Especialidad, Teléfono).Mascota (Mascota): Ficha del paciente animal, asociada directamente a un Dueño (Nombre, Especie, Raza, Edad).Atención Médica (AtencionMedica): Registro de consulta clínica, asociada a una Mascota y al Veterinario que realizó la atención (Fecha, Motivo de consulta, Diagnóstico, Tratamiento).💻 Tecnologías y DependenciasLenguaje: Python 3.10+Framework Web: Django (4.x / 5.x)API Toolkit: Django REST FrameworkBase de Datos: MySQL Server (mediante XAMPP)Conector DB: PyMySQL / mysqlclientGestor de Variables de Entorno: python-decouple / python-dotenvControl de Versiones: Git y GitHub⚙️ Requisitos PreviosAntes de ejecutar el proyecto en una máquina limpia, asegúrate de contar con:Python 3.10+ instalado y agregado al PATH del sistema.XAMPP instalado (con módulos Apache y MySQL funcionales).Git instalado en el equipo.🚀 Instalación y Puesta en Marcha (Paso a Paso)Paso 1: Iniciar el servidor de Base de DatosAbre el panel de control de XAMPP.Haz clic en Start junto a los servicios Apache y MySQL.Abre tu navegador y verifica el acceso en: http://localhost/phpmyadmin.Paso 2: Clonar el repositorioAbre una terminal (PowerShell, CMD o Bash) y ejecuta:Bashgit clone [https://github.com/Shaul77/sistema-veterinaria.git](https://github.com/Shaul77/sistema-veterinaria.git)
cd sistema-veterinaria
Paso 3: Crear y activar el entorno virtualAislar las librerías asegura que el proyecto funcione de manera independiente al resto del sistema operativo:En Windows (PowerShell):PowerShellpython -m venv env
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\activate
En Linux / macOS:Bashpython3 -m venv env
source env/bin/activate
(Notarás el prefijo (env) a la izquierda de la línea de comandos).Paso 4: Instalar las dependenciasCon el entorno virtual activo, descarga los paquetes necesarios:Bashpip install -r requirements.txt
Paso 5: Configurar variables de entorno (.env)Por estándares de seguridad, las credenciales reales no se versionan en Git:Copia el archivo de muestra:Bashcp .env.example .env
(En Windows CMD puedes usar copy .env.example .env).Abre el archivo .env creado y verifica los parámetros de conexión local:Fragmento de códigoSECRET_KEY=clave_secreta_django_aqui
DEBUG=True

DB_NAME=veterinaria_db
DB_USER=root
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306
Paso 6: Configuración de la Base de DatosTienes dos alternativas para cargar la base de datos:Opción A (Importación directa desde phpMyAdmin):Entra a http://localhost/phpmyadmin.Crea una base de datos llamada veterinaria_db.Haz clic en la pestaña Importar, selecciona el archivo database.sql ubicado en la raíz del proyecto y presiona Continuar.Opción B (Migraciones de Django):Crea la base de datos vacía veterinaria_db en phpMyAdmin.Ejecuta en la terminal:Bashpython manage.py migrate
Paso 7: Crear superusuario (Opcional, para acceso al admin)Si deseas ingresar al panel web administrativo con un nuevo usuario:Bashpython manage.py createsuperuser
Completa nombre de usuario, correo y contraseña.Paso 8: Levantar el servidor de desarrolloInicia la aplicación:Bashpython manage.py runserver
El servidor estará activo y escuchando peticiones en: http://127.0.0.1:8000/.🌐 Endpoints de la API y Ejemplos de UsoLa API REST cuenta con una interfaz web interactiva (Browsable API) disponible en http://127.0.0.1:8000/api/.Tabla de Endpoints DisponiblesMétodo HTTPEndpointDescripciónParámetros / PayloadGET/api/duenos/Listar todos los dueñosN/APOST/api/duenos/Crear un nuevo dueñoObjeto JSON con datos del dueñoGET/api/duenos/{id}/Consultar detalle de un dueñoID en URLGET/api/veterinarios/Listar todos los veterinariosN/APOST/api/veterinarios/Registrar un nuevo veterinarioObjeto JSON del veterinarioGET/api/mascotas/Listar todas las mascotasN/APOST/api/mascotas/Registrar una mascotaJSON incluyendo dueno (ID)GET/api/atenciones/Listar atenciones clínicasN/APOST/api/atenciones/Registrar una atención médicaJSON con mascota (ID) y veterinario (ID)Ejemplo de Petición y Respuesta (JSON)Petición POST a /api/mascotas/JSON{
  "nombre": "Rocky",
  "especie": "Canino",
  "raza": "Golden Retriever",
  "edad": 3,
  "dueno": 1
}
Respuesta 201 CreatedJSON{
  "id": 1,
  "nombre": "Rocky",
  "especie": "Canino",
  "raza": "Golden Retriever",
  "edad": 3,
  "dueno": 1
}
🛡️ Seguridad y Buenas Prácticas ImplementadasPrincipio de Mínima Exposición: Las credenciales de base de datos (DB_USER, DB_PASSWORD), el host y la SECRET_KEY se extraen en tiempo de ejecución desde variables de entorno.Control de Exclusiones con .gitignore: Se bloquea activamente el seguimiento de:Archivos de entorno (.env, .envrc).Entornos virtuales (env/, venv/).Archivos temporales de ejecución y bytecode (__pycache__/, *.pyc).Documentación de Entorno (.env.example): Se provee una plantilla clara para permitir el despliegue del proyecto en otros entornos sin comprometer información sensible.🔧 Resolución de Problemas FrecuentesError de conexión a la base de datos (Can't connect to MySQL server on '127.0.0.1'):Asegúrate de que el módulo MySQL esté en verde (iniciado) en el panel de XAMPP.Verifica que el puerto en tu .env sea el 3306.Error al ejecutar scripts en PowerShell (Activate.ps1 cannot be loaded...):Ejecuta en la terminal con permisos de usuario:PowerShellSet-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
Error Table 'veterinaria_db.api_dueno' doesn't exist:La base de datos no tiene las tablas creadas. Ejecuta python manage.py migrate o importa el archivo database.sql en phpMyAdmin.
