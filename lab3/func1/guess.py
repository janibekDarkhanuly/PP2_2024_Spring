import random
def game():
    x = (random.randint(1,20))
    print("Hello!What is your name?")
    name = input()
    sum = 0
    print("Well",name,"I am thinking of a number between 1 and 20",'\n' "Take a guess.")
    while(True):
        guess = int(input())
        if(guess<x):
            print("Your guess is too low",'\n' "Take a guess")
            sum+=1
        elif(guess>x):
            print("Your guess is too high",'\n',"Take a guess")
            sum+=1

        elif(guess == x):
            print("Good job,",name,"You guessed my number in",sum+1,"guesses!")
            break
while(True):
    print("Do you want to play the game?",'\n' "Y/N")
    x = input()
    x.lower()
    if(x == "y"):
        game()
        break
    elif x == "n":
        break
    elif x!="y" and x!="n":
        print("invalid answer")
    
