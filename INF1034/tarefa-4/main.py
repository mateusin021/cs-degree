import pygame

width = 800  #Largura Janela
height = 600 #Altura Janela

def load():
    global sys_font, clock, px, sol, horario, corAstro, p
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()
    px = 30
    p=1
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
    pygame.draw.rect(screen, (204, 102, 0), (300, 340, 60, 60))
    pygame.draw.rect(screen, (128, 0, 0), (330, 380, 10, 20))
    pygame.draw.rect(screen, (204, 102, 0), (150, 340, 60, 60))
    pygame.draw.rect(screen, (128, 0, 0), (170, 380, 10, 20))
    
    screen.blit(gomes, (350,200))
def nuvens():
    pygame.draw.circle(screen, (255,255,255), (px, 150), 30)
    pygame.draw.circle(screen, (255,255,255), (20+px, 150), 30)
    pygame.draw.circle(screen, (255,255,255), (40+px, 150), 30)

def solzin():
    pygame.draw.circle(screen, corAstro, (sol, 100), 30)
    pygame.draw.line(screen, corAstro, (sol, 50), (sol, 150), 5)
    pygame.draw.line(screen, corAstro, (sol-50, 100), (sol+50, 100), 5)
    pygame.draw.line(screen, corAstro, (sol-40, 140), (sol+40, 60), 7)
    pygame.draw.line(screen, corAstro, (sol-40, 60), (sol+40, 140), 7)

def lua():
    pygame.draw.circle(screen, corAstro, (sol, 100), 30)
def update(dt):
    global px, sol, horario, corAstro, p 
    keys = pygame.key.get_pressed()
    

    #movimento nuvens
    px=px+(0.1*dt*p)
    
    if px <=30 or px >= width-60:
       p *= -1
    

    #movimento sol
    if keys[pygame.K_RIGHT]:
       sol = sol + (0.1 * dt)
       
    if keys[pygame.K_LEFT]:
       sol = sol - (0.1 * dt)

    # limite sol
    if sol > width:
        sol = width -20

    elif sol < 0:
        sol = 20

    # horarios do dia

    manha = width/3
    tarde = (width*2)/3
    if sol <=manha:
        horario = (51, 204, 255)
        corAstro = (255, 255, 0)
        solzin()
        nuvens()
    elif sol <= tarde:
        horario = (36, 75, 214)
        corAstro = (255, 255, 0)
        solzin()
        nuvens()
    else: 
        horario = (7, 24, 82)
        corAstro = (217, 217, 217)
        lua()
        nuvens()

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