n = input("Enter the number :")
print("*"*len(n))


m = int(input("Enter the triangle style number :"))
for i in range(m+1):
    print(i*"*")


p = int(input("Enter the triangle style number :"))
for j in range(p,0,-1):
    print(j*"*")

q = int(input("Enter the square style number :"))
for l in range(0,q):
    print("*"*q)