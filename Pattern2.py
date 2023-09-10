x = int(input("Enter The Value : "))

for i in range(x):
    print("  " * (x-i-1), end="")
    print("* " * (2*i+1), end="")
    print("  " * (x-i-1))
