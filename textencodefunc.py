def look_up_word_value(words):
    """
    ---------------------------------------------------------------------
    DESCRIPTION
    Translates the word (string) array into a floating-point value array.
    ---------------------------------------------------------------------
    PARAMETERS
    words (string array): The array of words to convert into a floating-
    point value array.
    ---------------------------------------------------------------------
    """
    the_dictionary = {}
    word_num = 0
    the_list_of_words = open("C:/YourShortListOfWords.txt", "r")
    the_text_within = the_list_of_words.read()
    for line in the_text_within.split('\n'):
        # print(line+":"+str(word_num))
        the_dictionary[line] = word_num
        word_num = word_num + 1
    looked_up_array = []
    for word in words:
        looked_up_array.append(int(the_dictionary[word]))
    # print(looked_up_array)
    real_looked_up_array = []
    for word_val in looked_up_array:
        real_looked_up_array.append(word_val / 10000)
    return real_looked_up_array


def look_up_word_for_value(word_values):
    """
    ---------------------------------------------------------------------
    DESCRIPTION
    Translates the floating-point value array into a word (string) array.
    ---------------------------------------------------------------------
    PARAMETERS
    wordvalues (floating-point value array): The array of floating-point
    values to convert into a word (string) array.
    ---------------------------------------------------------------------
    """
    word_list_here = []
    the_list_of_words_here = open("C:/YourShortListOfWords.txt", "r")
    the_word_list_within = the_list_of_words_here.read()
    for line in the_word_list_within.split('\n'):
        word_list_here.append(line)
    output_word_list_here = []
    for word_value in word_values:
        output_word_list_here.append(word_list_here[int(word_value * 10000)])
    return output_word_list_here


def is_valid_word_array(words_to_check):
    """
    ---------------------------------------------------------------------
    DESCRIPTION
    Checks if the words in the word (string) array are part of the
    dictionary.
    ---------------------------------------------------------------------
    PARAMETERS
    words_to_check (string array): The array of words to check for in the
    dictionary.
    ---------------------------------------------------------------------
    """
    valid = True
    try:
        look_up_word_value(words_to_check)
    except:
        valid = False
    return valid


def add_word_to_dictionary(word_to_add):
    """
    ---------------------------------------------------------------------
    DESCRIPTION
    Adds a word to the dictionary file, if it does not already exist.
    ---------------------------------------------------------------------
    PARAMETERS
    word_to_add (string): The word to add to the dictionary.
    ---------------------------------------------------------------------
    """
    list_of_exist_words = open("C:/YourShortListOfWords.txt", "r")
    existing_words = list_of_exist_words.read()
    not_taken = True
    for ExistLine in existing_words.split('\n'):
        if ExistLine.lower() == word_to_add:
            not_taken = False
    if not_taken:
        ready_to_add = open("C:/YourShortListOfWords.txt", "a")
        ready_to_add.write("\n" + word_to_add.lower())


def pad_word_array(word_array_to_pad, input_size):
    """
    ---------------------------------------------------------------------
    DESCRIPTION
    Pads the word array with ^ to reshape it to the network's input size,
    or trims it if necessary. Otherwise, leaves it unchanged.
    ---------------------------------------------------------------------
    PARAMETERS
    word_array_to_pad (string array): The word array to pad.
    input_size (integer): The input size the neural network expects.
    ---------------------------------------------------------------------
    """
    if len(word_array_to_pad) > input_size:
        return word_array_to_pad[0:input_size]
    elif len(word_array_to_pad) == input_size:
        return word_array_to_pad
    elif len(word_array_to_pad) < input_size:
        padded_word_array = word_array_to_pad
        for PadChar in range(input_size - len(word_array_to_pad)):
            padded_word_array.append("^")
        return padded_word_array


def easy_convert_sentence_to_values(sentence_array, input_size):
    """
    ---------------------------------------------------------------------
    DESCRIPTION
    Converts the array of sentences to an array of word value arrays. If
    necessary, they might be padded.
    ---------------------------------------------------------------------
    PARAMETERS
    sentence_array (string array): The sentence array to convert.
    input_size (integer): The input size the neural network expects.
    ---------------------------------------------------------------------
    """
    arr_of_token_wrd_arrs = []
    # Tokenizes each sentence in arr_of_token_wrd_arrs
    import nltk
    for SentenceToTokenize in sentence_array:
        arr_of_token_wrd_arrs.append(pad_word_array(nltk.word_tokenize(SentenceToTokenize), input_size))

    # Checks the validity of arr_of_token_wrd_arrs, extending the dictionary if necessary
    for WordArray in arr_of_token_wrd_arrs:
        for Word in WordArray:
            if is_valid_word_array([Word]):
                print(Word + " is a valid word.")
            else:
                add_word_to_dictionary(Word)

    # Converts arr_of_token_wrd_arrs to an array of word value arrays
    arr_of_wrd_val_arrs = []
    for WordArrayToConvert in arr_of_token_wrd_arrs:
        arr_of_wrd_val_arrs.append(look_up_word_value(WordArrayToConvert))
    return arr_of_wrd_val_arrs


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
