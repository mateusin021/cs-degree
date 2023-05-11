import random

opcoes = ['pedra', 'papel', 'tesoura']

print("""
    escolha uma opcao:
    1) pedra
    2) papel
    3) tesoura
        """)
jogador = int(input("> ")) 
computador = random.choice(opcoes)
print(f"jogador: {opcoes[jogador - 1]} VS computador: {computador}")

if opcoes[jogador-1] == computador:
    print('empate!!')
elif opcoes[jogador-1] == 'pedra':
    if computador == "tesoura":
        print('vitoria do jogador')
    else:
        print('vitoria do computador')
elif opcoes[jogador-1] == 'papel':
    if computador == "pedra":
        print('vitoria do jogador')
    else:
        print('vitoria do computador')
elif opcoes[jogador-1] == 'tesoura':
    if computador == "papel":
        print('vitoria do jogador')
    else:
        print('vitoria do computador')
