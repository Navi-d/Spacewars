# Imports
import math
import random
import pygame
from pygame import mixer
import sys
import time
from pygame import mouse
from pygame.locals import *
import webbrowser


# Intialize the pygame
pygame.init()

# window size
s_width = 1200
s_height = 750

# Frames
clock = pygame.time.Clock()

# create the screen (to be able to be resized)
pg_flag = pygame.RESIZABLE
window = pygame.display.set_mode((s_width, s_height), pygame.RESIZABLE)
screen = pygame.Surface((s_width, s_height))
original_window_size = screen.get_size()


# Background and Wallpapers
background = pygame.image.load("Data\photos and wallpapers\\space.jpg")
menu_wp = pygame.image.load("Data\photos and wallpapers\menu.jpg")
game_over_wp = pygame.image.load("Data\photos and wallpapers\game over.jpg")
sound_credits_wp = pygame.image.load(
    "Data\photos and wallpapers\sound credits wp.png")
game_controls_wp = pygame.image.load(
    "Data\photos and wallpapers\game controls wp.png")
credit_image = pygame.image.load("Data\photos and wallpapers\credit wp.png")
attention_wp = pygame.image.load("Data\photos and wallpapers\\attention.png")

# for fullscreen process
fullscreen = False

# caption and icon
pygame.display.set_caption("Spacewars")
icon = pygame.image.load("Data\photos and wallpapers\spaceship.png")
pygame.display.set_icon(icon)

# Menu music
mixer.music.load(
    "Data\sounds\Luke-Bergs-No-More-Worries.mp3")
mixer.music.play(-1)

# game over music
game_over_sound = mixer.Sound(
    "Data\sounds\game over sound.wav")

# about window resize
screen_pos = (0, 0)


def scale():
    window_size = window.get_size()
    return (
        (window_size[0] - screen_pos[0] * 2) / original_window_size[0],
        (window_size[1] - screen_pos[1] * 2) / original_window_size[1]
    )


def mouse_pos():
    s = scale()
    m_pos = pygame.mouse.get_pos()
    scaled_pos = (
        (m_pos[0] - screen_pos[0]) / s[0],
        (m_pos[1] - screen_pos[1]) / s[1]
    )
    return scaled_pos


# buttons
start_img = pygame.image.load(
    "Data\\buttons\\button_start.png").convert_alpha()
exit_img = pygame.image.load("Data\\buttons\\button_exit.png").convert_alpha()
credit_img = pygame.image.load(
    "Data\\buttons\\button_credit.png").convert_alpha()
play_again_img = pygame.image.load(
    "Data\\buttons\\button_play-again.png").convert_alpha()
sound_credit_img = pygame.image.load(
    "Data\\buttons\\button_sound-credits.png").convert_alpha()
back_sound_img = pygame.image.load(
    "Data\\buttons\\button_back.png").convert_alpha()
game_controls_img = pygame.image.load(
    "Data\\buttons\\button_game-controls.png").convert_alpha()
menu_button_img = pygame.image.load(
    "Data\\buttons\\button_menu.png").convert_alpha()
attention_img = pygame.image.load(
    "Data\\buttons\\button_read-before-playing.png").convert_alpha()
github_link_img = pygame.image.load(
    "Data\\buttons\\button_github-link.png").convert_alpha()


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = mouse_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


start_button = Button(350, 320, start_img, 0.9)
exit_button = Button(620, 320, exit_img, 0.9)
credit_button = Button(1025, 700, credit_img, 0.8)
exit_button_over = Button(200, 500, exit_img, 0.7)
play_again = Button(200, 200, play_again_img, 0.7)
sound_credits = Button(10, 10, sound_credit_img, 0.7)
back_button = Button(10, 700, back_sound_img, 0.9)
game_controls_button = Button(150, 10, game_controls_img, 0.7)
menu_button = Button(200, 350, menu_button_img, 0.7)
attention_button = Button(1000, 10, attention_img, 0.7)
link_button = Button(500, 10, github_link_img, 0.8)

# Player
player_image = pygame.image.load("Data\photos and wallpapers\player.png")
x_player = 420
y_player = 580
x_player_change = 0
y_player_change = 0


def player(x, y):
    screen.blit(player_image, (x, y))


