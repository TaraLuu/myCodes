def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    string.upper()

    for i in range(0,len(string)) :
        if string[i] in "AEIOU": 
            kevin = kevin + len(string[i:])
        else:
            stuart = stuart + len(string[i:])

    if kevin > stuart: 
        print("Kevin" + " " + str(kevin)) 
    elif kevin < stuart: 
        print("Stuart" + " " + str(stuart))        
    else: 
        print("Draw")
