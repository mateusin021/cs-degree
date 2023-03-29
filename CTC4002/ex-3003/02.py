dias = int(input('insira o numero de dias: '))
semanas = dias // 7
if dias %7 == 0:
    print(f'{semanas} semanas')
else:
    print(f'{semanas} semanas e {dias%7} dias')