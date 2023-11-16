import random

class RoboLimpeza:
    def __init__(self):
        self.energia = 100
        self.bolsa = 0
        self.posicao = [0, 0]

        # Inicializar a matriz 4x4 com campos sujos aleatórios
        self.matriz = [[random.choice([0, 1]) for _ in range(4)] for _ in range(4)]

    def limpar_campo(self, linha, coluna):
        if self.matriz[linha][coluna] == 1:  # Campo sujo
            self.matriz[linha][coluna] = 0  # Limpar o campo
            self.bolsa += 1
            self.energia -= 1

    def limpar_ambiente(self):
        while self.bolsa < 10:
            self.limpar_campo(self.posicao[0], self.posicao[1])
            self.mostrar_estado()
            self.mover(random.choice(['cima', 'baixo', 'esquerda', 'direita']))

        # Retornar ao ponto inicial
        while self.posicao != [0, 0]:
            self.mover('cima' if self.posicao[0] > 0 else 'esquerda')
            self.mostrar_estado()

        print("Limpeza concluída!")

    def mostrar_estado(self):
        print(f"Posição: {self.posicao}, Energia: {self.energia}, Bolsa: {self.bolsa}")
        print("Matriz:")
        for linha in self.matriz:
            print(linha)
        print("\n")
