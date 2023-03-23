# -*- coding: UTF-8 -*- 
# Nome completo: Mateus César Mansour de Almeida Soares 
# Matrícula PUC-Rio: 2310555
# Turma: 33P
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim

nome_candidato = input('insira o nome do candidato:')
nota1 = float(input('insira a nota prova: '))
nota2 = float(input('insira a nota de curriculo: '))
nota3 = float(input('insira a nota entrevista: '))

nota_final = (nota1 * 3 + nota2* 2 + nota3 *1)/6

print('nome do candidato: %s\nnota final: %.1f'%(nome_candidato,nota_final))
