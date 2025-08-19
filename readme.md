🏋️ Projeto DB Backend — API de Gestão de Atletas

Este projeto é uma API desenvolvida com FastAPI para gerenciar dados de atletas, categorias e centros de treinamento. Utiliza SQLAlchemy para ORM, Alembic para migrações de banco de dados e está containerizado com Docker para facilitar o desenvolvimento e a implantação.

🚀 Tecnologias Utilizadas

FastAPI

SQLAlchemy

Alembic

Docker

PostgreSQL

Pydantic

📁 Estrutura do Projeto

projeto_db_backend/
├── alembic/                  # Migrações do banco de dados
├── projeto/
│   ├── atleta/               # Módulo de atletas
│   ├── categorias/           # Módulo de categorias
│   ├── centro_treinamento/  # Módulo de centros de treinamento
│   ├── configs/              # Configurações gerais
│   ├── contrib/              # Utilitários e helpers
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── routers.py            # Registro de rotas
├── docker-compose.yml        # Orquestração com Docker
├── Makefile                  # Comandos úteis para desenvolvimento
└── alembic.ini               # Configuração do Alembic

⚙️ Como Rodar Localmente

1. Clone o repositório

git clone https://github.com/Raphael2203/fastapi_docker_postgre.git
cd projeto

2. Configure o ambiente

Crie um arquivo .env com as variáveis de ambiente necessárias (exemplo em configs/env.py).

3. Suba os containers

docker-compose up --build

4. Acesse a documentação interativa

Acesse http://localhost:8000/docs para visualizar e testar os endpoints via Swagger UI.

🧪 Testes

Você pode rodar os testes com:

make test

📌 Funcionalidades

CRUD de atletas

Associação com categorias e centros de treinamento

Validação de dados com Pydantic

Documentação automática com Swagger

Migrações de banco com Alembic

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.