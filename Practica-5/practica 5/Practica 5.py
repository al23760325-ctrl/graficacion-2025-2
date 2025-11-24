import pygame, random
pygame.init()

pantalla = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Práctica 5 - Sprites y fondo")

fondo = pygame.image.load("fondo.png")
fondo_x = 0

sprites = [
    pygame.image.load("p1.png"),
    pygame.image.load("p2.png"),
    pygame.image.load("p3.png")
]
indice = 0
x, y = 100, 300

enemigo_img = pygame.image.load("enemigo.png")
enemigos = [pygame.Rect(600, 300, 40, 40)]

balas = []

vel_y = 0
saltando = False

clock = pygame.time.Clock()
running = True
puntos = 0

contador_anim = 0
            
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(x + 40, y + 20, 10, 5))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not saltando:
            vel_y = -12
            saltando = True

    fondo_x -= 2
    if fondo_x <= -600:
        fondo_x = 0

    vel_y += 1
    y += vel_y
    if y >= 300:
        y = 300
        vel_y = 0
        saltando = False

    contador_anim += 1
    if contador_anim >= 5:
        indice = (indice + 1) % len(sprites)
        contador_anim = 0

    for b in balas:
        b.x += 10
    balas = [b for b in balas if b.x < 600]

    for e in enemigos:
        e.x -= 4
    enemigos = [e for e in enemigos if e.x > -50]

    while len(enemigos) < 1:
        enemigos.append(pygame.Rect(600, 300, 40, 40))

    for b in balas [:]:
        for e in enemigos [:]:
            if b.colliderect(e):
                balas.remove(b)
                enemigos.remove(e)
                puntos += 1

    pantalla.blit(fondo, (fondo_x, 0))
    pantalla.blit(fondo, (fondo_x + 600, 0))

    pantalla.blit(sprites[indice], (x,y))

    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b)

    for e in enemigos:
        pantalla.blit(enemigo_img, (e.x, e.y))

    font = pygame.font.SysFont(None, 30)
    texto = font.render(f"Puntos: {puntos}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()
