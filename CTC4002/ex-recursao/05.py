def iplr(num):
    if num< 10:
        print(num)
        return
    print(num%10)
    iplr(num//10)

iplr(1337)
