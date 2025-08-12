n = input()
arr = list(n)
arr2 =arr.reverse()
print(''.join(arr))
if arr2[0]=='0':
    arr2.remove('0')
print(''.join(arr))
if n == ''.join(arr):
    print('YES')
else:
    print('NO')