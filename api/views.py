from django.shortcuts import render
from rest_framework import viewsets

from .models import Cliente
from .serializers import ClienteSerializer

from .models import Endereco
from .serializers import EnderecoSerializer

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        return Endereco.objects.filter(cliente=self.kwargs['cliente_pk'])


def index(request):

    enderecos = Endereco.objects.all()

    context = {
        # 'nome': enderecos.cliente.nome,
        # 'sobrenome': enderecos.cliente.nome,
        # 'cpf': enderecos.cliente.cpf,
        # 'rg': enderecos.cliente.rg,
        # 'telefone': enderecos.cliente.telefone,
        # 'email': enderecos.cliente.email,
        # 'logradouro': enderecos.logradouro,
        # 'numero': enderecos.numero,
        # 'bairro': enderecos.bairro,
        # 'cidade': enderecos.cidade,
        # 'estado': enderecos.estado,
        'enderecos': enderecos,
    }

    return render(request, 'index.html', context)

