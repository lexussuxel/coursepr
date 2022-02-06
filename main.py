import os
from math import fabs
from ball_basket import *
from random import randrange
from line import Line
from time import sleep

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("back_music.mp3")
pygame.mixer.music.set_volume(0.4)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.mixer.music.play()

clock = pygame.time.Clock()


path = os.path.dirname(__file__)
ball_path = path + "/ball.png"
basket_path = path + "/basket.png"
boot_img = pygame.image.load("boot_back.png")
button_img = pygame.image.load("button.png")
wasted_img = pygame.image.load("wasted.png")
wasted_img = pygame.transform.scale(wasted_img, (400, 200))
aws_img = pygame.image.load("awesome.png")
aws_img = pygame.transform.scale(aws_img, (400, 200))
button_img = pygame.transform.scale(button_img, (50, 50))
tr_boot_img = pygame.transform.scale(boot_img, (WIDTH, HEIGHT))

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


button = pygame.Rect(20, 20, 50, 50)
run = True
while count_music < 500:
    screen.fill(BLACK)
    screen.blit(tr_boot_img, tr_boot_img.get_rect())
    clock.tick(FPS)
    count_music += 1
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            count_music = 501
            run = False
            break

music_pl = True
ind_a = False
press_m_ind = False
jump_ind = False

score = 0
all_sprites = pygame.sprite.Group()
ball = reset(ball_path, screen)
left_l = Line(basket_left_line)
mid_l = Line(basket_middle_line)
right_l = Line(basket_right_line)
basket = Basket(basket_path, basket_start_pos[0], basket_start_pos[1])
lines = (left_l, mid_l, right_l)
all_sprites.add(ball)
all_sprites.add(basket)
all_sprites.add(left_l, mid_l, right_l)
end_ind = False


while run:
    clock.tick(FPS)
    screen.fill(WHITE)
    all_sprites.draw(screen)
    draw_text(screen, "score: " + str(score), 18, WIDTH / 2, 10)
    pygame.draw.line(screen, BLACK, line_pos[0], line_pos[1], 3)
    screen.blit(button_img, (20, 20))
    if ball.rect.bottom < 0 or ball.rect.left > WIDTH or ball.rect.right < 0:
        if ball.point:
            score += 1
            screen.blit(aws_img, (300, 150))
        else:
            screen.blit(wasted_img, (300, 150))
            score = 0
        end_ind = True
        all_sprites.remove(ball)
        rand = randrange(40 - basket_right_line[0][1], line_pos[0][1] - 180)
        for line in lines:
            line.rect.y += rand
        basket.rect.y += rand
        ball = reset(ball_path, screen)
        all_sprites.add(ball)

    prev_c = ball.rect.y - ball.speedy
    if (ball.rect.x > basket_left_line[0][0] and (ball.rect.x + ball_size[0]) < basket_middle_line[0][0]) and (
            prev_c < basket_middle_line[0][1] and (ball.rect.y + (ball_size[1] / 2)) > basket_middle_line[0][1]):
        ball.point = True

    if ball.rect.bottom + ball.speedy > line_pos[1][1] + 1:
        ball.rect.y = line_pos[1][1] - ball_size[1]
        ball.speedy *= -1
        ball.speedy += 5
        ball.floor_count += 1
        if ball.floor_count == 2:
            if ball.point:
                score += 1
                screen.blit(aws_img, (300, 150))
            else:
                screen.blit(wasted_img, (300, 150))
                score = 0
            end_ind = True
            all_sprites.remove(ball)
            rand = randrange(0, line_pos[0][1] - 280)
            dell = basket.rect.y - rand
            for line in lines:
                line.rect.y -= dell
            basket.rect.y = rand
            ball = reset(ball_path, screen)
            all_sprites.add(ball)

    for line in (left_l, mid_l, right_l):
        if fabs(ball.rect.x + ball_size[0] / 2 - line.rect.x) <= fabs(ball.speedx) and fabs(
                ball.rect.y + ball_size[0] - line.rect.y) <= fabs(ball.speedy) and ball.speedy < 0:
            ball.speedy *= -1
        if pygame.sprite.collide_rect(ball, line):
            ball.speedx *= -1
            ball.speedx -= ball.speedx / 10

    all_sprites.update()
    pygame.display.flip()
    if end_ind:
        sleep(1)
        end_ind = False
    if pygame.key.get_pressed()[pygame.K_m]:
        if not press_m_ind:
            if music_pl:
                pygame.mixer.music.set_volume(0.0)
                music_pl = False
            else:
                pygame.mixer.music.set_volume(0.4)
                music_pl = True
            press_m_ind = True
    else:
        press_m_ind = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                ind_a = True
                if ball.point:
                    score += 1
                all_sprites.remove(ball)
                ball = reset(ball_path, screen)
                ball.mouse_ind = True
                all_sprites.add(ball)
        elif ind_a:
            ball.jump_ind = False
            ind_a = False
        else:
            ball.mouse_ind = False
        if event.type == pygame.QUIT:
            run = False
            break


pygame.quit()
