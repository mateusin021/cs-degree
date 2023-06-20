def carregaRanking():
    global ranking
    ranking = []
    with open('ranking.txt','r') as lista:
        for line in lista:
            ranking.append(line.strip())

def imprimeRanking():
    for i,content in enumerate(ranking):
        print(f'{i+1}º lugar: {content}')

def atualizaRanking():
    with open('partidas.txt', 'r') as partidas:
        for linha in partidas:
            linha = linha.strip().split(',')
            if int(linha[1]) > int(linha[3]):
                venc = linha[0]
                perd = linha[2]
            else:
                venc = linha[2]
                perd = linha [0]
            posperd=ranking.index(perd)
            posvenc=ranking.index(venc)
            if posperd < posvenc:
                ranking.pop(posvenc)
                ranking.insert(posperd,venc)

carregaRanking()
print('***antes da atualizacao***')
imprimeRanking()
atualizaRanking()
print('***depois da atualizacao***')
imprimeRanking()