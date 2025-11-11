import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 1 - Movimiento básico")

x, y = 300, 200
vel = 50
clock = pygame.time.Clock()
running = True
# el personaje cambia de color (en este caso naranja)
color_personaje = (255, 100, 0) 

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    teclas = pygame.key.get_pressed()

    # cambiar velocidad
    if teclas [pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]:
        velocidad_actual = vel * 2
    else:
        velocidad_actual = vel
    

    if teclas[pygame.K_LEFT]:
        x -= velocidad_actual
    if teclas[pygame.K_RIGHT]:
        x += velocidad_actual
    if teclas[pygame.K_UP]:
        y -= velocidad_actual
    if teclas[pygame.K_DOWN]:
        y += velocidad_actual

    # evitar que el personaje salga de la pantalla
    if x < 0:
        x = 0
    if x > 600 - 40:
        x = 600 - 40
    if y < 0:
        y = 0
    if y > 400 - 40:
        y = 400 - 40
 
    pantalla.fill((30, 30, 30))
    pygame.draw.rect(pantalla, color_personaje, (x, y, 40, 40))
    pygame.display.update()

pygame.quit()
