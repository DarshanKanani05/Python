Dictionary={
    "English":"Hello",
    "Hindi":"Nameste",
    "Spanish": "Hola",
    "French": "Bonjour",
    "Japanese": "Konnichiwa",
}

print("Choice : ",Dictionary.keys())

a=input("Enter Your Choice : ")

print("Hello In",a,": ",Dictionary.get(a))