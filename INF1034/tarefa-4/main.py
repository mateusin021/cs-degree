import pygame

width = 800  #Largura Janela
height = 600 #Altura Janela

def load():
    global sys_font, clock, px, sol, horario, corAstro
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()
    px = 0
    sol=600
    corAstro = (255, 255, 0)
    horario = (51, 204, 255)
    global gomes
    gomes = pygame.image.load('manoel.png')
    gomes = pygame.transform.scale(gomes, (100,200))

def draw_screen(screen):
    screen.fill(horario)
    #Cria Imagem da String
    pygame.draw.rect(screen, (255, 204, 102), (0, 400, 800, 800))
    pygame.draw.polygon(screen,(204, 153, 0), [(450, 400), (550, 400),(500, 300)])
    pygame.draw.polygon(screen,(204, 153, 0), [(550, 400), (650, 400),(600, 350)])
    pygame.draw.circle(screen, corAstro, (sol, 200), 50)
    pygame.draw.rect(screen, (204, 102, 0), (300, 340, 60, 60))
    pygame.draw.rect(screen, (128, 0, 0), (330, 380, 10, 20))
    pygame.draw.rect(screen, (204, 102, 0), (150, 340, 60, 60))
    pygame.draw.rect(screen, (128, 0, 0), (170, 380, 10, 20))
    nuvens()
    screen.blit(gomes, (350,200))
def nuvens():
    pygame.draw.circle(screen, (255,255,255), (px, 150), 30)
    pygame.draw.circle(screen, (255,255,255), (20+px, 150), 30)
    pygame.draw.circle(screen, (255,255,255), (40+px, 150), 30)

def update(dt):
    global px, sol, horario, corAstro
    keys = pygame.key.get_pressed()
    
    if px < width:
        px=px+(0.1*dt)

    #movimento sol
    if keys[pygame.K_RIGHT]:
       sol = sol + (0.1 * dt)
       
    if keys[pygame.K_LEFT]:
       sol = sol - (0.1 * dt)

    #movimento nuvens
    if px > width-30:
       px = 0
    
    # horarios do dia

    manha = width/3
    tarde = (width*2)/3
    if sol <=manha:
        horario = (51, 204, 255)
        corAstro = (255, 255, 0)
    elif sol <= tarde:
        horario = (36, 75, 214)
        corAstro = (255, 255, 0)
    else: 
        horario = (7, 24, 82)
        corAstro = (217, 217, 217)
       

def main_loop(screen):
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break
        clock.tick(60)        
 
        # Calcula tempo transcorrido desde
        # a última atualização 
        dt = clock.get_time()

        # Desenha objetos na tela 
        draw_screen(screen)

        # Atualiza posição dos objetos da tela
        update(dt)
        
        # Pygame atualiza o seu estado
        pygame.display.update() 


pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()