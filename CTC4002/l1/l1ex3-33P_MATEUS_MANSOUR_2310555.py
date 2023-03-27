# -*- coding: UTF-8 -*- 
# Nome completo: Mateus César Mansour de Almeida Soares 
# Matrícula PUC-Rio: 2310555
# Turma: 33P
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim
p = float(input('insira o capital inicial: '))
i = float(input('insira a taxa de juros mensal: '))
n = int(input('insira a quantidade de meses: '))

capital_final = float(p * ((1+i/100)**n))

print('para o capital inicial de R$%.2f, com taxa de %.2f%s ao mes, apos %d meses, teremos o capital final de R$%.2f'%(p,i,"%",n,capital_final))
