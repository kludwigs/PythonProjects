import random

def getwordlistfromfile(filename):
    file = open(filename, 'r')
    lst =[]
    count = 0
    for line in file:
        if(len(line) > 6):
            count += 1
            lst.append(line)                
    myword = lst[random.randint(1, count)]
    word_okay = False
    while word_okay == False:
        if(validatemyword(myword)):
           #print("Word okay")
           word_okay = True
        else:
           #print("Word contains non alphanumeric characters." + myword + ".. picking another word") 
           myword  = lst[random.randint(1, count)]
    return myword               
    
def validatemyword(word):
    word = word.rstrip()
    count = 0
    word_length = len(word)
    for i in word:
        if i.isalpha():
            count+=1
    return(count == word_length)              

