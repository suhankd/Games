def mastermind():
    import random
    def get_color():
        while True:
            color = input("Enter a color ranging from:\n\nBlack, White, Orange, Red, Blue, Green, Violet, and Yellow.")
            if color.lower() in ["black","white","orange","red","blue","green","violet","yellow"]:
                return color.lower()
            else:
                print("Please enter a valid color.")
    i = 10
    colors = ["black","white","orange","red","blue","green","violet","yellow"]
    comp_choice1 = random.choice(colors)
    comp_choice2 = random.choice(colors)
    comp_choice3 = random.choice(colors)
    comp_choice4 = random.choice(colors)
    comp_choices = [comp_choice1,comp_choice2,comp_choice3,comp_choice4]
    i = 10
    while i > 0:
        i -= 1
        red_pegs = 0
        white_pegs = 0
        user_choice1 = get_color()
        user_choice2 = get_color()
        user_choice3 = get_color()
        user_choice4 = get_color()

        print("You have chosen the following colors in the given order :\n\n",user_choice1,user_choice2,user_choice3,user_choice4,"\n\n")

        if user_choice1 == comp_choice1:
            red_pegs += 1
        if user_choice2 == comp_choice2:
            red_pegs += 1
        if user_choice3 == comp_choice3:
            red_pegs += 1
        if user_choice4 == comp_choice4:
            red_pegs += 1
        if user_choice1 != comp_choice1 and user_choice1 in comp_choices:
            white_pegs += 1
        if user_choice2 != comp_choice2 and user_choice2 in comp_choices:
            white_pegs += 1
        if user_choice3 != comp_choice3 and user_choice3 in comp_choices:
            white_pegs += 1
        if user_choice4 != comp_choice4 and user_choice4 in comp_choices:
            white_pegs += 1
        print("The computer has placed",white_pegs,"white pegs and",red_pegs,"red peg(s) on the board.")
        print("You have",i,"more turns.")
        if red_pegs == 4:
            print("You have won!")
            break
        elif i == 0:
            print("You have lost.")
            print("The computer had chosen,\n\n",comp_choice1,comp_choice2,comp_choice3,comp_choice4)
            break


mastermind()
