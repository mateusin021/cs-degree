import random
import turtle

t = turtle.Turtle()

cores = ['red','green','blue','yellow','magenta','cyan','pink','gray','black','brown']

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

positions = list()
t.color("orange")
t.goto(0, 0)
for i in range(40):
    t.forward(4*i)
    t.right(30)
    positions.append(t.pos())

positions = positions[::-2]

t.penup()
for i,stat in enumerate(top20):
    t.goto(positions[i])
    t.color(random.choice(cores))
    t.write(stat[1],font=('Arial',int(16+(1.5*stat[0]))))

turtle.done()