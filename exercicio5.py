from exercicio4 import calcular_media

alunos = []

def obter_dados_aluno():
    nome_aluno = input("Informe seu nome completo: ")
    email_aluno = input("Informe o email do aluno: ")
    serie_aluno = input("Informe a serie do aluno: ")
    nota01_aluno = float(input("Informe a primeira nota do aluno: "))
    nota02_aluno = float(input("Informe a segunda nota do aluno: "))
    nota03_aluno = float(input("Informe a terceira nota do aluno: "))

    return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01_aluno, nota02_aluno, nota03_aluno)

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):
    
    notas = [nota01, nota02, nota03]

    aluno = {
            "nome": nome,
            "email": email,
            "serie": serie,
            "notas": notas,
            "media": calcular_media(notas)
}
    alunos.append(aluno)
    
    return aluno



def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"Nome do aluno: {aluno["nome"]} | Email do aluno: {aluno["email"]} | Série do aluno {aluno["serie"]} | Notas do aluno{aluno["notas"]} Média do aluno {aluno["media"]}")

    return 

def iniciar_sistema():
    while True:
        print("="*80)
        print("Opção 1 => Mostrar lista de alunos cadastrados.")
        print("Opção 2 => Cadastrar alunos.")
        print("Opção 3 => Sair do sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções acima: ")

        if opcao == "1":
            mostrar_dados_alunos(alunos)
        elif opcao == "2":
            obter_dados_aluno()
        else:
            print("Sistema finalizado.")
            break

iniciar_sistema()

