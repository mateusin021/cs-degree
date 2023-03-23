# -*- coding: UTF-8 -*- 
# Nome completo: Mateus César Mansour de Almeida Soares 
# Matrícula PUC-Rio: 2310555
# Turma: 33P
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim

valor_inicial = float(input('insira o valor inicial da aplicação: '))
rendimento = float(input('insira a porcentagem mensal do rendimento: '))

valor_final = valor_inicial + (valor_inicial*(rendimento/100))

print('valor inicial: %.2f\nvalor final: %.2f'%(valor_inicial,valor_final))