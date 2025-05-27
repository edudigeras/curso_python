import json
import os

db_veiculos = "db_veiculos.json"

def carregar_dados():
    if os.path.exists(db_veiculos):
        with open(db_veiculos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados_veiculo():
    marca_veiculo = input("Informe a Marca do Veículo: ")
    modelo_veiculo = input("Informe o Modelo do Veículo: ")
    ano_veiculo = input("Informe o Ano de Fabricação do Veículo: ")
    cor_veiculo = input("Informe a Cor do Veículo: ")

    veiculo = {
        "marca": marca_veiculo,
        "modelo": modelo_veiculo,
        "ano": ano_veiculo,
        "cor": cor_veiculo
    }

    return veiculo

def cadastrar_veiculo(dados_veiculo):
    veiculos = carregar_dados()
    veiculos.append(dados_veiculo)

    with open(db_veiculos, "w", encoding="utf-8") as arq_json:
        json.dump(veiculos, arq_json, indent=4, ensure_ascii=False)

def mostrar_dados_veiculos(veiculos):
    if not veiculos:
        print("Nenhum veículo cadastrado no momento.")
    else:
        for veiculo in veiculos:
            print(f"""
            Marca do Veículo: {veiculo["marca"]}
            Modelo do Veículo: {veiculo["modelo"]}
            Ano de Fabricação do Veículo: {veiculo["ano"]}
            Cor do Veículo: {veiculo["cor"]}
            """)

def iniciar_sistema():
    veiculos = carregar_dados()
    while True:
        print("")
        print("=" * 80)
        print("Opção 1 - Mostrar Lista de Veículos")
        print("Opção 2 - Cadastrar Veículo")
        print("Opção 3 - Sair do Sistema")
        print("=" * 80)
