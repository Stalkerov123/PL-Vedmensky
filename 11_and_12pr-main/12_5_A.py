def r(x):
    if x == 0:
        return 0 
    else:
        print(x % 10)
        r(x // 10)

x = int(input())
r(x)

    


