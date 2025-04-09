import pygame
import random
import sys

# Inicialización de pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 1360, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evil Liam Remake Unreal Engine 4")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Constantes del juego
FPS = 60
PLAYER_SPEED = 7
BULLET_SPEED = 10
ENEMY_SPEED = 3
ENEMY_SIZE = 100
PLAYER_SIZE = 100
ENEMY_BULLET_SPEED = 6
ENEMY_SHOOT_PROBABILITY = 80
BASE_ENEMY_COUNT = 7
VICTORY_SCORE = 600

# Fuente
font = pygame.font.SysFont("Arial", 30)

# Cargar imágenes
try:
    player_img = pygame.image.load("player.png")
    player_img = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
    
    enemy_img = pygame.image.load("enemy.png")
    enemy_img = pygame.transform.scale(enemy_img, (ENEMY_SIZE, ENEMY_SIZE))

    background_img = pygame.image.load("background.png")
    
    oppenheimer_img = pygame.image.load("oppenheimer.png")
    oppenheimer_img = pygame.transform.scale(oppenheimer_img, (PLAYER_SIZE, PLAYER_SIZE))
except pygame.error as e:
    print(f"Error cargando imágenes: {e}")
    sys.exit()

# Clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - PLAYER_SIZE - 10)
        self.speed = PLAYER_SPEED

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        return Bullet(self.rect.centerx, self.rect.top)

# Clase del enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, shoot_probability, bullets_group):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.shoot_probability = shoot_probability
        self.bullets_group = bullets_group  

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
        
        # Disparar con cierta probabilidad
        if random.randint(1, self.shoot_probability) == 1:
            self.bullets_group.add(EnemyBullet(self.rect.centerx, self.rect.bottom))

# Clase de las balas del jugador
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Clase de las balas del enemigo
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = ENEMY_BULLET_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

def show_manual():
    """Muestra la pantalla de instrucciones al inicio del juego"""
    screen.fill(BLACK)
    instructions = [
        "EVIL LIAM REMAKE - UNREAL ENGINE 4",
        "",
        "Historia:",
        "El salvador de la BIS, Liam. Fue encerrado en el laboratorio de IOT por 100 años, ",
        "despues de darse cuenta de que fue traicionado por la BIS, se corrompio a base de arduinos, ",
        "por lo que ha secuestrado a nuestro señor y salvador Abiertoheimer para terminar con la BIS",
        "y depende de ti salvarlo.",
        "Derrota a sus versiones malvadas y salva a Abiertoheimer.",
        "",
        "Controles:",
        "Flecha izquierda/derecha - Moverse",
        "Espacio - Disparar",
        "Enter - Empezar juego",
        "Esc - Salir"
    ]
    
    y_offset = 100
    for line in instructions:
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (WIDTH//4, y_offset))
        y_offset += 40
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def show_end_screen(message):
    """Muestra la pantalla de fin de juego (victoria/derrota)"""
    screen.fill(BLACK)
    text = font.render(message, True, WHITE)
    screen.blit(text, (WIDTH // 4, HEIGHT // 3))
    screen.blit(oppenheimer_img, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
    screen.blit(player_img, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True  # Reiniciar juego
                if event.key == pygame.K_ESCAPE:
                    return False  # Salir del juego

def main():
    """Función principal del juego"""
    # Mostrar manual al inicio
    show_manual()
    
    # Inicializar grupos de sprites
    player = Player()
    player_group = pygame.sprite.Group(player)
    bullet_group = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group() 
    enemy_group = pygame.sprite.Group()
    
    # Crear enemigos iniciales 
    for _ in range(BASE_ENEMY_COUNT):
        enemy = Enemy(
            x=random.randint(0, WIDTH - ENEMY_SIZE),
            y=random.randint(-100, -40),
            speed=ENEMY_SPEED,
            shoot_probability=ENEMY_SHOOT_PROBABILITY,
            bullets_group=enemy_bullets  
        )
        enemy_group.add(enemy)
    
    score = 0
    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(FPS)
        
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullet_group.add(player.shoot())
        
        # Actualización del juego
        keys = pygame.key.get_pressed()
        player.update(keys)
        bullet_group.update()
        enemy_group.update() 
        enemy_bullets.update()
        
        # Colisiones balas jugador con enemigos
        for bullet in bullet_group:
            enemies_hit = pygame.sprite.spritecollide(bullet, enemy_group, True)
            for _ in enemies_hit:
                bullet.kill()
                score += 10
                # Añadir nuevo enemigo
                enemy = Enemy(
                    random.randint(0, WIDTH - ENEMY_SIZE),
                    random.randint(-100, -40),
                    ENEMY_SPEED,
                    ENEMY_SHOOT_PROBABILITY,
                    enemy_bullets 
                )
                enemy_group.add(enemy)
        
        # Colisiones jugador con enemigos o balas enemigas
        if (pygame.sprite.spritecollide(player, enemy_group, False) or 
            pygame.sprite.spritecollide(player, enemy_bullets, False)):
            running = False
            if show_end_screen("¡Game Over!"):
                main()  # Reiniciar juego
            else:
                running = False  # Salir del juego
        
        # Verificar victoria
        if score >= VICTORY_SCORE:
            running = False
            if show_end_screen("¡Felicidades, salvaste a Abiertoheimer!"):
                main()  # Reiniciar juego
            else:
                running = False  # Salir del juego
        
        # Dibujado
        screen.blit(background_img, (0, 0))
        player_group.draw(screen)
        enemy_group.draw(screen)
        bullet_group.draw(screen)
        enemy_bullets.draw(screen)  
        
        # Mostrar puntaje
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()