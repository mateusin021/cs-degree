import random
import pygame

width = 900  #Largura Janela
height = 800 #Altura Janela

cores = [
    (255, 0, 0),
    (51, 204, 51),
    (51, 102, 255),
    (255, 255, 0),
    (204, 0, 153),
    (0, 255, 255),
    (255, 51, 204),
    (191, 191, 191),
    (0,0,0),
    (102, 51, 0)
    ]

letra = '''
O Rio de Janeiro continua lindo
O Rio de Janeiro continua sendo
O Rio de Janeiro, fevereiro e março
Alô, alô, Realengo
Aquele abraço
Alô torcida do Flamengo
Aquele abraço
Alô, alô, Realengo
Aquele abraço
Alô torcida do Flamengo
Aquele abraço
Chacrinha continua
Balançando a pança
E buzinando a moça
E comandando a massa
E continua dando
As ordens no terreiro
Alô, alô, seu Chacrinha
Velho guerreiro
Alô, alô, Terezinha
Rio de Janeiro
Alô, alô, seu Chacrinha
Velho palhaço
Alô, alô, Terezinha
Aquele abraço
Alô, moça da favela
Aquele abraço
Todo mundo da Portela
Aquele abraço
Todo mês de fevereiro
Aquele passo
Alô Banda de Ipanema
Aquele abraço
Meu caminho pelo mundo
Eu mesmo traço
A Bahia já me deu
Régua e compasso
Quem sabe de mim sou eu
Aquele abraço
Pra você que me esqueceu
Aquele abraço
Alô Rio de Janeiro
Aquele abraço
Todo o povo brasileiro
Aquele abraço
O Rio de Janeiro continua lindo
O Rio de Janeiro continua sendo
O Rio de Janeiro, fevereiro e março
Alô, alô, Realengo
Aquele abraço
Alô torcida do Flamengo
Aquele abraço
Alô, alô, Realengo
Aquele abraço
Alô torcida do Flamengo
Aquele abraço
Chacrinha continua
Balançando a pança
E buzinando a moça
E comandando a massa
E continua dando
As ordens no terreiro
Alô, alô, seu Chacrinha
Velho guerreiro
Alô, alô, Terezinha
Rio de Janeiro
Alô, alô, seu Chacrinha
Velho palhaço
Alô, alô, Terezinha
Aquele abraço
Alô, moça da favela
Aquele abraço
Todo mundo da Portela
Aquele abraço
Todo mês de fevereiro
Aquele passo
Alô Banda de Ipanema
Aquele abraço
Meu caminho pelo mundo
Eu mesmo traço
A Bahia já me deu
Régua e compasso
Quem sabe de mim sou eu
Aquele abraço
Pra você que me esqueceu
Aquele abraço
Alô Rio de Janeiro
Aquele abraço
Todo o povo brasileiro
Aquele abraço
'''

palavras = letra.split()

for palavra in palavras:
    if len(palavra) <= 4:
        for i in range(palavras.count(palavra)):
            palavras.remove(palavra)

unicas = list(set(palavras))

contagem = list()

for palavra in unicas:
    contagem.append([palavras.count(palavra),palavra])

contagem.sort(reverse=True)

top20 = list()

for i in range(20):
    top20.append(contagem[i])

print(top20)


def load():
    global dfontsize,starterx,startery
    dfontsize = 20
    starterx = 100
    startery = 200

def draw_screen(screen):
    global starterx,startery
    screen.fill((255,255,255))

    for item in top20:
        fontsize = int(dfontsize + (1.5*item[0]))
        sys_font = pygame.font.Font(pygame.font.get_default_font(), fontsize)
        t = sys_font.render(item[1], False, random.choice(cores))
        screen.blit(t, t.get_rect(top = starterx, left=startery))
        starterx += 0.75*fontsize
        startery += 0.75*fontsize

def main_loop(screen):
    running = True
    draw_screen(screen)
    pygame.display.update() 
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break


pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()