# Desafio ma9

### Instalando dependências

Na raiz do projeto acesse o terminal e execute:
```
pip install pipenv
pipenv install
```

### Criando o banco de dados

Crie o banco de dados `SQL` com base nos modelos:

```
python manage.py makemigrations
python manage.py migrate
```

### Criando um usuário

Crie um usúario para acessar a área administrativa:

```
python manage.py createsuperuser
```

### Servindo o projeto

Use o servidor para ambiente de desenvolvimento do `Django`:

```
python manage.py runserver
```

### Acessando o CRUD

Abra o navegador e acesse o CRUD para alterar o banco de dados:

```
firefox localhost:8000/admin
```

### Acessando a API

Abra o navegador e acessa a API para alterar o banco de dados:

```
firefox localhost:8000/api/cliente/<pk>/endereco/<pk>
```

