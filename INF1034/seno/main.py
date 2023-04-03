from math import factorial, radians, sin
def seno(x, termo):
    newx = radians(x)
    atual = 1
    for i in range(1,termo+1):
        
        #print(atual)
        atual+=2
        newx += ((newx**atual)/factorial(atual)) *(-1)
    return newx

print(seno(30,4))
print(sin(radians(30)))