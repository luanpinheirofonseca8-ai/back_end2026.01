livros = []
disponiveis = []
emprestimos = []

def mensagem(msg):
    print(msg)

def cadastrar_livro(titulo, autor):
    livros.append(titulo)
    disponiveis.append(True)
    mensagem("Livro cadastrado com sucesso")
def mostrar_livros():
    for i in range(len(livros)):
        status = "Disponível" if disponiveis[i] else "Indisponível"
        mensagem(f"{i} - {livros[i]} - {status}")
def emprestar_livro(indice):
    if disponiveis[indice]:
        disponiveis[indice] = False
        emprestimos.append(livros[indice])
        mensagem("Livro emprestado com sucesso")
    else:
        return "Livro indisponível para empréstimo"
def devolver_livro(indice):
    if not disponiveis[indice]:
        disponiveis[indice] = True
        emprestimos.remove(livros[indice])
        return "Livro devolvido com sucesso"
    else:
        return "Livro já está disponível"
def menu():
    print("\n==== Biblioteca ====")
    print("1 - Cadastrar Livro\n2 - Mostrar Livros\n3 - Emprestar Livro\n4 - Devolver Livro\n5 - Sair ")
def main():
    while True:
        menu()
        opcao = int(input("Escolha a opção pelo numero: "))
        if opcao == 1:
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            cadastrar_livro(titulo, autor)
        elif opcao == 2:
            print("\n==== Livros Disponíveis ====")
            mostrar_livros()
        elif opcao == 3:
            mostrar_livros()
            escolha = int(input("Escolha o livro pelo numero: "))
            print(emprestar_livro(escolha))
        elif opcao == 4:
            mostrar_livros()
            escolha = int(input("Escolha o livro pelo numero: "))
            print(devolver_livro(escolha))
        elif opcao == 5:
            print("Saindo...")
            break
        else :
            print("Opção invalida!")
main()
            