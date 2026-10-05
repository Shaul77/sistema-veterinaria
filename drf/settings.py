from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para la seguridad de la aplicacion
SECRET_KEY = 'django-insecure-j7pi0t06^tn569#)bcx)x5c6&iii$w&_#1hovz60l^7+n0frkc'

# Modo depuracion: True para desarrollo, False para activar la pagina de error 404 personalizada
DEBUG = False

# Dominios o direcciones IP permitidas para acceder al sitio
ALLOWED_HOSTS = ['*']

# Aplicaciones instaladas y activas en el proyecto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',  # Nuestra aplicacion de la veterinaria
]

# Capas intermedias que procesan peticiones y respuestas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo de rutas principales del proyecto
ROOT_URLCONF = 'drf.urls'

# Configuracion del motor de plantillas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Carpeta donde se buscan las plantillas HTML como bienvenida y el error 404
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Conexion con el servidor web
WSGI_APPLICATION = 'drf.wsgi.application'

# Configuracion de la base de datos (SQLite por defecto)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Reglas de validacion para las contraseñas de usuarios
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Idioma y zona horaria
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# Ruta para servir archivos estaticos (CSS, imagenes)
STATIC_URL = 'static/'

# Tipo de clave primaria por defecto para los modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuracion de envio de correos por consola para pruebas
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}