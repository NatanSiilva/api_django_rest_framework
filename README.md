## API Django Rest Framework
Este projeto é uma API construída em Django Rest Framework, possui endpoints para autenticação de usuários que implementa as operações CRUD (Create, Read, Update, Delete) para uma entidade de "Produtos".

# Instalação

Para instalar o projeto, siga os passos abaixo:

- Clone o repositório: git clone https://github.com/NatanSiilva/api_django_rest_framework.git
- Acesse a pasta do projeto: cd api_django_rest_framework
- Crie um ambiente virtual: python -m venv .venv
- Ative o ambiente virtual: source .venv/bin/activate (ou .venv/Scripts/activate no Windows)
- Instale as dependências: pip install -r requirements.txt
- Rode as migrações: python manage.py migrate

# Como rodar o projeto

Para rodar o projeto, execute o comando python manage.py runserver. A API estará disponível em http://localhost:8000/.

# Endpoints

A API possui os seguintes endpoints:

| Método | Endpoint               | Descrição                          |
| ------ | --------------------- | --------------------------------- |
| GET    | /api/produtos/         | Retorna a lista de produtos       |
| POST   | /api/produtos/         | Cria um novo produto              |
| GET    | /api/produtos/{id}/    | Retorna os detalhes de um produto |
| PUT    | /api/produtos/{id}/    | Atualiza um produto existente     |
| DELETE | /api/produtos/{id}/    | Deleta um produto existente       |


# Documentação da API
A documentação da API pode ser acessada em http://localhost:8000/swagger/ (Swagger) ou http://localhost:8000/redoc/ (Redoc).

# Tecnologias utilizadas
- Django
- Django Rest Framework
- SQLite

# Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
