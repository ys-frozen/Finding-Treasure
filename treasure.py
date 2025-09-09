a=input("welcome to Treasure land\nThere are two ways to find the treasure right or left you have to choose one way\n").lower()
if(a=='right'):
    print("GAME OVER\n You have fell in lava try again next time")
else:
    b=input("You see a big lake there is boat which come to the edge of the lake and go to the other edge.\n Do you wait or swim \n").lower()
    if(b=='swim'):
        print("GAME OVER \n You have killed by crocodile in the lake try again next time")
    else:
        c=input("you have reached to the other end of the lake and you see three doors white,black and grey you have to choose one door only\n").lower()
        if(c=='black'):
            print("GAME OVER\n you have killed by snakes try again later")
        elif(c=='grey'):
            print("GAME OVER\n you have killed by arrows try again later")
        else:
            print("congratulations you have found treasure \n        you will     \n")
    