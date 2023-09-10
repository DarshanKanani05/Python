sub1 = int(input("Enter Marks Of Subject 1 : "))
sub2 = int(input("Enter Marks Of Subject 2 : "))
sub3 = int(input("Enter Marks Of Subject 3 : "))

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You Are Fail!!!")
elif (sub1+sub2+sub3)/3 < 40:
    print("You Are Fail!!!")
else:
    print("You Are Pass...")
