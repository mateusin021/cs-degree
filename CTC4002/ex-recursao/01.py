def produto(a,b):
    if a == 0 or b ==0:
        return 0
    return a+ produto(a,b-1)

print(produto(4,2))
