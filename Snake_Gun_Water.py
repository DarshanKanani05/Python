import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer's Turn (Snake(s) Water(w) Or Gun(g)) : ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn (Snake(s) Water(w) Or Gun(g)) : ")

result = gameWin(comp, you)

print(f"Computer's Choice : {comp}")
print(f"Your Choice : {you}")

if result == None:
    print("Game Is Tie!!!")
elif result == True:
    print("You Win!!!")
else:
    print("You Lose!!!")
