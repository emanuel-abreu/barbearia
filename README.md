# Barbearia API

Este projeto é uma API desenvolvida para gerenciar uma barbearia, utilizando **Python** e gerenciador de pacotes **Poetry**. Ele faz uso de variáveis de ambiente armazenadas em um arquivo `.env` para configuração sensível.

## Requisitos

Antes de começar, certifique-se de ter instalado:

- [Python 3.12+](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

## Instalação

Siga os passos abaixo para configurar e rodar o projeto localmente.

### 1. Clonando o repositório

```bash
git clone <URL-do-repositório>
cd barbearia
```

### 2. Configuração do ambiente

#### 2.1. Instalar as dependências do projeto com o Poetry

Certifique-se de estar no diretório raiz do projeto (onde está o arquivo `pyproject.toml`) e execute o comando:

```bash
poetry install
```

Esse comando irá instalar todas as dependências listadas no arquivo `pyproject.toml` em um ambiente virtual isolado.

#### 2.2. Criando o arquivo `.env`

O arquivo `.env` contém as variáveis de ambiente necessárias para o funcionamento do projeto. Use o arquivo `example.env` como modelo. Edite o arquivo `.env` com as variáveis adequadas para o seu ambiente de desenvolvimento.

### 3. Rodando o projeto

#### 3.1. Ativando o ambiente virtual do Poetry

Antes de rodar o projeto, ative o ambiente virtual gerenciado pelo Poetry:

```bash
poetry shell
```

#### 3.2. Rodando a aplicação

Execute o arquivo `run.py` para iniciar o servidor da API:

```bash
python run.py
```

A aplicação estará disponível localmente em `http://localhost:8000`.

## Banco de Dados

Você pode inicializar o banco de dados no pgAdmin executando o script SQL fornecido em ``script_database.sql``.

## Estrutura do Projeto

- `app/models.py`: Modelos do banco de dados.
- `app/routes.py`: Definição das rotas da API.
- `app/utils.py`: Funções utilitárias para a API.
- `config.py`: Configurações globais da aplicação.
- `run.py`: Arquivo principal para executar a aplicação.
  