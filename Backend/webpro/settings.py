from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0+u99!##l5abq3(kjimj8&t-pnc0r5@r7jg3t072*zwqm!8w-x'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Aplicativos instalados
INSTALLED_APPS = [
    # Apps do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps de terceiros
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    # Seus apps
    'appfoto',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # precisa vir antes do CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Permitir qualquer origem (para desenvolvimento)
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'webpro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webpro.wsgi.application'

# Banco de dados
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'WebPro',
#        'USER': 'root',
#        'PASSWORD': 'ftju7439',
#        'HOST': 'localhost',
#        'PORT': '3306',
#        'OPTIONS': {
#            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#        }
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',
        'USER': 'root',
        'PASSWORD': 'cQtCBZIPH0ejonbhMtyHHUdTwASYBRd0',
        'HOST': 'mysql.railway.internal',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}





# Validação de senha
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

# Internacionalização
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Arquivos estáticos
STATIC_URL = 'static/'

# Configuração do Django REST Framework com Token Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.skymail.net.br'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  
EMAIL_HOST_USER = 'fernando@murashima.com.br'
EMAIL_HOST_PASSWORD = 'Ftju7439@@'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
