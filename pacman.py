import pygame

amarelo =(255,255,0)
preto=(0,0,0)
velocidade = 0.50

pygame.init()

tela = pygame.display.set_mode((640, 480),0)
x = 10
y = 10
vel_x = velocidade
vel_y= velocidade

while True:

    # Cacula as regras
    x = x + vel_x
    y = y + vel_y
    raio = 30
   
    if x  + raio> 640:
           vel_x = - velocidade
    if x - raio < 0:
            vel_x = velocidade
    if x + raio > 480:
            vel_y = - velocidade
    if x - raio < 0:
            vel_y = velocidade

    # Pinta
    tela.fill((preto))
    pygame.draw.circle(tela, amarelo,(int(x),(int(y))), 30, 0)
    pygame.display.update()
    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
