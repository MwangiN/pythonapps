
import random
import emoji #imports emoji

print(emoji.emojize("Welcome to the :game_die: Dice Simulator :nerd_face::nerd_face::nerd_face:"))

x="y"

while x == "y":
    number=random.randint(1,6) #should be inside the loop
    if number==1:
        print(emoji.emojize(":green_circle:"))
    elif number==2:
        print(emoji.emojize(":green_circle::orange_circle:"))
    elif number==3:
        print(emoji.emojize(":green_circle::orange_circle::blue_circle:"))
    elif number==4:
        print(emoji.emojize(":green_circle::orange_circle::blue_circle::yellow_circle:"))
    elif number==5:
        print(emoji.emojize(":green_circle::orange_circle::blue_circle::yellow_circle::purple_circle:"))
    elif number==6:
        print(emoji.emojize(":green_circle::orange_circle::blue_circle::yellow_circle::purple_circle::brown_circle:"))
    
    x = input(emoji.emojize("press y to roll again :gear: or press any other letter to stop :stop_sign: "))



