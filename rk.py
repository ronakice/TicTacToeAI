import sys
board=[["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

def drawBoard1():
    """
    Draws the Board
    """
    print("")
    for row in board:
        for x in row:
            sys.stdout.write(x+"   ")
        print("")
def drawBoard2(baa):
    """
    Draws the intermediate Board
    """
    print("")
    for row in board:
        for x in row:
            sys.stdout.write(x+"   ")
        print("")
def checkwin(baa):
    """
    Checks to see if anyone has won
    """
    
    if baa[0][0]==baa[0][1] and baa[0][0]==baa[0][2] and baa[0][0]=="X":
        return 100
    elif baa[0][0]==baa[0][1] and baa[0][0]==baa[0][2] and baa[0][0]=="O":
        return -100
    elif baa[1][0]==baa[1][1] and baa[1][0]==baa[1][2] and baa[1][0]=="X":
        return 100
    elif baa[1][0]==baa[1][1] and baa[1][0]==baa[1][2] and baa[1][0]=="O":
        return -100
    elif baa[2][0]==baa[2][1] and baa[2][0]==baa[2][2] and baa[2][0]=="X":
        return 100
    elif baa[2][0]==baa[2][1] and baa[2][0]==baa[2][2] and baa[2][0]=="O":
        return -100
    elif baa[0][0]==baa[1][0] and baa[1][0]==baa[2][0] and baa[0][0]=="X":
        return 100
    elif baa[0][0]==baa[1][0] and baa[1][0]==baa[2][0] and baa[0][0]=="O":
        return -100
    elif baa[0][1]==baa[1][1] and baa[1][1]==baa[2][1] and baa[1][1]=="X":
        return 100
    elif baa[0][1]==baa[1][1] and baa[1][1]==baa[2][1] and baa[1][1]=="O":
        return -100
    elif baa[0][2]==baa[1][2] and baa[1][2]==baa[2][2] and baa[2][2]=="X":
        return 100
    elif baa[0][2]==baa[1][2] and baa[1][2]==baa[2][2] and baa[2][2]=="O":
        return -100
    elif baa[0][0]==baa[1][1] and baa[0][0]==baa[2][2] and baa[0][0]=="X":
        return 100
    elif baa[0][0]==baa[1][1] and baa[0][0]==baa[2][2] and baa[0][0]=="O":
        return -100
    elif baa[2][0]==baa[1][1] and baa[2][0]==baa[0][2] and baa[2][0]=="X":
        return 100
    elif baa[2][0]==baa[1][1] and baa[2][0]==baa[0][2] and baa[2][0]=="O":
        return -100
    else:
        return 0
def FullBoard(x):
    """
    Checks to see if the board is full
    """
    for i in x:
        for t in i:
            if t in "123456789":
                return False
    return True
def minimax(baa,level):
    """
    Minimax is an implementation of the MINIMAX algorithm on the game of TIC TAC TOE
    """
    if(checkwin(baa)==100):
        return 100
    elif(checkwin(baa)==-100):
        return -100
    else:
        if FullBoard(baa):
            return 0
        else:
            a=[]
            b=[]
            for i in range(0,3):
                for j in range(0,3):
                    #print a
                    if baa[i][j] in "123456789":
                        t=baa[:]
                        #print level
                        if level%2==0 and choice==1:
                            t[i][j]="O"
                        elif level%2==0 and choice==2:
                            t[i][j]="X"
                        elif level%2==1 and choice==1:
                            t[i][j]="X"
                        else:
                            t[i][j]="O"
                        a.append(minimax(t,level+1))
                        if(level==0):
                            baa[i][j]=str(i*3 + j + 1)
                            b.append(int(baa[i][j]))
                        baa[i][j]=str(i*3 + j + 1)
            if(level==0 and choice==1):     
              
                c=b[0]
                t=a[0]
                for i in range(0, len(a)):
                    if a[i]<a[0]:
                        c=b[i]
                        t=a[i]
                return c
            elif(level==0 and choice==2):
        
                c=b[0]
                t=a[0]
                for i in range(0, len(a)):
                    if a[i]>a[0]:
                        c=b[i]
                        t=a[i]
                return c
            else:
                if((level%2==0 and choice==1) or(level%2==1 and choice==2)):
                    return min(a)
                else:
                    return max(a)          
movecount=0
choice=0
def StartGame():
    """
    MAIN FUNCTION
    """
    global choice
    print "Welcome to this game of tic tac toe vs the computer. Prepare to lose or draw."
    movecount=0
    choice=int(raw_input("Choose if you want to be player 1 or player 2(1-2): "))
    while movecount<=8:
        if ((movecount%2)+1)==choice:
            drawBoard1()
            while 1==1:
                movec = raw_input("Make a move mate! ")
                if movec not in "123456789" or movec=="":
                    print "Choose an integer between 1-9!"
                else:
                    movec=int(movec)
                    if str(movec)!=board[(movec-1)/3][(movec-1)%3]:
                        print "Spot taken,choose another. "
                    else:
                        if(choice==1):
                            board[(movec-1)/3][(movec-1)%3]='X'
                        else:
                            board[(movec-1)/3][(movec-1)%3]='O'
                        break
        else:
            c=minimax(board,0)
            if choice==1:
                board[(c-1)/3][(c-1)%3]='O'
            else:
                board[(c-1)/3][(c-1)%3]='X'
        movecount=movecount+1
        if(checkwin(board)==100 and choice==1):  
            drawBoard1()
            print "You win!"
            break
        elif (checkwin(board)==-100 and choice==1):
            drawBoard1()
            print "You lose!"
            break
        elif(checkwin(board)==100 and choice==2):  
            drawBoard1()
            print "You lose!"
            break
        elif (checkwin(board)==-100 and choice==2):
            drawBoard1()
            print "You win!"
            break
        elif (FullBoard(board)):
            drawBoard1()
            print "Draw!"
            break
StartGame()
