def calcula(a,b,op):
    if op == "+":
        return a+b
    elif op =="-":
        return a-b
    elif op =="*":
        return a*b
    elif op =="/":
        return a/b
    elif op =="%":
        return a%b
    elif op =="^":
        return a**b
    
a = float(input('insira o primeiro valor: '))
b = float(input('insira o segundo valor: '))
op = input('insira o operador: ')
print(f'resultado: {calcula(a,b,op)}')