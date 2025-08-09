import math
n = int(input())
if n <= 1:
    print('NO')
else:
    is_prime = 'YES'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = 'NO'
            break
    print(is_prime)