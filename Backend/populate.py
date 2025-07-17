# populate.py
import os
import django
from django.utils import timezone

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpro.settings')
django.setup()

from django.contrib.auth.models import User
from appfoto.models import Cliente, Evento

# Criar ou recuperar usuário
user1, _ = User.objects.get_or_create(username='maria', defaults={'email': 'maria@email.com'})
user1.set_password('senha123')  # Define a senha, se for novo
user1.save()

user2, _ = User.objects.get_or_create(username='joao', defaults={'email': 'joao@email.com'})
user2.set_password('senha123')
user2.save()

# Criar ou recuperar cliente
cliente1, _ = Cliente.objects.get_or_create(
    user=user1,
    defaults={'nome': 'Maria Oliveira', 'email': 'maria@email.com', 'telefone': '21999999999'}
)

cliente2, _ = Cliente.objects.get_or_create(
    user=user2,
    defaults={'nome': 'João Souza', 'email': 'joao@email.com', 'telefone': '21988888888'}
)

# Criar eventos de teste
Evento.objects.get_or_create(
    nome='Ensaio Infantil',
    tipo_evento='Infantil',
    data_evento='2025-07-20',
    descricao='Sessão temática infantil',
    cliente=cliente1
)

Evento.objects.get_or_create(
    nome='Casamento',
    tipo_evento='Casamento',
    data_evento='2025-08-01',
    descricao='Cobertura completa do casamento',
    cliente=cliente2
)

print("Clientes e eventos populados com sucesso!")
