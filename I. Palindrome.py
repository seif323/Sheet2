# Read input as string to avoid integer issues
n = input().strip()
# Reverse and remove leading zeros using int()
reversed_no_leading = str(int(n[::-1]))
print(reversed_no_leading)
# Check palindrome
if n == n[::-1]:
    print("YES")
else:
    print("NO")
