import random 

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
