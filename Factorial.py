def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


num = int(input("Enter The Number : "))

print(f"The Factorial Of {num} Is {factorial(num)}.")
