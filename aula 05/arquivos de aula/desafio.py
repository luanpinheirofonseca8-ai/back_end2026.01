""" class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
prod = Produto("Camiseta", 50.0)
print(f"Produto: {prod.nome}, Preço: R${prod.preco:.2f}")
class Livro:
    def __init__(self,nome_livro,preco_livro):
        self.nome = nome_livro
        self.preco = preco_livro
livro = Livro("Dom Casmurro", 45.0)
print(f"Livro: {livro.nome}, Preço: R${livro.preco:.2f}")
class Filme:
    def __init__(self,nome_filme,preco_filme,categoria_filme):
        self.nome = nome_filme
        self.preco = preco_filme
        self.categoria = categoria_filme
filme = Filme("Vingadores", 30.0, "Ação")
print(f"Filme: {filme.nome}, Preço: R${filme.preco:.2f}, Categoria: {filme.categoria}")
 """



class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        

    def saldo_atual(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
    


    def realizar_deposito(self):
        info_deposito =  int(input("Digite o valor do depósito: "))
        if info_deposito > 0:
            print(f"Depósito de R${info_deposito:.2f} realizado com sucesso.")    
        else:
            info_deposito == 0
            print("Valor de depósito inválido.")
        self.saldo += info_deposito
conta = ContaBancaria()
conta.saldo_atual()
conta.realizar_deposito()
conta.saldo_atual()
