import json
import os

data = "filmes.json"

def cadastrar_filmes():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_filmes():
    nome_filme = input("Informe o nome do filme: ")
    categoria_filme = input("Informe a categoria do filme: ")
    classficacao_filme = input("Informe a classificação indicativa do filme: ")
    
    filme = {
        "nome_filme": nome_filme,
        "categoria_filme": categoria_filme,
        "classficacao_filme": classficacao_filme
    }

    return filme

def cadastro_filme(dados_filme):
    data.append(dados_filme)

    return data

def mostrar_dados_filmes(dados_filme):
    for filmes in dados_filme:
        print(f"""
              Nome do filme: {filmes["nome_filme"]}
              Categoria do filme: {filmes["categoria_filme"]}
              Classificação do filme: {filmes["classficacao_filme"]}
              """)
        
def iniciar_sistema():
    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar Lista de filmes")
        print("Opção 2 - Cadastrar filmes")
        print("Opção 3 - Sair do Sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao == "1":
            obter_filmes(data)
        elif opcao == "2":
            cadastro_filme(obter_filmes())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção Invalida, escolha uma das opções do menu.")

iniciar_sistema()