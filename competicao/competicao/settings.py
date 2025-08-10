import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CONFIGURAÇÕES DE PRODUÇÃO
# ==============================================================================

# ALTERADO: A Secret Key agora é lida de uma variável de ambiente no Render.
# É muito mais seguro do que deixá-la no código.
SECRET_KEY = os.environ.get('SECRET_KEY')

# ALTERADO: O modo DEBUG será 'False' em produção (no Render) e 'True'
# apenas se você definir a variável de ambiente DEBUG como 'True' localmente.
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# ALTERADO: Lista de hosts permitidos. No Render, ele adicionará automaticamente
# o endereço do seu site (ex: granprix.onrender.com).
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
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ALTERADO: Adicionado o Middleware do WhiteNoise para servir arquivos estáticos.
    # Deve vir logo após o SecurityMiddleware.
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Assumindo que seu arquivo urls.py principal está na pasta 'competicao'
ROOT_URLCONF = 'competicao.urls'

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

# Assumindo que seu arquivo wsgi.py principal está na pasta 'competicao'
WSGI_APPLICATION = 'competicao.wsgi.application'


# Database
# ALTERADO: A configuração do banco de dados agora lê a URL do banco PostgreSQL
# do Render. Se não encontrar, usa o SQLite localmente (para desenvolvimento).
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
# ALTERADO: Ajustei o fuso horário para 'America/Fortaleza', que é o mesmo de
# Teresina-PI e não tem horário de verão, evitando possíveis bugs com datas.
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ALTERADO: Configuração completa para arquivos estáticos em produção com WhiteNoise.
STATIC_URL = 'static/'
# O comando 'collectstatic' irá juntar todos os arquivos estáticos nesta pasta.
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Melhora o cache e a performance dos arquivos estáticos.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'