latter = '''Dear <|NAME|>
You Are Selected!!

Date : <|DATE|>
'''

name = input("Enter Your Name : ")
date = input("Enter Date : ")

latter = latter.replace("<|NAME|>", name)
latter = latter.replace("<|DATE|>", date)

print(latter)
