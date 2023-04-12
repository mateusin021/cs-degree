import pygame

width = 800  #Largura Janela
height = 600 #Altura Janela

def load():
    global sys_font
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    global gomes
    gomes = pygame.image.load('manoel.png')
    gomes = pygame.transform.scale(gomes, (100,200))

def draw_screen(screen):
    screen.fill((51, 204, 255))
    #Cria Imagem da String
    pygame.draw.rect(screen, (255, 204, 102), (0, 400, 800, 800))
    pygame.draw.polygon(screen,(204, 153, 0), [(450, 400), (550, 400),(500, 300)])
    pygame.draw.polygon(screen,(204, 153, 0), [(550, 400), (650, 400),(600, 350)])
    pygame.draw.circle(screen, (255, 255, 0), (600, 200), 50)
    pygame.draw.rect(screen, (204, 102, 0), (300, 340, 60, 60))
    pygame.draw.rect(screen, (128, 0, 0), (330, 380, 10, 20))
    pygame.draw.rect(screen, (204, 102, 0), (150, 340, 60, 60))
    pygame.draw.rect(screen, (128, 0, 0), (170, 380, 10, 20))
    screen.blit(gomes, (350,200))


def main_loop(screen):
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break
        # Desenha objetos na tela 
        draw_screen(screen)
        # Pygame atualiza o seu estado
        pygame.display.update() 


pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()