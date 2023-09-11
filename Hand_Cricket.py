# Hand Cricket
def handcricket():
    import random
    def get_int():
        while True:
            try:
                n = int(input("Please enter a number between 0 and 10."))
                if n > 10 or n < 0:
                    print("Enter a valid input.")
                else:
                    return n
            except ValueError:
                print("Invalid input. Please input an integer.")
    def get_nature():
        while True:
            z = input("What's the nature of the sum?")
            if z.lower() in ["odd","even"]:
                return z
            else:
                print("Invalid input. Please try again.")
    def toss():
            x = get_int()
            z = get_nature()
            y = random.randint(0,10)
            print("You chose",x,"and the computer chose",y,". The nature of the sum was chosen to be",z)

            if (x+y)%2 == 0 and z.lower() == "even" :
                print("You have won the toss!")
                return True
            elif (x+y)%2 != 0 and z.lower() == "odd":
                print("You have won the toss!")
                return True
            else:
                print("You have lost the toss!")
                return False
    def batting():
            print("You are batting.")
            total = 0
            while True:
                x = get_int()
                y = random.randint(0,10)
                print("You have chosen",x,"and the computer has chosen",y,".")
                if x != y:
                    total += x
                    print("Your score is",total)
                elif x == y:
                    print("Out! Your score is",total)
                    return total
    def bowling():
            print("You are bowling.")
            total = 0
            while True:
                x = get_int()
                y = random.randint(0,10)
                print("You have chosen",x,"and the computer has chosen",y,".")
                if x != y:
                    total += y
                    print("The computer's score is",total)
                elif x == y:
                    print("Out! The computer's score is",total)
                    return total
    def batorbowl():
        while True:
                choice = input("Congratulations! You have won the toss. Would you like to bat or bowl?")
                if choice.lower() in ["bat","bowl"]:
                    return choice
                else:
                    print("Invalid input. Please try again.")
    toss_bool = toss()
    if toss_bool == True:
       player_choice = batorbowl()
       if player_choice == "bowl":
           comp_score = bowling()
           print("The computer scored",comp_score,"points. You need to score",(comp_score+1),"points to win!")
           player_score = batting()
           print("You scored",player_score,"points and the computer scored",comp_score,"points.")
           if player_score > comp_score:
               print("You win!")
           elif player_score < comp_score:
               print("You lose!")
           else:
               print("It's a tie!")
       elif player_choice == "bat":
           player_score = batting()
           print("You scored",player_score,"points! The computer needs",(player_score+1),"points to win!")
           comp_score = bowling()
           print("The computer scored",comp_score,"points!")
           if player_score > comp_score:
               print("You win!")
           elif comp_score > player_score:
               print("You lose!")
           else:
               print("It's a tie!")
    elif toss_bool == False:
        choices = ["bowl","bat"]
        comp_choice = random.choice(choices)
        if comp_choice == "bowl":
            print("The computer has chosen to bat.")
            comp_score = bowling()
            print("The computer's score is",comp_score,". You need a score of",(comp_score+1),"to win!")
            player_score = batting()
            print("The computer scored",comp_score,"points and you scored",player_score,"points.")
            if comp_score > player_score:
                print("You lose!")
            elif player_score > comp_score:
                print("You win!")
            else:
                print("It's a tie!")
        if comp_choice == "bat":
            print("The computer has chosen to bowl.")
            player_score = batting()
            print("You scored",player_score,"points! The computer needs",(player_score+1),"points to win!")
            comp_score = bowling()
            print("The computer scored",comp_score,"points!")
            if player_score > comp_score:
               print("You win!")
            elif comp_score > player_score:
               print("You lose!")
            else:
               print("It's a tie!")


handcricket()


        


            
    





        
