class Animal:
    def __init__(self,nome_animal, idade_animal, raca_animal, tipo_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        self.raca = raca_animal
        self.tipo = tipo_animal
    def desc_animal(self):
        print(f'O animal {self.nome},\na idade é {self.idade},\nraça:{self.raca},\ntipo:{self.tipo}')