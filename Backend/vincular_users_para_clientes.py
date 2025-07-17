import django
import os

# Configurar o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webpro.settings")
django.setup()

from django.contrib.auth.models import User
from appfoto.models import Cliente

from django.utils.text import slugify

clientes_sem_user = Cliente.objects.filter(user__isnull=True)

print(f"Clientes sem user: {clientes_sem_user.count()}")

for cliente in clientes_sem_user:
    # Gera um username único baseado no nome
    base_username = slugify(cliente.nome).replace('-', '')[:15]
    username = base_username
    suffix = 1
    while User.objects.filter(username=username).exists():
        username = f"{base_username}{suffix}"
        suffix += 1

    # Cria usuário
    user = User.objects.create_user(
        username=username,
        email=cliente.email or '',
        password="123456"  # senha padrão
    )

    # Associa ao cliente
    cliente.user = user
    cliente.save()

    print(f"✔️ Vinculado {cliente.nome} ao usuário '{username}'")

print("Finalizado.")
