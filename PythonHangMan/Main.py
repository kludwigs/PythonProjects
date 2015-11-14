import startprompt
import wordlist
import validateguess
import sys

print("Welcome to Karl's hang man game")
print("Would you like to play?")

answer = raw_input("Type y or n and hit 'Enter'.\n").lower()

action = startprompt.hangmanstartprompt(answer)

if action is True:
    print("Okay let's get going")
else:
    sys.exit()

# save the word and an array with the same length    
theword = wordlist.getwordlistfromfile("wordlist.txt")
theword = theword.rstrip()
thewordcopy = "-" * len(theword)
number_of_characters = len(theword)
print("Okay the word has ", number_of_characters, " characters")

number_of_guesses = 8

print("Enter a letter to begin guessing. You'll start with ", number_of_guesses, " guesses")
# print(theword)
# show the number of characters in the word

correct_letter_positions = []
win = False
while number_of_guesses > 0 and win == False:

    print(thewordcopy)
    guess = raw_input("Go!\n").lower()
    if not validateguess.isacharacter(guess):
        print("That's not even a character! Try again")
    else:
        print("You're going to guess " + guess)
        if len(guess) > 1:
            if not validateguess.checkword(guess, theword):
                print("Oops, that's not right")
                number_of_guesses -= 1
            else:
                win = True
                print("You are correct!\nThe word is " + guess + "\nYou win!")
                break
        else:
            correct_letter_positions = validateguess.checkcharacter(guess, theword)
            if correct_letter_positions:
                for i in correct_letter_positions:
                    thewordcopy = thewordcopy[:i] + guess + thewordcopy[i + 1:]
                if thewordcopy == theword:
                    win = True
                    print("You Win\nWord is " + thewordcopy + "!\n")
                    break
            else:
                number_of_guesses -= 1
    print("You have ", number_of_guesses, " remaining...")
if win == False:
    print("Word was " + theword + ".")
print("Game over...")
