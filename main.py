import requests
from tinydb import TinyDB
from datetime import datetime

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados
  
def transform_dados_bitcoin(dados):
  """Transformar os dados dos json para a colunas no banco de dados"""
  valor = dados ['data']['amount']
  criptomoeda = dados ['data']['base']
  moeda = dados ['data']['currency']
  dados_transformados ={
    'valor': valor,
    'criptomoeda': criptomoeda,
    'moeda': moeda
  }
  return dados_transformados

def salvar_dados_tinydb(dados, db_name="bitcoin.json"):
  db = TinyDB(db_name)
  db.insert(dados)
  print("Dados salvos com sucesso!")
  
  
if __name__ == "__main__":
    # Extração e tratamento dos dados
    dados_json = extrair_dados_bitcoin()
    dados_tratados = transform_dados_bitcoin(dados_json)
    salvar_dados_tinydb(dados_tratados)