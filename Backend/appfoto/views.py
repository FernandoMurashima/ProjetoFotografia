from rest_framework import viewsets
from .models import (
    Cliente, RedesSociaisCliente, Endereco, Evento, PagamentoEvento, Galeria,
    Sorteio, ParticipanteSorteio, Promocao, LogAtividades
)
from .serializers import (
    ClienteSerializer, RedesSociaisClienteSerializer, EnderecoSerializer, EventoSerializer, PagamentoEventoSerializer,
    GaleriaSerializer, SorteioSerializer, ParticipanteSorteioSerializer, PromocaoSerializer, LogAtividadesSerializer
)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class RedesSociaisClienteViewSet(viewsets.ModelViewSet):
    queryset = RedesSociaisCliente.objects.all()
    serializer_class = RedesSociaisClienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class PagamentoEventoViewSet(viewsets.ModelViewSet):
    queryset = PagamentoEvento.objects.all()
    serializer_class = PagamentoEventoSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class SorteioViewSet(viewsets.ModelViewSet):
    queryset = Sorteio.objects.all()
    serializer_class = SorteioSerializer

class ParticipanteSorteioViewSet(viewsets.ModelViewSet):
    queryset = ParticipanteSorteio.objects.all()
    serializer_class = ParticipanteSorteioSerializer

class PromocaoViewSet(viewsets.ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer

class LogAtividadesViewSet(viewsets.ModelViewSet):
    queryset = LogAtividades.objects.all()
    serializer_class = LogAtividadesSerializer
