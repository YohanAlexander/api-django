from rest_framework import serializers
from .models import Cliente
from .models import Endereco

from drf_writable_nested.serializers import WritableNestedModelSerializer

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ('foto', 'nome', 'sobrenome', 'cpf', 'rg', 'telefone', 'email')

class EnderecoSerializer(WritableNestedModelSerializer):

    cliente = ClienteSerializer()

    class Meta:

        model = Endereco
        fields = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cliente')

