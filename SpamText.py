text = input("Enter Your Text : ")

spam = False

if ("Make A Lot Of Money" in text):
    spam = True
elif ("Buy Now" in text):
    spam = True
elif ("Subscribe This" in text):
    spam = True
elif ("Click This" in text):
    spam = True
else:
    spam = False

if (spam is True):
    print("Your Massage Is Spam!!!")
else:
    print("Your Massage Is Not Spam!!!")
