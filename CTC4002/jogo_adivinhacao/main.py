lista = [[],[],[],[],[],[]]
soma = 0

def geraCartelas():
    iniciais = [1, 2, 4, 8, 16, 32]
    
    for i in range(1, 64):
        for j in range(6):
            if i & iniciais[j]:
                lista[j].append(i)

def exibeCartela(lista):
    ind = 0
    for i in range(4):
        for j in range(8):
            print(f'{lista[ind]: >2}', end=' ')
            ind+=1
        print("\n", end="")

def exibeMensagemInicial():
    print("""
    *************************************************************
    *                    Jogo da adivinhação                    * 
    *   Pense em um inteiro de 1 a 63 e não conte pra ninguém!  * 
    *   Em seguida, tecle ENTER para continuar... e boa sorte!  * 
    *                                                           * 
    *************************************************************""")

exibeMensagemInicial()
geraCartelas()

for indice, subl in enumerate(lista):
    print(f'cartela {indice+1}')
    exibeCartela(subl)
    opcao = input('o numero escolhido esta na cartela? (s/n) ')
    if opcao == 's':
        soma += subl[0]

print(f'o valor escolhido foi............. {soma}!!!!!!!')
