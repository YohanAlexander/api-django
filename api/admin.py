from django.contrib import admin
from .models import Cliente
from .models import Endereco

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('foto', 'nome', 'sobrenome', 'cpf', 'rg', 'telefone', 'email', 'endereco')


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco, EnderecoAdmin)

