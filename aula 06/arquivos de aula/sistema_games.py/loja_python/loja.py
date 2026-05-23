from jogo import Jogo



class Loja:
    def __init__(self):
        self.cadastro = []

    def cadastrar_jogo(self):
        print("\n--- Cadastro de Jogo ---")
        nome = input("Nome do jogo: ")
        genero = input("Gênero do jogo: ")
        preco = input("Preço do jogo: ")
        meu_jogo = Jogo(nome, genero, preco)
        # Adiciona o jogo na lista da Loja
        self.cadastro.append(meu_jogo)
        print(f"{nome} cadastrado com sucesso!\n")
    def mostrar_jogos(self):
        for jogo in self.cadastro:
            jogo.desc_jogo()
            print("-" * 20)
    def main(self):
        while True:
            print("Bem-vindo à Loja de Jogos Python!\n")
            print("1 - Cadastrar jogo")
            print("2 - Mostrar jogos cadastrados")
            print("3 - Sair\n")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                self.cadastrar_jogo()
            elif opcao == 2:
                self.mostrar_jogos()
            elif opcao == 3:
                print("Obrigado por usar a Loja de Jogos! Até mais!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.\n")        
sistema = Loja()
sistema.main()                