def criscrosb(xaxis,yaxis):
    print(f"{'X' if xaxis[0] else ('O' if yaxis[0] else 0)} | {'X' if xaxis[1] else ('O' if yaxis[1] else 1)} | {'X' if xaxis[2] else ('O' if yaxis[2] else 2)} ")
    print(f"--|---|---")
    print(f"{'X' if xaxis[3] else ('O' if yaxis[3] else 3)} | {'X' if xaxis[4] else ('O' if yaxis[4] else 4)} | {'X' if xaxis[5] else ('O' if yaxis[5] else 5)}")
    print(f"--|---|---")
    print(f"{'X' if xaxis[6] else ('O' if yaxis[6] else 6)} | {'X' if xaxis[7] else ('O' if yaxis[7] else 7)} | {'X' if xaxis[8] else ('O' if yaxis[8] else 8)} ")
    print(f"--|---|---")
def add(a,b,c):
    return a+b+c
def wins(xaxis,yaxis):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,7]]
    for win in wins:
      if add(xaxis[win[0]],xaxis[win[1]],xaxis[win[2]])==3:
        print("X wins the match.")
        return 1
      if add(yaxis[win[0]],yaxis[win[1]],yaxis[win[2]])==3:
        print("Y wins the match.")
        return 0
    return -1
if __name__=="__main__":
    xaxis=[0,0,0,0,0,0,0,0,0,0]
    yaxis=[0,0,0,0,0,0,0,0,0,0]
    chance = 1
    print("Welcome to TIC TAC TOE")
    while(True):
          criscrosb(xaxis,yaxis)
          if(chance == 1):
              print("Its X's chance")
              value=int(input("Enter a value: "))
              xaxis[value]=1
          else:
              print("Its Y's chance")
              value=int(input("Enter a value: "))
              yaxis[value]=1
          winner= wins(xaxis,yaxis)
          if(winner!=-1):
              print("Match over.")
              break
          chance= 1-chance
          