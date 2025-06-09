# SimpleShop API

API de e-commerce baseada em FastAPI com CRUD de usuários e autenticação JWT.

## Funcionalidades

- Registro e autenticação de usuários (JWT)
- Listagem de produtos
- Criação e gerenciamento de pedidos
- Endpoints seguros com controle de acesso por função

## Primeiros Passos

### Pré-requisitos

- Python 3.9+
- pip

### Instalação

```bash
git clone https://github.com/Jaoow/simpleshop-api.git
cd simpleshop-api
pip install -r requirements.txt
```

### Executando a API

```bash
uvicorn main:app --reload
```

ou

```
bash
fastapi run
```

A API estará disponível em `http://127.0.0.1:8000`.

### Documentação da API

Acesse `http://127.0.0.1:8000/docs` para a documentação interativa Swagger.