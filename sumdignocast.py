n = 12345
if n!=0:
    sum = 0
    mul = 1
    for i in range(5):
        m=n%10
        n=n//10
        sum += m
        mul = mul*m
else:
    sum = 0
    mul = 0
print(f"sum is {sum} and multiplication is {mul}")