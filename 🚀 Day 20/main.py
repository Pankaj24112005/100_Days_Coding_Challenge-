import random

'''
1 for snake
-1 for water
0 for gun

'''
computer=random.choice([-1,0,1])
print("Snake Water Gun Game")
youstr=input("Enter your choice :").lower()
youDict={"snake":1,"water":-1,"gun":0}
reverseDict={1:"snake",-1:"water",0:"gun"}

you=youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"you choose {reverseDict[you]} \ncomputer choose {reverseDict[computer]}")

if(computer==you):
    print("Its Draw")

    
else:
    if(computer==-1 and you==1):
        print("You Winn!")
    
    elif(computer==-1 and you==0):
        print("You Lose!")

    elif(computer==1 and you==-1):
        print("You Lose!")

    elif(computer==1 and you==0):
        print("You Win!")

    elif(computer==0 and you==-1):
        print("you Win!")

    elif(computer==0 and you==1):
        print("You Lose!")

    else:
        print("Something went wrong!")
