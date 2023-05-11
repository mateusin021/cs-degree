import pygame
width = 500  #Largura Janela
height = 600 #Altura Janela
cinza = (89, 89, 89)
global result, operator,op1
result = ""
operator = ""
op1=""
def calcula(a,b,op):
    if op == "+":
        return a+b
    elif op =="-":
        return a-b
    elif op =="*":
        return a*b
    elif op =="/":
        return a/b
def load():
    global sys_font
    
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 50)

def check_click(x1,y1,w1,h1,x2,y2):
     return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def draw_screen(screen):
    screen.fill((191, 191, 191))
    # display
    pygame.draw.rect(screen, (204, 238, 255), (10,30,480,120))
    t = sys_font.render(result, False, (0,0,0))
    screen.blit(t, (20,60))

    # primeira fileira numeros

    pygame.draw.rect(screen, cinza, (20, 170, 100, 100))
    t = sys_font.render("7", False, (255,255,255))
    screen.blit(t, (55,195))

    pygame.draw.rect(screen, cinza, (130, 170, 100, 100))
    t = sys_font.render("8", False, (255,255,255))
    screen.blit(t, (165,195))

    pygame.draw.rect(screen, cinza, (240, 170, 100, 100))
    t = sys_font.render("9", False, (255,255,255))
    screen.blit(t, (275,195))

    # segunda fileira numeros

    pygame.draw.rect(screen, cinza, (20, 280, 100, 100))
    t = sys_font.render("4", False, (255,255,255))
    screen.blit(t, (55,305))

    pygame.draw.rect(screen, cinza, (130, 280, 100, 100))
    t = sys_font.render("5", False, (255,255,255))
    screen.blit(t, (165,305))

    pygame.draw.rect(screen, cinza, (240, 280, 100, 100))
    t = sys_font.render("6", False, (255,255,255))
    screen.blit(t, (275,305))

    # terceira fileira

    pygame.draw.rect(screen, cinza, (20, 390, 100, 100))
    t = sys_font.render("1", False, (255,255,255))
    screen.blit(t, (55,415))

    pygame.draw.rect(screen, cinza, (130, 390, 100, 100))
    t = sys_font.render("2", False, (255,255,255))
    screen.blit(t, (165,415))

    pygame.draw.rect(screen, cinza, (240, 390, 100, 100))
    t = sys_font.render("3", False, (255,255,255))
    screen.blit(t, (275,415))

    # quarta fileira

    pygame.draw.rect(screen, cinza, (20, 500, 100, 80))
    t = sys_font.render("c", False, (255,255,255))
    screen.blit(t, (55,515))

    pygame.draw.rect(screen, cinza, (130, 500, 100, 80))
    t = sys_font.render("0", False, (255,255,255))
    screen.blit(t, (165,515))

    pygame.draw.rect(screen, cinza, (240, 500, 100, 80))
    t = sys_font.render("=", False, (255,255,255))
    screen.blit(t, (275,515))

    # operadores
    
    pygame.draw.rect(screen, cinza, (350, 170, 100, 100))
    t = sys_font.render("+", False, (255,255,255))
    screen.blit(t, (385,195))

    pygame.draw.rect(screen, cinza, (350, 280, 100, 100))
    t = sys_font.render("-", False, (255,255,255))
    screen.blit(t, (385,305))

    pygame.draw.rect(screen, cinza, (350, 390, 100, 100))
    t = sys_font.render("x", False, (255,255,255))
    screen.blit(t, (385,415))

    pygame.draw.rect(screen, cinza, (350, 500, 100, 80))
    t = sys_font.render("/", False, (255,255,255))
    screen.blit(t, (385,515))

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global result,op1,operator
    if mouse_buttons[0]:
        # primeira fileira
        if check_click(20, 170, 100, 100, px_mouse, py_mouse):
            result += "7"
        if check_click(130, 170, 100, 100, px_mouse, py_mouse):
            result += "8"
        if check_click(240, 170, 100, 100, px_mouse, py_mouse):
            result += "9"
        # segunda fileira
        if check_click(20, 280, 100, 100, px_mouse, py_mouse):
            result += "4"
        if check_click(130, 280, 100, 100, px_mouse, py_mouse):
            result += "5"
        if check_click(240, 280, 100, 100, px_mouse, py_mouse):
            result += "6"
        # terceira fileira
        if check_click(20, 390, 100, 100, px_mouse, py_mouse):
            result += "1"
        if check_click(130, 390, 100, 100, px_mouse, py_mouse):
            result += "2"
        if check_click(240, 390, 100, 100, px_mouse, py_mouse):
            result += "3"
        # operadores
        if check_click(350, 170, 100, 100, px_mouse, py_mouse):
            op1 += result
            operator = "+"
            result = ""
        if check_click(350, 280, 100, 100, px_mouse, py_mouse):
            op1 += result
            operator = "-"
            result = ""
        if check_click(350, 390, 100, 100, px_mouse, py_mouse):
            op1 += result
            operator = "*"
            result = ""
        if check_click(350, 500, 100, 80, px_mouse, py_mouse):
            op1 += result
            operator = "/"
            result = ""
        # quarta fileira
        if check_click(20, 500, 100, 80, px_mouse, py_mouse):
            result = ""
        if check_click(130, 500, 100, 80, px_mouse, py_mouse):
            result += "0"
        if check_click(240, 500, 100, 80, px_mouse, py_mouse):
            print([op1,result,operator])
            result = str(calcula(float(op1),float(result),operator))
            op1=""

def main_loop(screen):
    running = True 
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break
            elif e.type == pygame.MOUSEBUTTONDOWN: #detecta o inicio do clique do mouse
                    mouse_buttons = pygame.mouse.get_pressed()
                    px_mouse, py_mouse = pygame.mouse.get_pos()
                    mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            elif result =="1337":
                pygame.mixer.music.load("musica.mp3")
                pygame.mixer.music.play()
        # Desenha objetos na tela 
        draw_screen(screen)
        # Pygame atualiza o seu estado
        pygame.display.update() 


pygame.init()
pygame.display.set_caption('NAO DIGITA 1337!!!!')
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()