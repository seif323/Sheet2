# Even: 3
# Odd: 2
# Positive: 1
# Negative: 3

n = int(input())
nums = []*n;nums = map(int, input().split());even = 0;odd = 0;pos = 0;neg = 0
for i in nums:
    if i%2 == 0:
        even +=1
    else:
        odd += 1
    if i>0:
        pos += 1
    elif i<0:
        neg += 1

print(f"Even: {even}\nOdd: {odd}\nPositive: {pos}\nNegative: {neg}")