import pygame, random
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 4 - Colisiones")

jugador = pygame.Rect(50, 300, 40, 40)
balas = []
enemigos = [pygame.Rect(500, 300, 40, 40)]

puntos = 0
fuente = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()
running = True


while running:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(jugador.x + 40, jugador.y + 15, 10, 5))

    for b in balas:
        b.x += 10
        
    balas = [b for b in balas if b.x < 600]

    for b in balas[:]:
        for e in enemigos[:]:
            
            if b.colliderect(e):
                balas.remove(b)
                enemigos.remove(e)

                puntos += 1

                enemigos.append(pygame.Rect(
                    500,
                    random.randint(0, 360),
                    40,
                    40
                ))

    pantalla.fill((0, 0, 0))
    
    pygame.draw.rect(pantalla, (0, 255, 0), jugador)
    
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b)
        
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e)

    texto = fuente.render(f"Puntos: {puntos}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))
    
    pygame.display.update()

pygame.quit()
