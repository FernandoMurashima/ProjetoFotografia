from django.db import models
from django.contrib.auth.models import User  # tabela auth_user do Django

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    nome = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class RedesSociaisCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='redes_sociais')
    nome_rede = models.CharField(max_length=100)
    url_perfil = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.nome_rede} - {self.cliente.nome}"

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='enderecos', blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.logradouro or ''}, {self.numero or ''} - {self.cidade or ''}"

class Evento(models.Model):
    STATUS_CHOICES = [
        ('Agendado', 'Agendado'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]

    nome = models.CharField(max_length=255)
    tipo_evento = models.CharField(max_length=100, blank=True, null=True)
    data_evento = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='eventos')
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True, related_name='eventos')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Agendado')

    def __str__(self):
        return f"{self.nome} ({self.status})"

class PagamentoEvento(models.Model):
    STATUS_PAGAMENTO_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Cancelado', 'Cancelado'),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=50, blank=True, null=True)
    status_pagamento = models.CharField(max_length=50, choices=STATUS_PAGAMENTO_CHOICES, default='Pendente')

    def __str__(self):
        return f"Pagamento {self.id} - {self.status_pagamento}"

class Galeria(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    url_imagem = models.URLField(max_length=500)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, blank=True, null=True, related_name='galerias')

    def __str__(self):
        return self.titulo or "Imagem da Galeria"

class Sorteio(models.Model):
    STATUS_CHOICES = [
        ('Aberto', 'Aberto'),
        ('Encerrado', 'Encerrado'),
        ('Cancelado', 'Cancelado'),
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    regras = models.TextField(blank=True, null=True)
    data_sorteio = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Aberto')

    def __str__(self):
        return self.nome

class ParticipanteSorteio(models.Model):
    sorteio = models.ForeignKey(Sorteio, on_delete=models.CASCADE, related_name='participantes')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='sorteios_participados')
    foi_ganhador = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.nome} - {'Ganhador' if self.foi_ganhador else 'Participante'}"

class Promocao(models.Model):
    STATUS_CHOICES = [
        ('Ativa', 'Ativa'),
        ('Inativa', 'Inativa'),
        ('Expirada', 'Expirada'),
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Ativa')

    def __str__(self):
        return self.nome

class LogAtividades(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='logs_atividades')
    acao = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username if self.usuario else 'Sistema'} - {self.acao} - {self.data_hora}"
