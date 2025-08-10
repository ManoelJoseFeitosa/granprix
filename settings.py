import os
import dj_database_url
from pathlib import Path

# CORRIGIDO: Com a nova estrutura, o BASE_DIR aponta para o diretório pai do arquivo settings.py,
# que agora é a raiz do projeto.
BASE_DIR = Path(__file__).resolve().parent


# ==============================================================================
# CONFIGURAÇÕES DE PRODUÇÃO
# ==============================================================================

# A Secret Key agora é lida de uma variável de ambiente no Render.
SECRET_KEY = os.environ.get('SECRET_KEY')

# O modo DEBUG será 'False' em produção (no Render).
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Lista de hosts permitidos. No Render, ele adicionará automaticamente o endereço do seu site.
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'votacao.apps.VotacaoConfig', # Adicionei seu app 'votacao' aqui, pois ele aparece na sua estrutura
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORRIGIDO: Aponta para o arquivo urls.py na raiz do projeto.
ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Adicionado para que o Django encontre sua pasta de templates na raiz.
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

# CORRIGIDO: Aponta para o arquivo wsgi.py na raiz do projeto.
WSGI_APPLICATION = 'wsgi.application'


# Database
# A configuração do banco de dados agora lê a URL do banco PostgreSQL do Render.
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'
    )
}


# Password validation
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


# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# Configuração para arquivos estáticos em produção com WhiteNoise.
STATIC_URL = 'static/'
# O comando 'collectstatic' irá juntar todos os arquivos estáticos nesta pasta.
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'