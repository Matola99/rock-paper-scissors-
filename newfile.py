#create a lists of players options
t=[" rock" ,"paper" ,"scissors"]
#assign a random play to the computer
computer = t[randint (0.2)]
#set player to false
player = false
while player == false:
    #set player to true
    player = input (" rock, paper, scissors ")
    if player == computer:
        print (" tie")
        elif player == "rock":
            if computer == "paper":
                print("you lose!", computer,"cover", player)
                else:
                    print(" you win!", player, "smashes", computer)
                    elif player == "paper":
                        if computer == "scissors":
                            print("you lose"!, computer,"cut",player)
                            else:
                                print("you win"!, player "cover",computer)
                                elif player == "scissors":
                                if computer == "rock":
                                    print ( "you lose"!,computer, " smashes" ,player)
                                    else:
                                        print(" you win"!, player, "cut" , computer)
                                        else:
                                            print (" that's not  valid play, check your spelling!")
                                    #player was set to true but we want it to be false so the loop continues 
                                    player = false
                                    computer = t[randint(0.2)]













