from django.db import models
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Cliente(models.Model):

    foto = models.ImageField('Foto', upload_to='fotos')
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    cpf = CPFField('CPF', primary_key=True)
    rg = models.CharField('RG', max_length=100)
    telefone = PhoneNumberField('Telefone')
    email = models.EmailField('Email', max_length=100)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.nome

class Endereco(models.Model):

    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)

    def __str__(self):
        return f'{self.logradouro} - {self.numero} - {self.bairro} - {self.cidade} - {self.estado}'

