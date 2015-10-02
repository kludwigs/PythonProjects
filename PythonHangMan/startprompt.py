def hangmanstartprompt(args):
    if args =="y" or args=="yes":
        print("Oh Good, you want to play")
        return True
    elif args=="n" or args== "no":
        print("That's too bad. Maybe next time.")
        return False
    else:
        return False
    

