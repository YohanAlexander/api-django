from django.contrib import admin
from .models import Cliente
from .models import Endereco

from imagekit.admin import AdminThumbnail

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'rg', 'telefone', 'email', 'image')
    image = AdminThumbnail(image_field='foto')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cliente')

