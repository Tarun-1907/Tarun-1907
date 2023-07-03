import random

def snakegame():
 computer=random.randint(0,2)
 you=int(input("0 for snake 1 for water and 2 for gun, enter your choice: "))
 if(you<0 or you>2):
    raise ValueError ("Wrong value!! please input a correct value")
 
 def check(computer,you):
    if computer==you:
        return 0
        
    if computer==0 and you==1: return -1
    if computer==1 and you==2: return -1
    if computer==2 and you==0: return -1
   
    else: return 1

 print("You: ",you)
 print("Computer: ",computer)

 score=check(computer, you)
 if(score==-1):
   print("Computer wins")
 elif(score==1):
   print("You win")
 else:
   print("It's a draw")
        
for i in range (2):
 play=str(input("Do you want to play ? yes or no: "))
 if(play=='yes'):
     snakegame()
 elif(play=='no'):
    print("OK! Maybe another day !!")
    break
 else:
    raise ValueError("Input only yes or no !!")   