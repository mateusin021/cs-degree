import pygame
import math
import random

width = 800  #Largura Janela
height = 600 #Altura Janela

def load():
    global clock, px, bola, p1,p2, vetorx, vetory, pontos1,pontos2,sys_font
    
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 50)
    vetorx = 1
    vetory = 1
    pontos1 = 0
    pontos2 = 0

    clock = pygame.time.Clock() 

    bola = {
      "x": 390,
      "y": 300,
      "raio": 25,
    }
    p1 = {
      "x": 50,
      "y": 250,
      "width": 50,
      "height": 150,
      "speed": 0.2,
      "collided": False
    }
    p2 = {
      "x": 700,
      "y": 250,
      "width": 50,
      "height": 150,
      "speed": 0.5,
      "collided": False
    }



def check_box_collision(x1, y1, w1, h1, x2, y2, w2, h2):
   return (x1 < x2 + w2) and (x2 < x1 + w1) and (y1 < y2 + h2) and (y2 < y1 + h1)

def check_circular_collision(ax, ay, ar, bx, by, br):
   dx = bx - ax
   dy = by - ay
   dist = math.sqrt(dx * dx + dy * dy)
   return dist < ar + br



def update(dt):
    global vetorx,vetory,pontos2,pontos1
    keys = pygame.key.get_pressed()
    
    bola['x']=bola['x']+(0.2*dt*vetorx)
    bola['y']=bola['y']+(vetory)

    if check_box_collision(bola["x"], bola["y"], 50, 50, p1["x"], p1["y"], p1["width"],p1["height"]) or check_box_collision(bola["x"], bola["y"], 25, 25, p2["x"], p2["y"], p2["width"],p2["height"]):
       vetorx *= -1
       vetory = random.random()
       vetory *= -1

    if bola['x'] <= 30 or bola['x'] >= 775:
        bola['x'] = 400

    if bola['x'] >= 770:
        pontos1 +=1
    if bola['x'] <= 35:
        pontos2 +=1

    if bola['y'] <= 20 or bola['y'] >= 550:
        vetory *= -1
    
    if keys[pygame.K_UP]:
       p2["y"] = p2["y"] - (p2["speed"] * dt)
    
    if keys[pygame.K_DOWN]:
       p2["y"] = p2["y"] + (p2["speed"] * dt)
    if keys[pygame.K_w]:
       p1["y"] = p1["y"] - (p1["speed"] * dt)
    
    if keys[pygame.K_s]:
       p1["y"] = p1["y"] + (p1["speed"] * dt)

    
def draw_screen(screen):
    screen.fill((0,0,0))
    
    pontosa= str(pontos1)
    pontosb= str(pontos2)
    t = sys_font.render(pontosa, False, (255,255,255))
    screen.blit(t, (300,20))
    t = sys_font.render(pontosb, False, (255,255,255))
    screen.blit(t, (450,20))
    
    pygame.draw.circle(screen,(255,255,255), (bola["x"], bola["y"]), bola["raio"])
    pygame.draw.rect(screen,(255,255,255), (p1["x"], p1["y"], p1["width"], p1["height"]))
    pygame.draw.rect(screen,(255,255,255), (p2["x"], p2["y"], p2["width"], p2["height"]))
    # pygame.draw.circle(screen,(255,255,255), (p2["x"], p2["y"]), p2["raio"])

    # if p2["collided"] == True:
    #     pygame.draw.circle(screen,(255,0,0), (p2["x"], p2["y"]), p2["raio"])
    # else:
    #     pygame.draw.circle(screen,(255,255,255), (p2["x"], p2["y"]), p2["raio"])



def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break
        
        clock.tick(60) 			# Define FPS máximo
 
        # Calcula tempo transcorrido desde
        # a última atualização 
        dt = clock.get_time()
         
        draw_screen(screen)			 # Desenha objetos na tela
        
        update(dt) 			# Atualiza posição dos objetos da tela

        pygame.display.update() 	# Pygame atualiza o seu estado


pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()