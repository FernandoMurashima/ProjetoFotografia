from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Cliente, RedesSociaisCliente, Endereco, Evento, PagamentoEvento, Galeria,
    Sorteio, ParticipanteSorteio, Promocao, LogAtividades, Orcamento,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Cliente
        fields = ['id', 'user', 'nome', 'email', 'telefone', 'data_cadastro']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        cliente = Cliente.objects.create(user=user, **validated_data)
        return cliente

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.save()
        return super().update(instance, validated_data)

class RedesSociaisClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedesSociaisCliente
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class PagamentoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagamentoEvento
        fields = '__all__'

class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galeria
        fields = '__all__'

class SorteioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorteio
        fields = '__all__'

class ParticipanteSorteioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipanteSorteio
        fields = '__all__'

class PromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocao
        fields = '__all__'

class LogAtividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAtividades
        fields = '__all__'

class AgendarEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = [
            'nome',
            'tipo_evento',
            'data_evento',
            'descricao',
            'quantidade_pessoas',
            'duracao_horas',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'estado',
            'cep'
        ]

    def create(self, validated_data):
        cliente = self.context['request'].user.cliente
        return Evento.objects.create(cliente=cliente, status='Agendado', **validated_data)

class OrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orcamento
        fields = [
            'idorcamento',
            'nome_requisitante',
            'tipo_evento',
            'data_desejada',
            'horario',
            'quantidade_pessoas',
            'duracao_horas',
            'valor',
            'forma_pagamento',
            'parcelado',
            'celular',
            'email',
            'descricao',
            'status',
            'data_solicitacao',
        ]
        read_only_fields = ['status', 'data_solicitacao']

