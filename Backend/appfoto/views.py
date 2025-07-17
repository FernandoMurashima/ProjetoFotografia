from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail

from .models import (
    Cliente, RedesSociaisCliente, Endereco, Evento, PagamentoEvento, Galeria,
    Sorteio, ParticipanteSorteio, Promocao, LogAtividades, Orcamento
)
from .serializers import (
    ClienteSerializer, RedesSociaisClienteSerializer, EnderecoSerializer, EventoSerializer, PagamentoEventoSerializer,
    GaleriaSerializer, SorteioSerializer, ParticipanteSorteioSerializer, PromocaoSerializer, LogAtividadesSerializer,
    AgendarEventoSerializer, OrcamentoSerializer
)

# -------------------- ViewSets --------------------

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

# -------------------- Autenticação --------------------

class RegistrarClienteView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        nome = data.get('nome')
        telefone = data.get('telefone')

        if not username or not password or not nome:
            return Response({'error': 'Campos obrigatórios faltando'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        cliente = Cliente.objects.create(user=user, nome=nome, email=email, telefone=telefone)
        token = Token.objects.create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.id,
            'cliente_id': cliente.id,
            'username': user.username,
            'email': user.email,
        }, status=status.HTTP_201_CREATED)

class LoginClienteView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Usuário ou senha inválidos'}, status=status.HTTP_401_UNAUTHORIZED)

class AgendarEventoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("Recebido POST em /api/eventos/ com dados:", request.data)
        serializer = AgendarEventoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            evento = serializer.save()
            print("Evento criado com sucesso:", evento)
            return Response({'mensagem': 'Evento agendado com sucesso', 'id': evento.id}, status=201)
        else:
            print("Erros de validação:", serializer.errors)
            return Response(serializer.errors, status=400)

class OrcamentoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrcamentoSerializer(data=request.data)
        if serializer.is_valid():
            orcamento = serializer.save()

            # Enviar e-mail de notificação
            send_mail(
                subject='Nova solicitação de orçamento',
                message=f"Novo orçamento solicitado:\n\n"
                        f"Nome: {orcamento.nome_requisitante}\n"
                        f"Tipo: {orcamento.tipo_evento}\n"
                        f"Data: {orcamento.data_desejada} às {orcamento.horario}\n"
                        f"Pessoas: {orcamento.quantidade_pessoas or 'N/A'}\n"
                        f"Duração: {orcamento.duracao_horas or 'N/A'} horas\n"
                        f"Valor: {orcamento.valor or 'N/A'}\n"
                        f"Pagamento: {orcamento.forma_pagamento or 'N/A'}\n"
                        f"Parcelado: {'Sim' if orcamento.parcelado else 'Não'}\n"
                        f"Celular: {orcamento.celular or 'N/A'}\n"
                        f"Email: {orcamento.email or 'N/A'}\n"
                        f"Descrição: {orcamento.descricao or ''}",
                from_email=None,
                recipient_list=['takeshimurashima@gmail.com'],
                fail_silently=False,
            )

            return Response({'mensagem': 'Solicitação enviada com sucesso'}, status=201)
        return Response(serializer.errors, status=400)
