import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")

sonido_disparo = pygame.mixer.Sound("disparo.mp3")

x, y = 50, 300
vel_bala = 12
balas = []
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            
             # bala hacia la derecha
            if event.key == pygame.K_SPACE:
                balas.append ({ "rect": pygame.Rect(x + 40, y + 15, 10, 5),
                                "dx": vel_bala, "dy": 0})
                sonido_disparo.play()

            # bala hacia la ariba
            if event.key == pygame.K_UP:
                balas.append ({ "rect": pygame.Rect(x + 15, y, 10, 10),
                                "dx": 0, "dy": -vel_bala})
                sonido_disparo.play()

            # bala hacia la abajo
            if event.key == pygame.K_DOWN:
                balas.append ({ "rect": pygame.Rect(x + 15, y + 40, 10, 10),
                                "dx": 0, "dy": vel_bala})
                sonido_disparo.play()

            # bala hacia la izquierda
            if event.key == pygame.K_LEFT:
                balas.append ({ "rect": pygame.Rect(x, y + 15, 10, 5),
                                "dx": -vel_bala, "dy": 0})
                sonido_disparo.play()
                              

    for bala in balas:
        bala["rect"].x += bala["dx"]
        bala["rect"].y += bala["dy"]

    balas = [b for b in balas if 0 <= b["rect"].x <=600 and 0 <= b["rect"].y <=400]

    pantalla.fill((20, 20, 20))
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))
    for b in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), b["rect"])
    pygame.display.update()

pygame.quit()
