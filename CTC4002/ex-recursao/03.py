def contatq(num):
    if num <10:
        if num == 3 or num ==4:
            return 1
        return 0
    if num%10 ==3 or num%10 == 4:
        return 1+ contatq(num//10)
    return contatq(num//10)

print(contatq(31234))
