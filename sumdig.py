n = input("Enter the number you want to process :")
i = 0
sum = 0
mul = 1
for i in range(len(n)):
    m =int(n[i])
    sum += m
    mul = mul *m
print(f"The sum of the given number digits is {sum}")
print(f"The multiplication of the given number digits is {mul}")

#do this with no type casting