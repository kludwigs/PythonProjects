import startprompt
import wordlist
import validateguess

print("Welcome to Karl's hang man game")
#print("Would you like to play?")

#answer = input("Type y or n and hit 'Enter'.\n").lower()

#action = startprompt.hangmanstartprompt(answer)

#if action is True:
 #   print("Okay let's get going")
#else:
 #   quit

# save the word and an array with the same length    
theword = wordlist.getwordlistfromfile("wordlist.txt")
theword = theword.rstrip()
thewordcopy = "-" * len( theword )
number_of_characters = len(theword)
print("Okay the word has ", number_of_characters, " characters")

number_of_guesses = 5

print("Enter a letter to begin guessing. You'll start with ", number_of_guesses, " guesses")
print(theword)
#show the number of characters in the word

correct_letter_positions = []

while number_of_guesses > 0:
    
    print(thewordcopy)
    guess = input("Go!\n").lower()
    if not validateguess.isacharacter(guess):
        print("That's not even a character! Try again")
    else:
        print("You're going to guess " + guess)
        if(len(guess) > 1):           
           if not validateguess.checkword(guess, theword):               
               print("Oops, that's not right")
           else:
               print("You are correct!\nThe word is " + guess + "\nYou win!")
               break
        else:               
           correct_letter_positions = validateguess.checkcharacter(guess,theword)
           if correct_letter_positions:
               for i in correct_letter_positions:                   
                   thewordcopy = thewordcopy[:i] + guess + thewordcopy[i+1:]   
        number_of_guesses -=1
    print("You have ", number_of_guesses, " remaining...")
    
print("Game over...")                





