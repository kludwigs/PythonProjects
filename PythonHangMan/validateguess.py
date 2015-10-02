def isacharacter(guess):
    for i in guess:
        if not i.isalpha():
            return False
    return True    
    

def checkword(guess, word):
    #print(guess)
    #print(word)
    #print("guess == word ", guess==word)
    #print("len of guess vs. len of word ", len(guess), " " , len(word))
    return guess == word

def checkcharacter(guess,word):
    print("checking with " + guess)
    tmp =[]
    count = 0
    for i in word:
        if guess == i:
            tmp.append(count)
        count+=1
    return tmp
