lista = []

# diminui de 20 pra 5 pra facilitar o teste
for i in range(5):
    num = int(input('insira o numero da chamada: '))
    nota = int(input('insira a nota: '))
    lista.append([num,nota])

stats = []
for i in range(0,11):
    qtd = 0
    for aluno in lista:
        if i == aluno[1]:
            qtd+=1
    stats.append(qtd)

print('tabela das notas: ')
for i in range(0,11):
    print(f'notas {i}: {"*"*stats[i]}')