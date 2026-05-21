
def preco_ingresso(idade, tipo):
    if tipo == "inteira":
        if idade < 12:
            return 10.0  # Preço para crianças
        elif idade < 60:
            return 20.0  # Preço para adultos
        else:
            return 15.0  # Preço para idosos
def idade_desconto(idade):
    if idade < 12:
        return 0.5  # Desconto de 50% para crianças
    elif idade < 60:
        return 0.0  # Sem desconto para adultos
    elif idade >= 60:
        return 0.25  # Desconto de 25% para idosos
            
    

    else:
        return 0.0

def cadastrar_filme(titulo, genero):
    return f"Filme '{titulo}' do gênero '{genero}' cadastrado com sucesso"

def mostrar_filmes(filmes):
    for i in range(len(filmes)):
        print(f"{i} - {filmes[i]['titulo']} - {filmes[i]['genero']}")
def arrecadacao(filmes, ingressos_vendidos):
    total = 0
    for i in range(len(filmes)):
        total += ingressos_vendidos[i] * preco_ingresso(0, "inteira")  # Supondo que todos os ingressos são inteiros
    return total
def menu():

    idade = int(input("Digite a idade do cliente: "))

    print("\n==== Cinema Do Python ====")
    
    print("1 - Cadastrar Filme\n2 - Mostrar Filmes\n3 - Calcular Arrecadação\n4 - Sair ")
def main():
    filmes = []
    ingressos_vendidos = []
    while True:
        menu()
        opcao = int(input("Escolha a opção pelo numero: "))
        if opcao == 1:
            titulo = input("Título do filme: ")
            genero = input("Gênero do filme: ")
            filmes.append({'titulo': titulo, 'genero': genero})
            print(cadastrar_filme(titulo, genero))
        elif opcao == 2:
            print("\n==== Filmes Cadastrados ====")
            mostrar_filmes(filmes)
        elif opcao == 3:
            for i in range(len(filmes)):
                vendidos = int(input(f"Quantos ingressos foram vendidos para '{filmes[i]['titulo']}'? "))
                ingressos_vendidos.append(vendidos)
            print(f"Arrecadação total: R${arrecadacao(filmes, ingressos_vendidos):.2f}")
        elif opcao == 4:
            print("Saindo...")
            break
        else :
            print("Opção invalida!")
main()                