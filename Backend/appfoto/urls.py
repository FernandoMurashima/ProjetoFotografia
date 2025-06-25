from rest_framework import routers
from django.urls import path, include
from .views import (
    ClienteViewSet, RedesSociaisClienteViewSet, EnderecoViewSet, EventoViewSet, PagamentoEventoViewSet,
    GaleriaViewSet, SorteioViewSet, ParticipanteSorteioViewSet, PromocaoViewSet, LogAtividadesViewSet
)

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'redes-sociais', RedesSociaisClienteViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'pagamentos', PagamentoEventoViewSet)
router.register(r'galerias', GaleriaViewSet)
router.register(r'sorteios', SorteioViewSet)
router.register(r'participantes-sorteio', ParticipanteSorteioViewSet)
router.register(r'promocoes', PromocaoViewSet)
router.register(r'logs', LogAtividadesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
