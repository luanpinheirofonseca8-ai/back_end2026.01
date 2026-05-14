""" def atendimento():
    print("bem-vindo ao sistema")


def saudacao():
    print("bom dia")
       

def menu():
    print("1 - café")
    print("2 - leite")
    print("3 - chocolate")

def linha():
    print("__________________________")


atendimento()
saudacao()
menu()
linha()

def cumprimento():
    print("ola joao")
cumprimento()
nome= input("digite seu nome: ")
def msg():
    print(f"ola {nome}")

 """


""" def idade(idade):
    print(f"sua idade é {idade}")
def cidade(cidade):
    print(f"sua cidade é {cidade}")
def produto(nome_produto):
    print(f"o produto é {nome_produto}")

idade("22")
cidade("sao paulo")
produto("cafe") """




""" nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
def hi(nome, idade):
    print(f"ola {nome}, voce tem {idade} anos")
hi() """


""" def ano(ano):
    print(f" voce tem  {2026 - ano} anos")
nascimento = int(input("digite seu ano de nascimento: "))
ano(nascimento)  """   


""" def cadastro(produto):
    print(f"O produto {produto} foi cadastrado com sucesso")
 
def venda(produto):
    print(f"Produto vendido! {produto}")
 
 
cadastro("Anel")
venda("Aliança")

""" """ Criar a função """
""" def mostrar_calculo(valor_um,valor_dois):
    resultado = valor_um + valor_dois
    print(f"O resultado da operção é {resultado}")
 
 
mostrar_calculo(20,10) """


def media(nota_um, nota_dois):
    return (nota_um + nota_dois) / 2
resultado = media(7, 8)
print(media(7, 8))

def multi(valor_um, valor_dois):
    return valor_um * valor_dois
re_multi = multi(10, 5)
print(re_multi)

#Cria uma função que de 10%
def desconto_10(valor_compra):
    #Calcula qunto é 10% do valor da compra
    desconto = valor_compra * 0.10
    return valor_compra - desconto
 
valor = int(input("Informe o valor da compra: "))
print("Aplicando cupom de 10%. Aguarde.. ")
valor_desconto = desconto_10(valor)
 
print(f"Desconto aplicado! Valor a pagar R${valor_desconto:.2f}")



