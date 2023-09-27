print("Welcome to Treasure Island")
side = input("Which side do you hope for luck with, choose left or right ").lower()
if side == "left":
    genious = input("You are at the lake would you like to swim or wait for a boot ").lower()
    if genious == "wait":
        color = input("You have reached the treasure house and there are three doors one blue,\nanother yellow and the last one is red choose a door basing on a color \n").lower()
        if color == "blue":
            print("You opened a door of bees game over")
        if color == "yellow":
            print("You won coz you have found your soulmate")
        elif color == "red":
            print("You opened a door with ladies game over")
    else:
        print("You drowned in the middle of the lake, game over")
else:
    print("You feel into a hole game over")