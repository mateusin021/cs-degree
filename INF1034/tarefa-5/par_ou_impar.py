import random

pontos_comp = 0
pontos_player = 0

for i in range(10):
    jogador = int(input('insira um numero de 0 a 10:'))
    computador = random.randint(0,10)
    total = jogador + computador
    if total%2 ==0:
        print(f'vitoria do computador | jogador: {jogador}, computador: {computador}')
        pontos_comp += 1
    else:
        print(f'vitoria do jogador | jogador: {jogador}, computador: {computador}')
        pontos_player += 1

if pontos_comp > pontos_player:
    print(f'vitoria do computador | {pontos_comp} pontos')
elif pontos_player == pontos_comp:
    print('o jogador e o computador empataram')
else:
    print(f'vitoria do jogador | {pontos_player} pontos')
