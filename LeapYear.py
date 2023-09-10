year=int(input("Enter The Year : "))

if (year%400==0) and (year%100==0):
    print((f"{year} Is Leap Year!!!"))
elif (year%4==0) and (year%100!=0):
    print((f"{year} Is Leap Year!!!"))
else:
    print(f"{year} Is Not Leap Year!!!")