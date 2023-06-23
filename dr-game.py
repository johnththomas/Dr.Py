import random

number = random.randint(1,10)
guess = 0
while guess != number:

    guess = int(input("Enter Guess: "))

    if (guess < number):
        print("Unlucky, guess heigher!\nReach DR.py2 to fix your luck hhh" )
    elif (guess > number):
        print("Unlucky, guess lower!\nReach DR.py2 to fix your luck hhh" )
    else:
        print("Halalouuuya!\n You wone!")
        