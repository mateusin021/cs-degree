# -*- coding: UTF-8 -*- 
# Nome completo: Mateus César Mansour de Almeida Soares 
# Matrícula PUC-Rio: 2310555
# Turma: 33P
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim
lmeses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
nome = input('insira o nome: ')
data = input('insira a data de nascimento: ')

mes = int(data[3:5])

print('%s nasceu no mes %s'%(nome, lmeses[mes-1]))