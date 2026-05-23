class Jogo:
    def __init__(self, nome, genero, preco):
        self.nome = nome
        self.genero = genero
        self.preco = preco

    def desc_jogo(self):
        print(f"Nome: {self.nome}")
        print(f"Gênero: {self.genero}")
        print(f"preco: {self.preco}")