import pygame
pygame.init()

# --- Configuración ---
ANCHO, ALTO = 640, 480
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación Direccional - Sprite Sheet")

# --- Cargar Sprite Sheet ---
sprite_sheet = pygame.image.load("personaje_direcciones.png").convert_alpha()

FRAME_ANCHO = 64
FRAME_ALTO = 64
FILAS = 4       # Una fila por dirección
COLUMNAS = 4    # Cuatro fotogramas por fila

# --- Función para extraer los cuadros de una fila ---
def obtener_frames(fila):
    frames = []
    for i in range(COLUMNAS):
        rect = pygame.Rect(i * FRAME_ANCHO, fila * FRAME_ALTO, FRAME_ANCHO, FRAME_ALTO)
        frame = sprite_sheet.subsurface(rect)
        frames.append(frame)
    return frames

# --- Diccionario con las animaciones de cada dirección ---
animaciones = {
    "arriba": obtener_frames(0),
    "izquierda": obtener_frames(1),
    "abajo": obtener_frames(2),
    "derecha": obtener_frames(3)
}

# --- Variables de juego ---
x, y = ANCHO // 2, ALTO // 2
velocidad = 3
direccion = "abajo"
frame_index = 0
ultimo_tiempo = pygame.time.get_ticks()
tiempo_animacion = 150  # milisegundos entre cuadros
reloj = pygame.time.Clock()

# --- Bucle principal ---
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # --- Movimiento y dirección ---
    teclas = pygame.key.get_pressed()
    moviendo = False

    if teclas[pygame.K_UP]:
        y -= velocidad
        direccion = "arriba"
        moviendo = True
    elif teclas[pygame.K_DOWN]:
        y += velocidad
        direccion = "abajo"
        moviendo = True
    elif teclas[pygame.K_LEFT]:
        x -= velocidad
        direccion = "izquierda"
        moviendo = True
    elif teclas[pygame.K_RIGHT]:
        x += velocidad
        direccion = "derecha"
        moviendo = True

    # --- Actualizar animación ---
    ahora = pygame.time.get_ticks()
    if moviendo:
        if ahora - ultimo_tiempo > tiempo_animacion:
            frame_index = (frame_index + 1) % len(animaciones[direccion])
            ultimo_tiempo = ahora
    else:
        frame_index = 0  # quieto muestra primer frame

    # --- Dibujar ---
    VENTANA.fill((90, 150, 255))
    VENTANA.blit(animaciones[direccion][frame_index], (x, y))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
