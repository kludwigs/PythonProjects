print("You've just entered the clinic!")
print("Do you take the door on the left or the right?")
answer = input("Type left or right and hit 'Enter'.\n").lower()
print("you entered--\t" + answer + "\n");
if answer =="left":
    print("Sorry, you chose poorly. You lose")
elif answer=="right":
    print("You choose wisely. You win")
else:
    print("I don't understand what you're saying")

    
