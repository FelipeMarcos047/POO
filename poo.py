class Estudantes:

    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

def media(self):
    return (self.nota1 + self.nota2) / 2

def situacao(self):
    media = self.media()
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"

def descrever(self):
    return (f"{self.nome:16} {self.nota1:<7.2f} {self.nota2:<7.2f} {self.media():<8.2f} {self.situacao():<14}")

estudante = []

def cadastrar():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Nota 1 : "))
    nota2 = float(input("Nota 2 : "))

    novo_estudante = Estudantes(nome, nota1, nota2)
    estudante.append(novo_estudante)

    print ("Aluno cadastrado com sucesso!")

def listar():
    if len (estudante) == 0:  #retorna o tamanho da lista array
        print("Nenhum aluno cadastrado.")
        return

    print(f"\n{'NOME':16} {'N1':<7} {'N2':<7} {'MÉDIA':<8} {'SITUAÇÃO':<14}")

    for estudante in estudante:
        print(estudante.descrever())

    def menu():
        while True:
            print("\nMenu:")
            print("1. Cadastrar aluno")
            print("2. Listar alunos")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar()
            elif opcao == "2":
                listar()
            elif opcao == "3":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")