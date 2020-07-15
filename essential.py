alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz" #String of lowercase letters, also available in the string module as string.ascii_lowercase
alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #String of uppercase letters, also available in the string module as string.ascii_uppercase
alphabet_lowercase_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ") #A list of all the lowercase letters
alphabet_uppercase_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ") #A list of all the uppercase letters
testphrase = "The quick brown fox jumps over the lazy dog" #This can be used to check that all letters are present in the list (refer to line 6)
def checkAlphabet():
    #For each letter in the alphabet
    for x in range(26):
        if alphabet_lowercase_list[x] in testphrase:
            #If the letter is anywhere in the sentence, print True
            print(True)
        else:
            #Otherwise, print false
            print(False)
    #If one of the repetitions returns False, that means that the list does not contain all the letters.
def getNumbers(start, stop, jump, listorstr, strornum=False, space=False):
    tempstr = ""
    templist = []
    for x in range(start, stop, jump):
        if listorstr == True:
            if strornum == True:
                templist.append(str(x))
            elif strornum == False:
                templist.append(x)
        elif listorstr == False:
            if space == True:
                tempstr = tempstr + x + " "
            elif space == False:
                tempstr = tempstr + x
    if listorstr == True:
        return templist
    elif listorstr == False:
        return tempstr

def getNumbers2(start, stop, jump, options):
    tempstr = ""
    templist = []
    for x in range(start, stop, jump):
        if options[0] == True:
            if options[1] == True:
                templist.append(str(x))
            elif options[1] == False:
                templist.append(x)
        elif options[0] == False:
            if options[2] == True:
                tempstr = tempstr + x + " "
            elif options[2] == False:
                tempstr = tempstr + x
    if options[0] == True:
        return templist
    elif options[0] == False:
        return tempstr