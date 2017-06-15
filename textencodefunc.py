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



#Translates the floating-point value array into a word array

def LookUpWordForValue(wordvalues):
    WordListHere = []
    TheListOfWordsHere = open("C:/YourShortListOfWords.txt", "r")
    TheWordListWithin = TheListOfWordsHere.read()
    for line in TheWordListWithin.split('\n'):
        WordListHere.append(line)
    OutputWordListHere = []
    for wordvalue in wordvalues:
        OutputWordListHere.append(WordListHere[int(wordvalue*10000)])
    return OutputWordListHere



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

#Pads the word array with ^ to reshape it to the network's input size
def PadWordArray(WordArrayToPad,InputSize):
    if len(WordArrayToPad)>InputSize:
        return WordArrayToPad[0:InputSize]
    elif len(WordArrayToPad)==InputSize:
        return WordArrayToPad
    elif len(WordArrayToPad)<InputSize:
        PaddedWordArray = WordArrayToPad
        for PadChar in range(InputSize-len(WordArrayToPad)):
            PaddedWordArray.append("^")
        return PaddedWordArray
