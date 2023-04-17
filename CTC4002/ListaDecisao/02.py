def umidade(nivel):
    if nivel <=100 and nivel >=60:
        return "nivel adequado"
    elif nivel <60 and nivel >30:
        return "nivel inadequado para a saude humana"
    elif nivel <=30 and nivel >20:
        return "estado de atencao"
    elif nivel <=20 and nivel >12:
        return "estado de alerta"
    else:
        return "emergencia"
    
nivel = input('insira a umidade relativa: ')
print(umidade(nivel))

# print(umidade(100))
# print(umidade(59))
# print(umidade(60))
# print(umidade(30))
# print(umidade(25))
# print(umidade(10))