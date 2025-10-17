# core/management/commands/create_admin.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Cria um superusuário a partir de variáveis de ambiente se ele não existir.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('ADMIN_USER')
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')

        if not all([username, email, password]):
            self.stdout.write(self.style.ERROR('As variáveis de ambiente ADMIN_USER, ADMIN_EMAIL e ADMIN_PASSWORD devem ser definidas.'))
            return

        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f'Criando conta para o superusuário: {username}'))
            User.objects.create_superuser(email=email, username=username, password=password)
        else:
            self.stdout.write(self.style.WARNING(f'O superusuário {username} já existe.'))