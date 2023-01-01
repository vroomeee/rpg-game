import pygame
import sys

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 80)

screen_size = (1280, 800)
render_screen_size = (640, 400)
win = pygame.display.set_mode(screen_size)
pygame.display.set_caption("RPG game")

renders = pygame.Surface(render_screen_size)
#texts
def get_font(size):
    font = pygame.font.SysFont('comicsans', size)
    return font

def text(text, font):
    main_text = font.render(str(text), 1, pygame.Color("black"))
    return main_text

main_text = text("vroomeee", font)
start_button_text = text("click space bar to start", get_font(30))


def text_mid(main_text, y):
    renders.blit(main_text, (render_screen_size[0] / 2 - main_text.get_width() / 2, y))


main_text_loc = 50
main_text_vy = 0
main_text_ay = 0.01

def start_screen():
    on_main_screen = True
    while on_main_screen:
        global main_text_loc, main_text_ay, main_text_vy
        renders.fill(pygame.Color("white"))
        text_mid(main_text, main_text_loc)
        text_mid(start_button_text, 230)
        surf = pygame.transform.scale(renders, screen_size)
        win.blit(surf, (0, 0))
        for event in pygame.event.get(pygame.KEYDOWN, pygame.QUIT):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    on_main_screen = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        clock.tick(60)
        pygame.display.flip()
    # main_text_loc += main_text_vy
    # if main_text_loc > 55:
    #     main_text_loc -= main_text_vy
    #     main_text_vy = 0
    #     main_text_ay = -main_text_ay
    # elif main_text_loc < 45:
    #     main_text_loc -= main_text_vy
    #     main_text_vy = 0
    #     main_text_ay = -main_text_ay
    # main_text_vy += main_text_ay

def main_game():
    while True:
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
    surf = pygame.transform.scale(renders, screen_size)
    win.blit(surf, (0, 0))
    clock.tick(60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    start_screen()
    main_game()
    surf = pygame.transform.scale(renders, screen_size)
    win.blit(surf, (0, 0))
    clock.tick(60)
    pygame.display.flip()
