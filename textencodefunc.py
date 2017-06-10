#Translates the word (string) array into a floating-point value array
def LookUpWordValue(words):
    TheDictionary={}
    wordNum=0
    TheListOfWords = open("C:/YourShortListOfWords.txt", "r")
    TheTextWithin = TheListOfWords.read()
    for line in TheTextWithin.split('\n'):
        #print(line+":"+str(wordNum))
        TheDictionary[line]=wordNum
        wordNum=wordNum+1
    LookedUpArray = []
    for word in words:
        LookedUpArray.append(int(TheDictionary[word]))
    #print(LookedUpArray)
    RealLookedUpArray = []
    for wordval in LookedUpArray:
        RealLookedUpArray.append(wordval/10000)
    return(RealLookedUpArray)

#Checks if the words in the word (string) array are part of the dictionary
def IsValidWordArray(WordsToCheck):
    VALID = True
    try:
        LookUpWordValue(WordsToCheck)
    except:
        VALID = False
    return VALID

#Adds a word to the dictionary file, if it does not already exist
def AddWordToDictionary(WordToAdd):
    ListOfExistWords = open("C:/YourShortListOfWords.txt", "r")
    ExistingWords = ListOfExistWords.read()
    NOTTAKEN = True
    for ExistLine in ExistingWords.split('\n'):
        if ExistLine.lower()==WordToAdd:
            NOTTAKEN = False
    if NOTTAKEN:
        ReadyToAdd = open("C:/YourShortListOfWords.txt", "a")
        ReadyToAdd.write("\n"+WordToAdd.lower())

AddWordToDictionary("github")
