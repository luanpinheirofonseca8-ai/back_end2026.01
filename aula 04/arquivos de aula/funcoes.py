# "SISTEMA DE CINEMA"
filmes = []
precos_ingresso = []
vendas = []
 
#FUNÇÕES
 
#Função de mensagem
def mensagem(msg):
    print(msg)
 
#Função para cdastrar os filmes
def cadastro_filme():
    nome_filme = input("Nome do Filme: ")
    genero_filme = input("Genero: ")
    autor_filme = input("Autor: ")
    preco_sessao = input("Valor da sessão: ")
 
    #Dicionario (Objeto)
    filme = {
        'nome': nome_filme,
        'genero': genero_filme,
        'autor': autor_filme
    }
 
    filmes.append(filme) #Cadastra o filme na lista Filmes
    precos_ingresso.append(preco_sessao) #Cadastra o valor do ingresso na lista precos_ingresso
    return mensagem("Filme cadastrado com sucesso!")
 
#Mostrar Filme
def mostrar_filme():
    mensagem("\n ===== FILMES =====")
    for i in range(len(filmes)):
        return mensagem(f" {i} - {filmes[i]} - R${precos_ingresso[i]}")
 
#Função vender ingresso
def vender_ingressos(filme):
    vendas.append[precos_ingresso[filme]]
    return mensagem("Ingresso vendido com sucesso!")
 
#Função calcula total de vendas
def calcula_total():
    return sum(vendas)
 
#Fnção calcula a quantidade de vendas
def total_ingressos():
    return len(vendas)
 
def menu():
    mensagem("\n ==== CINEMA =====")
    mensagem("1 - Cadastrar Filme")
    mensagem("2 - Mostrar Filme")
    mensagem("3 - Comprar Ingresso")
    mensagem("4 - Mostrar arrecadação")
    mensagem("5 - Total de ingressos")
    mensagem("6 - Sair")
 
#Funçõa main
 
def main():
    #Exibir o menu
    while True:
        menu()
 
        opcao = int(input("Esscolha uma opção [1] [2] [3] [4] [5] [6]: "))
 
        if opcao == 1:
            cadastro_filme()
        elif opcao == 2:
            mostrar_filme()
        elif opcao == 3:
            mostrar_filme()
            escolha = int(input("Escolha o numero do Filme: "))
            vender_ingressos(escolha)
        elif opcao == 4:
            mensagem(f" Arrecadação: R${calcula_total()}")
        elif opcao == 5:
            mensagem(f"Ingressos vendidos: {total_ingressos()}")
        elif opcao == 6:
            mensagem("Saindo...")
            break
        else:
            mensagem("Opção invalida!")
 
main()