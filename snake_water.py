# random module is imported
import random
def game(compter,you):
    if compter==you:
        return None
    elif compter=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif compter=='w':
        if you=='g':
            return False
        elif you=='w':
            return True
    elif compter=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("computer Turn:Snake(s) Or water(w) Or gun(g)...?")
randNo=random.randint(1,3)
if randNo==1:
    computer='s'
elif randNo==2:
    computer='w'
elif randNo==3:
    computer='g'
you=input("player's Turn:snake(S) Or water(W) Or gun(G)...?")
result=game(computer,you)
print(f"You choose {you} ")
print(f"computer choose {computer} \t")
if result==None:
    print("The game Tie!")
elif result==True:
    print("yahooo! you won the game!")
elif result==False:
    print("sorry! you lost the game!")