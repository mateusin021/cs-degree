# -*- coding: UTF-8 -*-
# Nome completo: Mateus César Mansour de Almeida Soares
# Matrícula PUC-Rio: 2310555
# Turma: 33P
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim
import math
hipotenusa = int(input('insira o valor de x: '))
teta = int(input('insira o valor do angulo teta: '))

seno = math.sin(math.radians(teta))
altura = round(seno,1) * hipotenusa

print('altura da rampa: %d'%(altura))
