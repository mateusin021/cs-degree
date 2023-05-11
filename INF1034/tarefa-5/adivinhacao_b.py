import random 

def checaNumero(tentativa, numero):
    if numero < tentativa:
        return -1
    elif numero > tentativa:
        return 1
    else:
        return 0

def main():
    player = int(input(
"""
quem ira jogar?
0) jogador
1) robo
    
> """))
    if player ==0:
        tentativas = 0

        numero = random.randint(1,1024)
        while True:
            tentativa = int(input('> '))
            if numero < tentativa:
                print(-1)
                tentativas += 1
            elif numero > tentativa:
                print(1)
                tentativas += 1
            else:
                print(f'numero correto! tentativas: {tentativas}')
                break
    else:
        tentativas= 0
        numero = int(input('insira o numero para o robo adivinhar: '))
        tentativa_robo = 1024
        while(checaNumero(tentativa_robo, numero))!= 1:
            tentativa_robo = int(tentativa_robo/2)
            tentativas +=1
        while(checaNumero(tentativa_robo, numero)) == 1:
            tentativa_robo = tentativa_robo+10
            tentativas +=1
        while(checaNumero(tentativa_robo, numero)) != 1:
            tentativa_robo = tentativa_robo-2
            tentativas +=1
        while(checaNumero(tentativa_robo, numero)) != 0:
            tentativa_robo = tentativa_robo+1
            tentativas +=1
        print(f'o numero correto e: {tentativa_robo} | tentativas: {tentativas}')
main()