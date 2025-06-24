def cadastrar_filmes(nome_filme, descricao, classificacao, categoria1, categoria2, categoria3):
    dados_filme = []
    filme = {
        "nome_filme": nome_filme,
        "descricao": descricao,
        "classificacao": classificacao,
        "categorias": [categoria1, categoria2, categoria3]
    }
    dados_filme.append(filme)
    return dados_filme

print(cadastrar_filmes("Interestelar", "Descrição", "10", "Ficção cientifica", "Ação", "Aventura"))
