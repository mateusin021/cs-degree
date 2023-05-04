def cortaString(string):
    arr = string.split(',')
    total = len(arr)
    ini=0
    while total>0:
        print(arr[ini])
        total -=1
        ini +=1
        
cortaString('ovos,leite,pao')