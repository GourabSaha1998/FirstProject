# Enter a number to check your guess is write or wrong #
import random

print("\t\t................................WELCOME TO THE GUESSING GAME................................")
print("\t\t  Var: 1.4.0")
print("\t\t  Release date: 21th June,2020")
print("\t\t  Designed and Developed by creation.com")
print("\t\t  Check your guessing power.....")
print("\t\t  You have maximum 5 chances to guess correct number")
print("\t\t  Hint: Sherlock said,\"My dear Watson most of the children enter high school in 10 years.\"")

print("Enter your name")
name1 = input()
name = name1.strip()
print("Hi", name.title(), end=" ")

print("enter your guess")  # Enter some number

guess = int(input())
exact_number = random.randint(1, 10)
i = 1
while i < 5:  # While loop

    if guess == exact_number:  # The correct number
        print("Well done", name.title(), "you win the game.....")

        print("Your guess is correct in", i, "chance")
        break
    else:
        if exact_number > guess >= exact_number - 2:
            print("You are too close")  # Guess again
            print("The exact number is ", exact_number)

            print("You have", 5 - i, "chances left ")
            print("................................")

        elif exact_number + 2 >= guess > exact_number:
            print("You are too close")  # Re-guess
            print("The exact number is ", exact_number)

            print("You have", 5 - i, "chances left ")
            print("................................")

        elif guess <= exact_number - 3:
            print("You guess a very small number")  # For re-guess
            print("The exact number is ", exact_number)

            print("You have", 5 - i, "chances left ")
            print("................................")

        else:
            print("You guess a very large number")  # For re-guess
            print("The exact number is ", exact_number)

            print("You have", 5 - i, "chances left ")
            print("................................")

    print("Are you interested?(Yes/No)")  # For the interest of the player in the game
    ans_ = input()
    ans = ans_.strip()
    print("................................")
    if ans.lower() == "no":
        print("Thank you for playing.....")
        break
    elif ans.lower() == "yes":
        print("Re-enter your guess")  # Re-entering the game
        guess = int(input())
        exact_number = random.randint(1, 10)
    else:
        print("Please enter Yes or No")
        print("Play from the beginning.....")
        break
    i = i + 1  # While loop increment
    if i == 5:  # For the last chance of guess
        if guess == exact_number:  # The exact number
            print("You win the game")

            print("Your guess is right in", i, "chances")

        elif exact_number > guess >= exact_number - 2:  # Out of chance
            print("You are too close")

            print("Sorry", name.title(), "you have", 5 - i, "chances left ")
            print("The exact number is ", exact_number)

            print("Game over!")

        elif exact_number + 2 >= guess > exact_number:  # Out of chance
            print("You are too close")

            print("Sorry", name.title(), "you have", 5 - i, "chances left ")
            print("The exact number is ", exact_number)

            print("Game over!")

        elif guess <= exact_number - 3:  # Out of chance
            print("You guess a very small number")

            print("Sorry", name.title(), "you have", 5 - i, "chances left ")
            print("The exact number is ", exact_number)

            print("Game over!")

        else:  # Out of chance
            print("You guess a very large number")

            print("Sorry", name.title(), "You have", 5 - i, "chances left ")
            print("The exact number is ", exact_number)

            print("Game over!")
print("Thank you for playing...")
