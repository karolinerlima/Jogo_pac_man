import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600),0)

amarelo = (255,255,0)
preto = (0,0,0)

class Pacman:
    def __init__(self) :
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 50
        self.raio = self.tamanho // 2


# Desenhar o corpo do Pacman
    def pintar(self, tela):
        pygame.draw.circle(tela,amarelo(self.centro_x, self.centro_y, self.raio),0)

        # Desenho da Boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior= (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_inferior, labio_superior]

        pygame.draw.polygon(tela,preto,pontos,0)

        # Desenho do olho
        olho_x = int(self.centro_x + self.raio /2)
        olho_y = int(self.centro_y - self.raio /2)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela,preto,(olho_x,olho_y),olho_raio,0)


if __name__ == "main":
    pacman = Pacman()

    while True:
        # Pintar a tela
        pacman.pintar(screen)
        pygame.display.update()


        for e in pygame.event.get():
              if e.type==pygame.QUIT:
                exit()
