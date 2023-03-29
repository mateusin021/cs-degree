from random import sample

lcores= ['azul','amarelo','verde','rosa','roxo', 'preto', 'marrom','violeta','celeste','magenta','vermelho','laranja','bege','cinza','marfim']

qtd = int(input('tamanho da lista desejada: '))

print(sample(lcores, qtd))