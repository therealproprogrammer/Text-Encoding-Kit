
def LookUpWordValue(words):
    '''
    ---------------------------------------------------------------------
    DESCRIPTION
    Translates the word (string) array into a floating-point value array.
    ---------------------------------------------------------------------
    PARAMETERS
    words (string array): The array of words to convert into a floating-
    point value array.
    ---------------------------------------------------------------------
    '''
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


def LookUpWordForValue(wordvalues):
    '''
    ---------------------------------------------------------------------
    DESCRIPTION
    Translates the floating-point value array into a word (string) array.
    ---------------------------------------------------------------------
    PARAMETERS
    wordvalues (floating-point value array): The array of floating-point
    values to convert into a word (string) array.
    ---------------------------------------------------------------------
    '''
    WordListHere = []
    TheListOfWordsHere = open("C:/YourShortListOfWords.txt", "r")
    TheWordListWithin = TheListOfWordsHere.read()
    for line in TheWordListWithin.split('\n'):
        WordListHere.append(line)
    OutputWordListHere = []
    for wordvalue in wordvalues:
        OutputWordListHere.append(WordListHere[int(wordvalue*10000)])
    return OutputWordListHere


def IsValidWordArray(WordsToCheck):
    '''
    ---------------------------------------------------------------------
    DESCRIPTION
    Checks if the words in the word (string) array are part of the
    dictionary.
    ---------------------------------------------------------------------
    PARAMETERS
    WordsToCheck (string array): The array of words to check for in the
    dictionary.
    ---------------------------------------------------------------------
    '''
    VALID = True
    try:
        LookUpWordValue(WordsToCheck)
    except:
        VALID = False
    return VALID


def AddWordToDictionary(WordToAdd):
    '''
    ---------------------------------------------------------------------
    DESCRIPTION
    Adds a word to the dictionary file, if it does not already exist.
    ---------------------------------------------------------------------
    PARAMETERS
    WordToAdd (string): The word to add to the dictionary.
    ---------------------------------------------------------------------
    '''
    ListOfExistWords = open("C:/YourShortListOfWords.txt", "r")
    ExistingWords = ListOfExistWords.read()
    NOTTAKEN = True
    for ExistLine in ExistingWords.split('\n'):
        if ExistLine.lower()==WordToAdd:
            NOTTAKEN = False
    if NOTTAKEN:
        ReadyToAdd = open("C:/YourShortListOfWords.txt", "a")
        ReadyToAdd.write("\n"+WordToAdd.lower())


def PadWordArray(WordArrayToPad,InputSize):
    '''
    ---------------------------------------------------------------------
    DESCRIPTION
    Pads the word array with ^ to reshape it to the network's input size,
    or trims it if necessary. Otherwise, leaves it unchanged.
    ---------------------------------------------------------------------
    PARAMETERS
    WordArrayToPad (string array): The word array to pad.
    InputSize (integer): The input size the neural network expects.
    ---------------------------------------------------------------------
    '''
    if len(WordArrayToPad)>InputSize:
        return WordArrayToPad[0:InputSize]
    elif len(WordArrayToPad)==InputSize:
        return WordArrayToPad
    elif len(WordArrayToPad)<InputSize:
        PaddedWordArray = WordArrayToPad
        for PadChar in range(InputSize-len(WordArrayToPad)):
            PaddedWordArray.append("^")
        return PaddedWordArray


def EasyConvertSentenceToValues(SentenceArray,InputSize):
    '''
    ---------------------------------------------------------------------
    DESCRIPTION
    Converts the array of sentences to an array of word value arrays. If
    necessary, they might be padded.
    ---------------------------------------------------------------------
    PARAMETERS
    SentenceArray (string array): The sentence array to convert.
    InputSize (integer): The input size the neural network expects.
    ---------------------------------------------------------------------
    '''
    ArrOfTokenWrdArrs=[]
    #Tokenizes each sentence in ArrOfTokenWrdArrs
    import nltk
    for SentenceToTokenize in SentenceArray:
        ArrOfTokenWrdArrs.append(PadWordArray(nltk.word_tokenize(SentenceToTokenize),InputSize))
        
    #Checks the validity of ArrOfTokenWrdArrs, extending the dictionary if necessary
    for WordArray in ArrOfTokenWrdArrs:
        for Word in WordArray:
            if IsValidWordArray([Word]):
                print(Word+" is a valid word.")
            else:
                AddWordToDictionary(Word)

    #Converts ArrOfTokenWrdArrs to an array of word value arrays
    ArrOfWrdValArrs=[]
    for WordArrayToConvert in ArrOfTokenWrdArrs:
        ArrOfWrdValArrs.append(LookUpWordValue(WordArrayToConvert))
    return ArrOfWrdValArrs

'''
#Keras Example Below
from keras.models import Sequential

from keras.layers.core import Dense, Dropout, Activation

from keras.optimizers import SGD

import numpy as np 


#The idea here is to output only one of the inputs (remove redundancy).
#For some reason, the outputs I got had similar values (so the outputs started with the same letter) when the dictionary file
#contained a long list of alphabetically-arranged words.
#I would appreciate it if anyone can help fix this bug.

#Here is the input data
X = np.array(EasyConvertSentenceToValues(["code code","program program","pet pet"],9))

#Here is the output data
y = np.array(EasyConvertSentenceToValues(["code","program","pet"],1))



model = Sequential()

model.add(Dense(8, input_dim=9))

model.add(Activation('tanh'))

model.add(Dense(6))

model.add(Activation('sigmoid'))

model.add(Dense(1))

model.add(Activation('sigmoid'))


sgd = SGD(lr=0.1)

model.compile(loss='binary_crossentropy', optimizer=sgd)



model.fit(X, y, batch_size=1, nb_epoch=100)

print(model.predict_proba(X))
for whatever in model.predict_proba(X).tolist():
    for theThing in whatever:
        print(LookUpWordForValue([round(theThing,1000)]))
'''
