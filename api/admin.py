from django.contrib import admin
from .models import Cliente
from .models import Endereco

from imagekit.admin import AdminThumbnail

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'rg', 'telefone', 'email', 'endereco', 'image')
    image = AdminThumbnail(image_field='foto')

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco, EnderecoAdmin)

