n = input("Enter the number :")
n = n[::-1]
print(n)


def exchange(m):
    y = m[-1]+m[1:-1]+m[0]
    return y


num = input("Enter the number :")
print("The output number is {}".format(exchange(num)))