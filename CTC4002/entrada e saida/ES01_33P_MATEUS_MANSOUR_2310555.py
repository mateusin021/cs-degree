# -*- coding: UTF-8 -*- 
# Nome completo: Mateus César Mansour de Almeida Soares 
# Matrícula PUC-Rio: 2310555
# Turma: 33P
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim

n = int(input('numero de latas de tinta: '))
capacidade_engradados = int((input('numero de latas que cabem no engradado: ')))
preco_engradado = float(input('preço do engradado: '))

if n%capacidade_engradados != 0:
    numero_engradados = n//capacidade_engradados + 1
else:
    numero_engradados = n//capacidade_engradados
preco_total = preco_engradado*numero_engradados

print('serão transportadas %d latas em %d engradados que terão o valor de %.2f'%(n,numero_engradados,preco_total))