# Enemy
enemy_image = []
x_enemy = []
y_enemy = []
enemy_x_exchange = []
enemy_y_exchange = []
number_of_enemies = 20


for i in range(number_of_enemies):
    enemy_image.append(pygame.image.load(
        "Data\photos and wallpapers\\alien.png"))
    x_enemy.append(random.randint(0, 1134))
    y_enemy.append(random.randint(0, 100))
    enemy_x_exchange.append(3)
    enemy_y_exchange.append(3)


def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))


# Bullet
bullet_image = pygame.image.load("Data\photos and wallpapers\\bullet.png")
x_bullet = 0
y_bullet = 580
x_bullet_change = 0
y_bullet_change = 15
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 13, y + 5))


# score
score_value = 0
font = pygame.font.Font(None, 40)

x_text = 10
y_text = 10


def show_score(x, y):
    score = font.render(
        "Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_score_end(x, y):
    end_score = font.render(
        "Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(end_score, (x, y))


def github():
    webbrowser.open('https://github.com/Navi-d/Spacewars.git')


# timer
time_limit = 60
start_time = time.time()
timer_font = pygame.font.Font(None, 40)

plus_font = pygame.font.Font(None, 40)


def timer(x, y):
    global start_time
    global game_over_sound
    elapsed_time = time.time() - start_time
    time_left = timer_font.render(
        "time left : " + str(time_limit - int(elapsed_time)), True, (255, 255, 255))
    screen.blit(time_left, (x, y))

    if score_value == 20:
        plus = plus_font.render('+8', True, (0, 200, 0))
        screen.blit(plus, (475, 10))
    if score_value == 40:
        plus = plus_font.render('+10', True, (0, 200, 0))
        screen.blit(plus, (475, 10))
    if score_value == 60:
        plus = plus_font.render('+12', True, (0, 200, 0))
        screen.blit(plus, (475, 10))
    if score_value == 80:
        plus = plus_font.render('+14', True, (0, 200, 0))
        screen.blit(plus, (475, 10))
    if score_value == 110:
        plus = plus_font.render('+16', True, (0, 200, 0))
        screen.blit(plus, (475, 10))
    if score_value == 150:
        plus = plus_font.render('+18', True, (0, 200, 0))
        screen.blit(plus, (475, 10))
    if score_value == 200:
        plus = plus_font.render('+20', True, (0, 200, 0))
        screen.blit(plus, (475, 10))
    if score_value == 300:
        plus = plus_font.render('+22', True, (0, 200, 0))
        screen.blit(plus, (475, 10))
    if elapsed_time > time_limit:
        mixer.music.stop()
        game_over_sound.play()
        start_time = time.time()
        running = False
        game_over_screen()


# Player colliding with an enemy (based on distance)
def is_collision_over(x_enemy, y_enemy, x_player, y_player):
    distance = math.sqrt(math.pow(x_enemy - x_player, 2) +
                         (math.pow(y_enemy - y_player, 2)))
    if distance < 30:
        return True


# Bullet colliding with an enemy (based on distance)
def is_collision(x_enemy, y_enemy, x_bullet, y_bullet):
    distance = math.sqrt(math.pow(x_enemy - x_bullet, 2) +
                         (math.pow(y_enemy - y_bullet, 2)))
    if distance < 30 and bullet_state == 'fire':
        return True


# Game over screen
def game_over_screen():
    global start_time
    global screen
    global window
    global fullscreen

    while True:
        start_time = time.time()

        screen.blit(game_over_wp, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (event.w, event.w * original_window_size[1] / original_window_size[0]), pg_flag)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(
                            (window.get_width(), window.get_height()), pygame.FULLSCREEN)
                if event.key == K_ESCAPE:

                    window = pygame.display.set_mode(
                        (s_width, s_height), pygame.RESIZABLE)
                    fullscreen = False

        if exit_button_over.draw():
            sys.exit()
        if play_again.draw():

            game_play()

        if menu_button.draw():
            mixer.music.load(
                "Data\sounds\Luke-Bergs-No-More-Worries.mp3")
            mixer.music.play(-1)
            menu()
        show_score_end(10, 10)
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()

# credit screen


def credit():
    global screen
    screen.blit(credit_image, (0, 0))
    global window
    global fullscreen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (event.w, event.w * original_window_size[1] / original_window_size[0]), pg_flag)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(
                            (window.get_width(), window.get_height()), pygame.FULLSCREEN)
                if event.key == K_ESCAPE:

                    window = pygame.display.set_mode(
                        (s_width, s_height), pygame.RESIZABLE)
                    fullscreen = False

        if back_button.draw():
            menu()
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))

        pygame.display.update()

