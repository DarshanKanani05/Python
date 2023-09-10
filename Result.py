marks = int(input("Enter Your Marks : "))

if marks > 90:
    print("Excellent!!!")
elif marks <= 90 and marks > 80:
    print("First Class!!!")
elif marks <= 80 and marks > 70:
    print("Second Class!!!")
elif marks <= 70 and marks > 60:
    print("Third Class!!!")
elif marks <= 60 and marks > 50:
    print("Forth Class!!!")
else:
    print("Fail!!!")
