import pygame
pygame.init()

# --- Configuración ---
ANCHO, ALTO = 1000, 1000
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación Direccional - Sprite Sheet")

# --- Cargar Sprite Sheet ---
sprite_sheet = pygame.image.load("personaje_direcciones.png").convert_alpha()

FRAME_ANCHO = 200
FRAME_ALTO = 300

COLUMNAS = 4
FILAS = 4

SPRITE_ESCALA = 2
DISPLAY_ANCHO = FRAME_ANCHO * SPRITE_ESCALA 
DISPLAY_ALTO = FRAME_ALTO * SPRITE_ESCALA

# --- Función para extraer los cuadros de una fila ---
def obtener_frames(fila):
    frames = []
    for i in range(COLUMNAS):
        rect = pygame.Rect(i * FRAME_ANCHO, fila * FRAME_ALTO, FRAME_ANCHO, FRAME_ALTO)
        frame = sprite_sheet.subsurface(rect)

        frame_escalado = pygame.transform.scale(frame, (DISPLAY_ANCHO, DISPLAY_ALTO))
        frames.append(frame_escalado)
    return frames

# --- Diccionario con las animaciones de cada dirección ---
animaciones = {
    "arriba_walk": obtener_frames(3),
    "izquierda_walk": obtener_frames(2),
    "abajo_walk": obtener_frames(0),
    "derecha_walk": obtener_frames(1)
}

# creamos las animaciones de "idle" usando solo el primer frame de cada direcion.
animaciones ["arriba_idle"] = [animaciones["arriba_walk"][0]]
animaciones ["izquierda_idle"] = [animaciones["izquierda_walk"][0]]
animaciones ["abajo_idle"] = [animaciones["abajo_walk"][0]]
animaciones ["derecha_idle"] = [animaciones["derecha_walk"][0]]

#--- poner fondo ---
try:
    fondo = pygame.image.load("fondo.png").convert()
    # escalamos para que oincida con el tamaño de la ventana
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
except pygame.error as e:
    print(f"Error cargando el fondo: {e}. usando color plano en su lugar.")
    fondo = None

# --- Variables de juego ---
x, y = ANCHO // 2, ALTO // 2
velocidad = 3
estado = "abajo_idle"
frame_index = 0
ultimo_tiempo = pygame.time.get_ticks()
tiempo_animacion = 150  # milisegundos entre cuadros
reloj = pygame.time.Clock()

# --- ataque ---
atacando = False
tiempo_inicio_ataque = 0
DURACION_ATAQUE = 400

# --- Bucle principal ---
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

        # detecion de tecla para atacar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not atacando:
                atacando = True
                tiempo_inicio_ataque = pygame.time.get_ticks()
                frame_index = 0 #reinicio de frames

    # logica para gestionar el estado de ataque
    if atacando:
        ahora = pygame.time.get_ticks()

        if ahora - tiempo_inicio_ataque > DURACION_ATAQUE:
            atacando = False
            dir_base = estado.split('_')[0]
            estado = dir_base + "_idle"
            frame_index = 0
        else:
            dir_base = estado.split('_')[0]

            estado = dir_base + "_walk"
            frame_index = len(animaciones[estado]) - 1
            

        # --- Movimiento y dirección ---
    if not atacando:
        teclas = pygame.key.get_pressed()
        moviendo = False

        # Extraer solo la direcion de la variable estado actual (ej: "abajo" idica ir abajo)
        # Si el estado es "abajo_idle", dir_base sera "abajo"
        dir_base = estado.split('_')[0]
        nueva_dir_base = dir_base # usaremos esta para saber si cambiamos de direccion

        if teclas[pygame.K_UP]:
            y -= velocidad
            nueva_dir_base = "arriba"
            moviendo = True
        elif teclas[pygame.K_DOWN]:
            y += velocidad
            nueva_dir_base = "abajo"
            moviendo = True
        elif teclas[pygame.K_LEFT]:
            x -= velocidad
            nueva_dir_base = "izquierda"
            moviendo = True
        elif teclas[pygame.K_RIGHT]:
            x += velocidad
            nueva_dir_base = "derecha"
            moviendo = True

    

        # --- Añadir límites de pantalla (PUNTO 3) ---
        # Límite horizontal (eje X)
        if x < 0:
            x = 0
        # Usamos DISPLAY_ANCHO (64) para que el borde derecho del sprite toque el límite de la ventana
        elif x > ANCHO - DISPLAY_ANCHO:
            x = ANCHO - DISPLAY_ANCHO
                
            # Límite vertical (eje Y)
        if y < 0:
            y = 0
        
    
        # Usamos DISPLAY_ALTO (64) para que el borde inferior del sprite toque el límite de la ventana
        elif y > ALTO - DISPLAY_ALTO:
            y = ALTO - DISPLAY_ALTO

        # 1. definir el nuevo estado (walk o idle)
        if moviendo:
            nuevo_estado = nueva_dir_base + "_walk"
        else:
            nuevo_estado = nueva_dir_base + "_idle"

        # 2. Transición de estado: si el estado cambia (ej: de idle a walk), reiniciamos el frame
        if nuevo_estado != estado:
            estado = nuevo_estado
            frame_index = 0 #Reiniciar animacion al cambiar de estado
            ultimo_tiempo = pygame.time.get_ticks() #reiniciar el tiempo para empezar la nueva animacion

    # --- actualizar animacion ( solo si es una animacion de walk) ---
    ahora = pygame.time.get_ticks()

    # solo animamos (cambiamos de feame) si el personaje esta en el modo "walk"
    if 'walk' in estado:
        if ahora - ultimo_tiempo > tiempo_animacion:
            # frame_index +1 y % len() asegura que la animacion se repita en
            frame_index = (frame_index + 1) % len(animaciones [estado])
            ultimo_tiempo = ahora
    

    # --- Dibujar ---
    if fondo:
        VENTANA.blit(fondo, (0, 0))
    else:
        VENTANA.fill((90, 150, 255))
    VENTANA.blit(animaciones[estado][frame_index], (x, y))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
