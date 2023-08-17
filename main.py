import pygame
import sys
import time

# Инициализация Pygame
pygame.init()

# Размер окна
screen_width = 800
screen_height = 600

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя Игра")

# Загрузка начальной заставки
background_image = pygame.image.load("background.jpg")  # Замените на путь к вашей картинке

# Загрузка игровой сцены (Пример: пустое поле)
game_scene_image = pygame.image.load("tmp.png")  # Замените на путь к вашей игровой сцене
game_scene_rect = game_scene_image.get_rect()
game_scene_rect.center = (screen_width // 2, screen_height // 2)

# Загрузка изображения игрока
player_image = pygame.image.load("player (2).png")  # Замените на путь к изображению игрока
player_rect = player_image.get_rect()
player_rect.center = (screen_width // 2, screen_height // 2)  # Начальное положение игрока

# Определение координат для отображения картинки по центру
background_rect = background_image.get_rect()
background_rect.center = (screen_width // 2, screen_height // 2)

# Инициализация музыки
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")  # Замените на путь к вашему музыкальному файлу
pygame.mixer.music.play(-1)  # Начать воспроизведение бесконечно

# Основной цикл игры
in_menu = True
game_started = False
start_time = time.time()

while in_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_menu = False

    if time.time() - start_time >= 5:
        in_menu = False

    # Отрисовка начальной заставки
    screen.fill(black)
    screen.blit(background_image, background_rect)

    # Отображение на экране
    pygame.display.flip()


# Главное меню
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Очистка экрана и рисование меню
        screen.fill(black)
        font = pygame.font.Font(None, 36)
        text_play = font.render("Играть", True, white)
        text_exit = font.render("Выход", True, white)
        text_play_rect = text_play.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        text_exit_rect = text_exit.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(text_play, text_play_rect)
        screen.blit(text_exit, text_exit_rect)

        # Определение положения курсора
        cursor_pos = pygame.mouse.get_pos()

        # Проверка нажатий на кнопки
        if text_play_rect.collidepoint(cursor_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
        elif text_exit_rect.collidepoint(cursor_pos):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()

        # Отображение на экране
        pygame.display.flip()


# Запуск главного меню после начальной заставки
if main_menu():
    game_started = True

# Основной игровой цикл
while game_started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка управления игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.move_ip(-5, 0)
    if keys[pygame.K_d]:
        player_rect.move_ip(5, 0)
    if keys[pygame.K_SPACE]:
        # Добавьте здесь логику для действия при нажатии на пробел
        pass

    # Отрисовка игровой сцены и игрока
    screen.fill(black)
    screen.blit(game_scene_image, game_scene_rect)
    screen.blit(player_image, player_rect)

    # Отображение на экране
    pygame.display.flip()

# Завершение работы Pygame
pygame.mixer.music.stop()  # Остановить музыку перед выходом
pygame.quit()
sys.exit()
