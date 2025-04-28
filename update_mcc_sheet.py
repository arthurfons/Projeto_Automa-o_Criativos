import os
import re
import time
from datetime import datetime
import pandas as pd
import requests
import pymysql
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from tqdm import tqdm
import difflib

# ------------------------ CONFIGURAÇÕES ------------------------
PASTA_OUTPUT = "output"
TEMPLATES_DIR = "templates"
LOGOS_DIR = "logos"
DIMENSOES = (336, 280)      # Dimensões compatíveis com Google Ads
LOGO_SIZE = (45, 14)        # Tamanho da logo
DEFAULT_CRIATIVOS_QUANTIDADE = 3  # Quantidade padrão para geração de criativos

# Configurações da planilha
SHEET_ID = ""  # Adicione o ID da sua planilha aqui
SHEET_RANGE = "Página1!A:F"  # Intervalo definido para as 6 colunas

# ------------------------ CONFIGURAÇÕES DO WEBHOOK ------------------------
WEBHOOK_URL = ""  # Adicione a URL do seu webhook do Discord aqui

# Arquivo de log para contas com erros de acesso
ERROR_LOG_FILE = "erro_de_acesso_contas.txt"

# ------------------------ FUNÇÕES DE CONTAS BLOQUEADAS ------------------------
BLOCKED_ACCOUNTS_FILE = "blocked_accounts.txt"

def load_blocked_accounts():
    """Carrega as contas bloqueadas do arquivo."""
    if not os.path.exists(BLOCKED_ACCOUNTS_FILE):
        return set()
    with open(BLOCKED_ACCOUNTS_FILE, "r") as f:
        accounts = {line.strip().split(",")[0] for line in f if line.strip()}
    return accounts

def add_blocked_account(account_id, reason):
    """Adiciona uma conta à lista de bloqueados."""
    with open(BLOCKED_ACCOUNTS_FILE, "a") as f:
        f.write(f"{account_id},{reason}\n")

def send_webhook(account_id, reason, message=""):
    """Envia notificação para o webhook do Discord."""
    payload = {
        "content": f"Conta {account_id} bloqueada: {reason}\n{message}"
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Erro ao enviar webhook: {e}")

def extrair_pais(nome_campanha):
    """Extrai o país do nome da campanha."""
    # Implementação da extração de país
    pass

def extrair_site(nome_conta):
    """Extrai o site do nome da conta."""
    # Implementação da extração de site
    pass

def parar_antes_de_1630():
    """Verifica se é antes das 16:30 para parar a execução."""
    hora_atual = datetime.now().time()
    hora_limite = datetime.strptime("16:30", "%H:%M").time()
    return hora_atual < hora_limite

def limpar_planilha():
    """Limpa a planilha mantendo apenas o cabeçalho."""
    service = get_sheets_service()
    service.spreadsheets().values().clear(
        spreadsheetId=SHEET_ID,
        range=SHEET_RANGE
    ).execute()

def ler_planilha():
    """Lê a planilha do Google Sheets."""
    service = get_sheets_service()
    result = service.spreadsheets().values().get(
        spreadsheetId=SHEET_ID,
        range=SHEET_RANGE
    ).execute()
    values = result.get('values', [])
    if not values:
        return pd.DataFrame(columns=["Site", "ID da Conta", "Nome da Conta", "ID do Grupo de Anúncios", "Campanha", "País"])
    return pd.DataFrame(values[1:], columns=values[0])

def atualizar_planilha(df):
    """Atualiza a planilha com os dados do DataFrame."""
    service = get_sheets_service()
    values = [df.columns.tolist()] + df.values.tolist()
    service.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range=SHEET_RANGE,
        valueInputOption="RAW",
        body={"values": values}
    ).execute()

def obter_ids_contas_db():
    """Obtém os IDs das contas do banco de dados."""
    # Implementação da obtenção de IDs
    pass

def obter_dados_de_contas(client):
    """Obtém dados das contas do Google Ads."""
    # Implementação da obtenção de dados
    pass

def get_data_from_child_account(client, customer_id):
    """Obtém dados de uma conta filha específica."""
    # Implementação da obtenção de dados da conta filha
    pass

def atualizar_planilha_com_dados():
    """Atualiza a planilha com dados das contas."""
    # Implementação da atualização
    pass

if __name__ == "__main__":
    atualizar_planilha_com_dados() 