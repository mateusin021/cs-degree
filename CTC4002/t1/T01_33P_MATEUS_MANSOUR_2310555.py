# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:09:49 2023

@author: PC45
"""

# Nome completo: Mateus César Mansour de Almeida Soares
# Matrícula PUC-Rio: 2310555
# Turma: 33P
# Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim.

def celsiusKelvin(tempCelsius):
    return tempCelsius + 273.15

def kelvinFahrenheit(tempKelvin):
    return (tempKelvin - 273.15) * 9/5 + 32

#temp = float(input('insira a temperatura em celsius: '))
temp = 5

print('celsius: %f    kelvin: %f    fahrenheit: %f'%(temp, celsiusKelvin(temp), kelvinFahrenheit(celsiusKelvin(temp))))
