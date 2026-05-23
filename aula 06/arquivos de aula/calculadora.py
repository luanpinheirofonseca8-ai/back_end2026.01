class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero_um = numero1
        self.numero_dois = numero2



    def somar(self):
        resultado = self.numero_um + self.numero_dois
        return resultado




    def subtrair(self):
        resultado = self.numero_um - self.numero_dois
        return resultado




    def multiplicar(self):
        resultado = self.numero_um * self.numero_dois
        return resultado





    def dividir(self):
        if self.numero_dois == 0:
            mensagem = "Não é possível dividir por zero."
            return mensagem
        else:
            resultado = self.numero_um / self.numero_dois
            return resultado




print("Calculadora Simples\n")
valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

calculadora_on = Calculadora(valor1, valor2)

print(f"O resultado da soma é: {calculadora_on.somar()}")
print(f"O resultado da subtração é: {calculadora_on.subtrair()}")
print(f"O resultado da multiplicação é: {calculadora_on.multiplicar()}")
print(f"O resultado da divisão é: {calculadora_on.dividir()}")
