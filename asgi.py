"""
ASGI config for granprix project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# CORRIGIDO: Aponta para o arquivo 'settings.py' na raiz do projeto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_asgi_application()