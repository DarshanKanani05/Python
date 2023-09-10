n1 = int(input("Enter The Number 1 : "))
n2 = int(input("Enter The Number 2 : "))
n3 = int(input("Enter The Number 3 : "))
n4 = int(input("Enter The Number 4 : "))

if (n1 > n2):
    f1 = n1
else:
    f1 = n2

if (n3 > n4):
    f2 = n3
else:
    f2 = n4

if (f1 > f2):
    print(f1, "Is Big Number.")
else:
    print(f2, "Is Big Number.")
