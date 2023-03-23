# -*- coding: UTF-8 -*- 
# Nome completo: Mateus César Mansour de Almeida Soares 
# Matrícula PUC-Rio: 2310555
# Turma: 33P
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim
from random import shuffle, sample

inicio = int(input('digite o valor inicial:'))
fim = int(input('digite o valor final:'))

lval_intervalo = list(range(inicio,fim+1))
print(lval_intervalo)

q = int(input('insira o valor de "q": '))

lq = sample(range(q))

print(q)