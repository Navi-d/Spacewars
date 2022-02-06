import math
import random
import pygame
from pygame import mixer
import sys
import time
from pygame import mouse
from pygame.locals import *
import webbrowser


pygame.init()

s_width = 1200
s_height = 750


clock = pygame.time.Clock()


pg_flag = pygame.RESIZABLE
window = pygame.display.set_mode((s_width, s_height), pg_flag)
screen = pygame.Surface((s_width, s_height))
original_window_size = screen.get_size()

background = pygame.image.load("Data\photos and wallpapers\\space.jpg")
menu_wp = pygame.image.load("Data\photos and wallpapers\menu.jpg")
game_over_wp = pygame.image.load("Data\photos and wallpapers\game over.jpg")
sound_credits_wp = pygame.image.load(
    "Data\photos and wallpapers\sound credits wp.png")
game_controls_wp = pygame.image.load(
    "Data\photos and wallpapers\game controls wp.png")
credit_image = pygame.image.load("Data\photos and wallpapers\credit wp.png")
attention_wp = pygame.image.load("Data\photos and wallpapers\\attention.png")
thunder_wp = pygame.image.load("Data\photos and wallpapers\\dragonblue.jpg")
dragon_wp = pygame.image.load("Data\photos and wallpapers\\dragon.jpg")
dragonfire_wp = pygame.image.load("Data\photos and wallpapers\\dragonfire.jpg")
bullet_image = pygame.image.load("Data\photos and wallpapers\\bullet.png")
under_button = pygame.image.load(
    'Data\photos and wallpapers\\under_button.png')
under_button2 = pygame.image.load(
    'Data\photos and wallpapers\\under_button2.png')
under_button3 = pygame.image.load(
    'Data\photos and wallpapers\\under_button3.png')

fullscreen = False


pygame.display.set_caption("Spacewars")
icon = pygame.image.load("Data\photos and wallpapers\spaceship.png")
pygame.display.set_icon(icon)


mixer.music.load(
    "Data\sounds\Luke-Bergs-No-More-Worries.mp3")
mixer.music.play(-1)


game_over_sound = mixer.Sound(
    "Data\sounds\game over sound.wav")
player1sound = mixer.Sound("Data\sounds\player1sound.wav")
player2sound = mixer.Sound("Data\sounds\player2sound.wav")
player3sound = mixer.Sound("Data\sounds\player3sound.wav")
icedragonsound = mixer.Sound("Data\sounds\\the ice dragon.wav")
whitedragonsound = mixer.Sound("Data\sounds\\the white dragon.wav")
firedragonsound = mixer.Sound("Data\sounds\\the fire dragon.wav")


def scale():
    window_size = window.get_size()

    return (
        (window_size[0]) / original_window_size[0],
        (window_size[1]) / original_window_size[1]
    )


def mouse_pos():
    s = scale()

    m_pos = pygame.mouse.get_pos()

    scaled_pos = (
        (m_pos[0]) / s[0],
        (m_pos[1]) / s[1]
    )
    return scaled_pos


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
spaceship_change_img = pygame.image.load(
    "Data\\buttons\\button_spaceships.png").convert_alpha()
player_1_img = pygame.image.load(
    "Data\photos and wallpapers\player.png").convert_alpha()
player_2_img = pygame.image.load(
    "Data\photos and wallpapers\spaceship (3).png").convert_alpha()
player_3_img = pygame.image.load(
    "Data\photos and wallpapers\spaceship (4).png").convert_alpha()


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

        pos = mouse_pos()
        collidepoints = [(436, 300), (568, 300), (700, 300)]
        if self.rect.collidepoint(pos):
            if self.rect.collidepoint(collidepoints[0]):
                screen.blit(under_button, (436, 365))
            if self.rect.collidepoint(collidepoints[1]):
                screen.blit(under_button2, (568, 365))
            if self.rect.collidepoint(collidepoints[2]):
                screen.blit(under_button3, (700, 365))

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

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
change_spaceship = Button(10, 50, spaceship_change_img, 0.7)
player_1 = Button(436, 300, player_1_img, 1)
player_2 = Button(568, 300, player_2_img, 1)
player_3 = Button(700, 300, player_3_img, 1)

player_images = [(player_1_img), (player_2_img), (player_3_img)]
player_image = player_1_img


def player(x, y):
    screen.blit(player_image, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 13, y + 5))


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


time_limit = 60
timer_font = pygame.font.Font(None, 40)
plus_font = pygame.font.Font(None, 40)
start_time = time.time()


def timer(x, y):
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
        running = False
        game_over_screen()


def is_collision_over(x_enemy, y_enemy, x_player, y_player):
    distance = math.sqrt(math.pow(x_enemy - x_player, 2) +
                         (math.pow(y_enemy - y_player, 2)))
    if distance < 30:
        return True


def is_collision(x_enemy, y_enemy, x_bullet, y_bullet):
    distance = math.sqrt(math.pow(x_enemy - x_bullet, 2) +
                         (math.pow(y_enemy - y_bullet, 2)))
    if distance < 30 and bullet_state == 'fire':
        return True


choice_font = pygame.font.Font(None, 40)


