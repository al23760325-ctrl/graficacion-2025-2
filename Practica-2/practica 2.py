import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 2 - Saltos")

x, y = 300, 300
vel_y = 0
gravedad = 1

SALTO_FUERZA = -18 # cambia el valor para modificar la fuerza del salto
salto_disponible = 2 # Doble salto (2 saltos permitidos)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #  saltar solo si aun queda saltos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and salto_disponible > 0:
                vel_y = SALTO_FUERZA
                salto_disponible -= 1

    #  aplicar movimiento y gravedad
    y += vel_y
    vel_y += gravedad

    # detectar suelo
    suelo_y = 300
    if y >= suelo_y:
        y = suelo_y
        vel_y = 0
        saltos_disponibles = 2 # se reinicia los saltos al tocar el suelo

    pantalla.fill((50, 50, 100))
    pygame.draw.rect(pantalla, (255, 255, 0), (x, y, 40, 40))
    pygame.display.update()

pygame.quit()
