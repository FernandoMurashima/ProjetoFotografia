# appfoto/admin.py

from django.contrib import admin
from .models import (
    Cliente, RedesSociaisCliente, Endereco, Evento, PagamentoEvento, Galeria,
    Sorteio, ParticipanteSorteio, Promocao, LogAtividades
)

admin.site.register(Cliente)
admin.site.register(RedesSociaisCliente)
admin.site.register(Endereco)
admin.site.register(Evento)
admin.site.register(PagamentoEvento)
admin.site.register(Galeria)
admin.site.register(Sorteio)
admin.site.register(ParticipanteSorteio)
admin.site.register(Promocao)
admin.site.register(LogAtividades)
