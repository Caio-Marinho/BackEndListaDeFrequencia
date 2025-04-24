# Importações padrão
import os
from datetime import datetime, date, time
import pytz

# Bibliotecas de terceiros
from dotenv import load_dotenv  # Carrega variáveis de ambiente do arquivo .env
from flask import Flask, Response, jsonify,request,Blueprint  # Framework web e tipos de resposta HTTP
from flask_cors import CORS  # Middleware para habilitar CORS (Cross-Origin Resource Sharing)
from flask_migrate import Migrate, init, migrate, upgrade  # Gerenciamento de migrações com Flask-Migrate

# Componentes da aplicação (internos)
from .util import *  # Funções utilitárias
from .configuration import *  # Classe de configuração da aplicação
from .routes import *  # Blueprint com as rotas da aplicação



# Lista de exportações explícitas
# Define quais objetos serão visíveis ao importar tudo com: from app.globals import *
__all__ = [
    'Blueprint',                          # Classe para criar blueprints
    'Configuration',                     # Classe de configuração da aplicação
    'CORS',                              # Middleware CORS
    'Flask',                             # Classe principal da aplicação Flask
    'HttpstatusCode',                    # Enum para status HTTP
    'Migrate',                           # Componente de migração
    'Response',                          # Tipo de resposta HTTP
    'configure_app_logging',             # Função para configurar logging
    'date',                              # Objeto de data
    'datetime',                          # Objeto de data/hora
    'gerar_env_automatico',              # Função que gera ou atualiza o .env automaticamente
    'init',                              # Comando para iniciar migrações
    'jsonify',                           # Função Flask para criar respostas JSON
    'load_dotenv',                       # Função para carregar variáveis de ambiente
    'migrate',                           # Comando para gerar migrações
    'os',                                # Biblioteca para interações com o sistema operacional
    'pytz',                              # Biblioteca para trabalhar com fuso horário
    'padronizarEmail',                   # Função utilitária para padronizar e-mails
    'padronizarNome',                    # Função utilitária para padronizar nomes
    'request',                           # Objeto de requisição HTTP
    'routes',                            # Blueprint das rotas
    'time',                              # Objeto de hora
    'upgrade'                            # Comando para aplicar migrações
]
