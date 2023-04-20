def geraForca(palavra):
    forca = {}
    i = 0
    for letra in palavra:
        forca[i] = {"letra": letra,"revealed": False}
        i+=1
    
    return forca

def formataForca(objForca):
    stringForca = ""
    for i in range(len(objForca)):
        if not objForca[i]["revealed"]:
            stringForca += "_ "
        else:
            stringForca += objForca[i]["letra"]
    return stringForca



try:
    palavra = input('insira a palavra: ')
    forca = geraForca(palavra)
    vidas = len(palavra)
    faltantes = len(palavra)
    while faltantes != 0:
        if vidas == 0:
            print('acabaram as tentativas!')
            break
        print(f'{formataForca(forca)} - tentativas sobrando: {vidas}')
        letra = input('> ')
        if letra in palavra:
            for i in range(len(forca)):
                if forca[i]["letra"] == letra:
                    forca[i]["revealed"] =True
                    faltantes -=1

        else:
            vidas -= 1
    print('parabens voce completou a forca!')

except KeyboardInterrupt:
    print('\n[!]saindo...')