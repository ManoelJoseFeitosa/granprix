# Este é o código correto para o arquivo 0003_auto_20251016_1924.py

from django.db import migrations
import os

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    # Nomes das variáveis de ambiente que você vai configurar no Render
    username = os.environ.get('ADMIN_USER')
    email = os.environ.get('ADMIN_EMAIL')
    password = os.environ.get('ADMIN_PASSWORD')

    # Só cria o usuário se as variáveis de ambiente existirem e o usuário não existir ainda
    if username and email and password and not User.objects.filter(username=username).exists():
        print(f'Criando superusuário {username}')
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print('Superusuário já existe ou variáveis de ambiente não configuradas.')


class Migration(migrations.Migration):

    dependencies = [
        # Esta linha diz que esta migração só pode rodar DEPOIS da migração 0002.
        ('core', '0002_votacao_criterios_alter_voto_escuderia'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]