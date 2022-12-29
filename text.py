import pygame

pygame.init()
pygame.font.init()

def text(text, font):
    main_text = font.render(str(text), 1, pygame.Color("black"))
    return main_text
def text_mid(main_text, y)
    renders.blit(main_text, (render_screen_size[0] / 2 - main_text.get_width() / 2, y))