fam = int(input('insira o numero de conveniados na familia: '))
soma = 100
totFam = fam
inicio = 1
while fam > 0:
    idade = int(input(f'insira a idade do conveniado {inicio}: '))
    if idade <=10:
        soma +=80
    elif idade <40:
        soma += 50
    elif idade <60:
        soma += 95
    else:
        soma += 130
    fam -=1
    inicio +=1
    
print(f'''
      total de pessoas na familia: {totFam}
      total a ser pago: {soma}
      ''')