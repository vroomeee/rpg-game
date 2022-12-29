import pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 90)

screen_size = (800, 600)
render_screen_size = (800, 600)
win = pygame.display.set_mode(screen_size)
pygame.display.set_caption("RPG game")

renders = pygame.Surface(render_screen_size)

def

def start_screen():
    renders.fill(pygame.Color("white"))
    main_text = font.render("vroomeee", 1, pygame.Color("black"))
    renders.blit(main_text, (render_screen_size[0]/2-main_text.get_width()/2, 60))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    start_screen()
    surf = pygame.transform.scale(renders, screen_size)
    win.blit(surf, (0, 0))
    pygame.display.flip()
