from random import randint

probable_inputs = ["r", "p", "s"]

def game(user):
    comp_input = probable_inputs[randint(0, 2)]
    print comp_input
    if user == comp_input:
        print "You guessed the same as the computer!"
    elif user == "r" and comp_input == "p":
        print "You lost!"
    elif user == "r" and comp_input == "s":
        print "You won!"
    elif user == "p" and comp_input == "r":
        print "You won!"
    elif user == "p" and comp_input == "s":
        print "You lost!"
    elif user == "s" and comp_input == "r":
        print "You lost!"
    elif user == "s" and comp_input == "p":
        print "You won!"

user_input = raw_input("r, p, or s?")

if user_input in probable_inputs:
    game(user_input)
else:
    print "Invalid choice!"
