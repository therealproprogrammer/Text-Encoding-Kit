#Use this function to look up the value of a word array, based on the words' position in YourListOfWords.txt:
LookedUpValues = LookUpWordValue(["a","pet"])

#Now we have our word values. Let's display them:
print(LookedUpValues)

#Is the array ["a_word_not_on_the_list","another_word_not_on_the_list"] a valid word array? Let's check:
print(IsValidWordArray(["a_word_not_on_the_list","another_word_not_on_the_list"]))
#It returns False, meaning the array was not a valid word array
# That is because it cannot find the words "a_word_not_on_the_list" and "another_word_not_on_the_list" in YourListOfWords.txt

#Let's add them:
AddWordToDictionary("a_word_not_on_the_list")
AddWordToDictionary("another_word_not_on_the_list")

#Let's say we wanted to feed a word array into a neural network of input size 9. How can we reshape the array?
#We can add ^ values to the array to make its size match the input size
print(PadWordArray(["A","program","is","worth","a","thousand","megabytes"]))

#With these functions, you can preprocess data to make it suitable for a neural network
#I hope this tutorial was helpful, and I hope that these functions will aid you in creating a natural language processing algorithm
