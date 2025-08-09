for i in range(int(input())):
    n = int(input())
    fact = 1
    for fac in range(1, n+1):
        fact *= fac
    print(fact) 