# songs credits screen


def sound_credit():
    global screen
    screen.blit(sound_credits_wp, (0, 0))
    global window
    global fullscreen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (event.w, event.w * original_window_size[1] / original_window_size[0]), pg_flag)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(
                            (window.get_width(), window.get_height()), pygame.FULLSCREEN)
                if event.key == K_ESCAPE:

                    window = pygame.display.set_mode(
                        (s_width, s_height), pygame.RESIZABLE)
                    fullscreen = False

        if back_button.draw():
            menu()
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()

# Game details and controls screen


def game_controls():
    global screen
    screen.blit(game_controls_wp, (0, 0))
    global window
    global fullscreen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (event.w, event.w * original_window_size[1] / original_window_size[0]), pg_flag)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(
                            (window.get_width(), window.get_height()), pygame.FULLSCREEN)
                if event.key == K_ESCAPE:

                    window = pygame.display.set_mode(
                        (s_width, s_height), pygame.RESIZABLE)
                    fullscreen = False

        if back_button.draw():
            menu()
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()

# attention screen


def attention():
    global screen
    screen.blit(attention_wp, (0, 0))
    global window
    global fullscreen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (event.w, event.w * original_window_size[1] / original_window_size[0]), pg_flag)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(
                            (window.get_width(), window.get_height()), pygame.FULLSCREEN)
                if event.key == K_ESCAPE:
                    window = pygame.display.set_mode(
                        (s_width, s_height), pygame.RESIZABLE)
                    fullscreen = False

        if back_button.draw():
            menu()
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()