def player_choice():
    global window
    global fullscreen
    global player_image

    while True:
        screen.fill((255, 255, 255))

        choice = choice_font.render(
            "Please click on the spaceship you wish to play with!", True, (0, 0, 0))
        screen.blit(choice, (250, 70))
        if player_1.draw():
            p_1()
        if player_2.draw():
            p_2()
        if player_3.draw():
            p_3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (window.get_width(), window.get_height()), pg_flag)
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


def p_1():
    global window, fullscreen, player_image
    player_1 = Button(568, 200, player_1_img, 1)
    icedragonsound.play()
    player1sound.play()
    player2sound.stop()
    player3sound.stop()
    whitedragonsound.stop()
    firedragonsound.stop()
    while True:
        screen.blit(thunder_wp, (0, 0))
        choice = choice_font.render(
            "The Ice Dragon selected!", True, (0, 200, 0))
        screen.blit(choice, (422, 150))
        mixer.music.stop()

        player_image = player_images[0]
        if player_1.draw():
            pass
        if player_2.draw():
            p_2()
        if player_3.draw():
            p_3()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (window.get_width(), window.get_height()), pg_flag)
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
            icedragonsound.stop()
            player1sound.stop()
            mixer.music.play()
            menu()
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()


def p_2():
    global window, fullscreen, player_image
    player_2 = Button(568, 200, player_2_img, 1)
    whitedragonsound.play()
    player2sound.play()
    player1sound.stop()
    player3sound.stop
    icedragonsound.stop()
    firedragonsound.stop()
    while True:
        screen.blit(dragon_wp, (0, 0))
        choice = choice_font.render(
            "The White Dragon selected!", True, (0, 0, 0))
        screen.blit(choice, (420, 150))
        mixer.music.stop()
        player_image = player_images[1]
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        if player_1.draw():
            p_1()
        if player_2.draw():
            pass
        if player_3.draw():
            p_3()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (window.get_width(), window.get_height()), pg_flag)
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
            whitedragonsound.stop()
            player2sound.stop()
            mixer.music.play()
            menu()
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()


def p_3():
    global window, fullscreen, player_image
    player_3 = Button(568, 200, player_3_img, 1)
    firedragonsound.play()
    player3sound.play()
    player2sound.stop()
    player1sound.stop()
    icedragonsound.stop()
    whitedragonsound.stop()
    while True:
        screen.blit(dragonfire_wp, (0, 0))
        choice = choice_font.render(
            "The Fire Dragon selected!", True, (200, 0, 0))
        screen.blit(choice, (423, 150))
        mixer.music.stop()
        player_image = player_images[2]
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        if player_1.draw():
            p_1()
        if player_2.draw():
            p_2()
        if player_3.draw():
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (window.get_width(), window.get_height()), pg_flag)
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
            firedragonsound.stop()
            player3sound.stop()
            mixer.music.play()
            menu()
        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()


def game_over_screen():
    global start_time
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
                        (window.get_width(), window.get_height()), pg_flag)
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


def credit():
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
                        (window.get_width(), window.get_height()), pg_flag)
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


def sound_credit():
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
                        (window.get_width(), window.get_height()), pg_flag)
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


def game_controls():
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
                        (window.get_width(), window.get_height()), pg_flag)
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


def attention():
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
                        (window.get_width(), window.get_height()), pg_flag)
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


def game_play():
    global time_left
    global time_limit
    global score_value
    global bullet_state
    global game_over_sound
    global window
    global fullscreen
    x_player = 568
    y_player = 580
    x_player_change = 0
    y_player_change = 0
    x_bullet = 0
    y_bullet = 0
    y_bullet_change = 15
    bullet_state = "ready"
    score_value = 0

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
        enemy_x_exchange.append(2.2)
        enemy_y_exchange.append(2.2)

    def enemy(x, y, i):
        screen.blit(enemy_image[i], (x, y))

    mixer.music.load(
        "Data\sounds\makai-symphony-dragon-slayer.mp3")
    mixer.music.play(-1)
    running = True
    pygame.display.update()
    while running:
        game_over_sound.stop()

        screen.blit(background, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == VIDEORESIZE:
                if not fullscreen:
                    window = pygame.display.set_mode(
                        (window.get_width(), window.get_height()), pg_flag)
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

                    x_bullet = x_player
                    y_bullet = y_player

                    fire_bullet(x_bullet, y_bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_player_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_player_change = 0

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

            enemy(x_enemy[i], y_enemy[i], i)

            if y_enemy[i] > 1000:
                running = False
                game_over_screen()
                break

        if bullet_state == "fire":
            fire_bullet(x_bullet, y_bullet)
            y_bullet -= y_bullet_change

        clock.tick(100)

        player(x_player, y_player)

        show_score(x_text, y_text)

        timer(300, 10)

        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()


def menu():
    global start_time
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
                        (window.get_width(), window.get_height()), pg_flag)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = True
                    if fullscreen:
                        window = pygame.display.set_mode(
                            (window.get_width(), window.get_height()), pygame.FULLSCREEN)

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

        if change_spaceship.draw():
            player_choice()

        if link_button.draw():
            github()
            for event in pygame.event.get():
                window = pygame.display.set_mode(
                    (s_width, s_height), pygame.RESIZABLE)
            fullscreen = False

        _screen = pygame.transform.scale(screen, window.get_size())
        window.blit(_screen, (0, 0))
        pygame.display.update()


menu()
