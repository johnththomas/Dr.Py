import random

number = random.randint(1,10)
guess = 0
while guess != number:

    guess = int(input("Enter Guess: "))

    if (guess < number):
        print("Unlucky, guess heigher!")
    elif (guess > number):
        print("Unlucky, guess lower!" )
    else:
        print("Halalouuuya!\n You wone!")
        