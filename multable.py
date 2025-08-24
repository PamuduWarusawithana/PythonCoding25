n = int(input("What number do you want to get multiplication table :"))
i = 1
for i in range(1,51):
    print("{} * {} = {}".format(i,n,i*n))