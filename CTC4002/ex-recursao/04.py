def ipl(num):
    if num < 10:
        print(num)
        return
    print(num//10)
    ipl(num%10)

ipl(137)
