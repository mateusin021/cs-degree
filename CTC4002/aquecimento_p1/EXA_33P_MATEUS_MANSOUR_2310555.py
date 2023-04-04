#nome: Mateus Cesar Mansour de Almeida Soares
#mat: CTC4002
#turma: 33P
#prof: Joisa
#declaro que fiz esse exercicio sozinho 

def representacao_horario(segs):
    horas = segs//3600
    minutos = int(segs%3600//60)
    segundos = int(segs%60)
    return f'{horas:02d}h:{minutos:02d}m:{segundos:02d}s'
segundos = int(input('insira os segundos:'))
print(representacao_horario(segundos))