# The main game function and while loop
def game_play():
    global x_player
    global x_player_change
    global y_player
    global y_player_change
    global x_bullet
    global y_bullet
    global bullet_state
    global score_value
    global time_left
    global game_over_sound
    global time_limit
    global screen
    global window
    global fullscreen
    x_player = 420
    y_player = 580
    x_player_change = 0
    y_player_change = 0
    x_bullet = 0
    y_bullet = 580
    x_bullet_change = 0
    y_bullet_change = 15
    bullet_state = "ready"
    score_value = 0
    number_of_enemies = 20
    enemy_image = []
    x_enemy = []
    y_enemy = []
    enemy_x_exchange = []
    enemy_y_exchange = []
    for i in range(number_of_enemies):
        enemy_image.append(pygame.image.load(
            "Data\photos and wallpapers\\alien.png"))
        x_enemy.append(random.randint(0, 1134))
        y_enemy.append(random.randint(0, 100))
        enemy_x_exchange.append(2)
        enemy_y_exchange.append(2)
    screen.blit(background, (0, 0))
    mixer.music.load(
        "Data\sounds\makai-symphony-dragon-slayer.mp3")
    mixer.music.play(-1)
    running = True
    time_limit = 60
    pygame.display.update()
    while running:
        game_over_sound.stop()

        # RGB
        screen.blit(background, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (event.w, event.w * original_window_size[1] / original_window_size[0]), pg_flag)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(
                            (window.get_width(), window.get_height()), pygame.FULLSCREEN)
                if event.key == K_ESCAPE:

                    window = pygame.display.set_mode(
                        (s_width, s_height), pygame.RESIZABLE)
                    fullscreen = False

                # if any movement keys are pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_player_change = -5.5
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_player_change = 5.5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_player_change = -5.5
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_player_change = 5.5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound(
                            'Data\sounds\laser.wav')
                    bullet_sound.play()
                    # Get the current x and y cordinate of the spaceship
                    x_bullet = x_player
                    y_bullet = y_player

                    fire_bullet(x_bullet, y_bullet)
            # for key ups
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_player_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_player_change = 0

        # player staying on the screen
        x_player += x_player_change
        if x_player <= 0:
            x_player = 0
        elif x_player >= 1133:
            x_player = 1133
        y_player += y_player_change
        if y_player <= 0:
            y_player = 0
        elif y_player >= 683:
            y_player = 683

        # the player-enemy collision
        for i in range(number_of_enemies):
            enemy_player = is_collision_over(
                x_enemy[i], y_enemy[i], x_player, y_player)
            if enemy_player:
                mixer.music.stop()
                game_over_sound = mixer.Sound(
                    "Data\sounds\game over sound.wav")
                game_over_sound.play()
                for j in range(number_of_enemies):
                    y_enemy[j] = 2000

            # enemy staying on the screen
            x_enemy[i] += enemy_x_exchange[i]
            if x_enemy[i] <= 0:
                enemy_x_exchange[i] = -enemy_x_exchange[i]
            elif x_enemy[i] >= 1134:
                enemy_x_exchange[i] = -enemy_x_exchange[i]
            y_enemy[i] += enemy_y_exchange[i]
            if y_enemy[i] <= 0:
                enemy_y_exchange[i] = -enemy_y_exchange[i]
            elif y_enemy[i] >= 686:
                enemy_y_exchange[i] = -enemy_y_exchange[i]
        # the enemy-bullet collision
            collision = is_collision(
                x_enemy[i], y_enemy[i], x_bullet, y_bullet)
            if collision:
                explosion_sound = mixer.Sound(
                    "Data\sounds\explosion.wav")
                explosion_sound.play()

                bullet_state = "ready"
                x_enemy[i] = random.randint(0, 830)
                y_enemy[i] = random.randint(0, 100)
                score_value += 1
            # increase of the time and number of enemies throughout the game
            if score_value == 0:
                number_of_enemies = 3
            elif score_value == 20:
                number_of_enemies = 4
                time_limit = 68

            elif score_value == 40:
                number_of_enemies = 5
                time_limit = 78
            elif score_value == 60:
                number_of_enemies = 7
                time_limit = 80
            elif score_value == 80:
                number_of_enemies = 8
                time_limit = 94
            elif score_value == 110:
                number_of_enemies = 10
                time_limit = 110
            elif score_value == 150:
                number_of_enemies = 12
                time_limit = 128
            elif score_value == 200:
                number_of_enemies = 15
                time_limit = 148
            elif score_value == 300:
                number_of_enemies = 17
                time_limit = 170
            elif score_value == 400:
                number_of_enemies = 20

            # calling enemy function
            enemy(x_enemy[i], y_enemy[i], i)
            global start_time
            if y_enemy[i] > 1000:
                start_time = time.time()
                running = False
                game_over_screen()
                break

        # Bullet Movement
        if y_bullet <= 0:
            y_bullet = y_player
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(x_bullet, y_bullet)
            y_bullet -= y_bullet_change

        # frame
        clock.tick(100)

        # calling player function
        player(x_player, y_player)

        # calling show score function
        show_score(x_text, y_text)

        # calling timer function
        timer(300, 10)

        # updating the screen
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()


# menu function
def menu():
    global start_time
    global screen
    global s_width
    global s_height
    global screen
    global window
    global fullscreen

    while True:
        game_over_sound.stop()

        start_time = time.time()

        screen.blit(menu_wp, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == VIDEORESIZE:
                if not fullscreen:

                    window = pygame.display.set_mode(
                        (event.w, event.w * original_window_size[1] / original_window_size[0]), pg_flag)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode(
                            (window.get_width(), window.get_height()), pygame.FULLSCREEN)
                        fullscreen = True

                if event.key == K_ESCAPE:
                    window = pygame.display.set_mode(
                        (s_width, s_height), pygame.RESIZABLE)
                    fullscreen = False

        if start_button.draw():

            game_play()

        if exit_button.draw():
            sys.exit()

        if credit_button.draw():

            credit()

        if sound_credits.draw():
            sound_credit()

        if game_controls_button.draw():
            game_controls()

        if attention_button.draw():
            attention()

        if link_button.draw():
            github()
            for event in pygame.event.get():
                window = pygame.display.set_mode(
                    (s_width, s_height), pygame.RESIZABLE)
            fullscreen = False

        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()


# calling the menu function
menu()

# THANKS FOR CHECKING THIS GAME OUT!
