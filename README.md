
<h1>Text Encoding Kit Introduction</h1>
<p>The <b>Text Encoding Kit</b> was created to convert words that are meaningful for humans into numbers that are meaningful for computers, and vice versa. This is especially important in the field of <b>Natural Language Processing</b>, where Recurrent Neural Networks are used to generate articles or classify text as having negative or positive sentiment.</p>

<h2>Brief Beginner Tutorial</h2>

Welcome to the Text Encoding Kit! In this brief tutorial, you will learn how to:
- Lookup the numerical values of word strings
- Lookup word strings based on numerical values
- Add words to the lookup dictionary
- Use the <b>EasyConvertSentenceToValues</b> function to easily convert sentences into numerical values

<h3>1. How to Lookup the Numerical Values of Word Strings</h3>

Let's say we had an array of words (in string form) that we wanted a Neural Network to understand. We cannot feed the Neural Network the word array directly. Instead, we can convert the word array into a numerical array that can be used as the network's input or expected output. In the Text Encoding Kit, there is a function just for that: The <code><b>LookUpWordValue</b></code> function.

EXAMPLE:
```python
print(LookUpWordValue["a","pet"])
#Gives you the numerical values of "a" and "pet" as an array, based on their positions in YourShortListOfWords.txt
```

<h3>2. How to Add Words to the Lookup Dictionary</h3>

However, what would happen if we used <code>LookUpWordValue</code> on words not in YourShortListOfWords.txt? We would recieve an error!
```python
LookUpWordValue(["UnknownWord","NotInDictionary"])
#Gives an error
```

We can add the unknown words to YourShortListOfWords.txt manually using a text editor like Notepad, or we can just use the <code><b>AddWordToDictionary</b></code> function. As a bonus, this function will not add words that already exist in the text file.

EXAMPLE:
```python
AddWordToDictionary(["UnknownWord","NotInDictionary"])
#The new words were added to YourShortListOfWords.txt
```

<h3>3. How to Lookup Word Strings Based on Numerical Values</h3>

So far, we learned how to lookup the numerical values of words. How do we lookup words based on numerical values? There is a function for that too: The <code><b>LookUpWordForValue</b></code> function.

EXAMPLE:
```python
print(LookUpWordForValue[0.0001,0.0002])
#Gives you the words that 0.0001 and 0.0002 represent, based on the words' positions in YourShortListOfWords.txt
```

<h3>4. How to Easily Convert Sentences into Numerical Values</h3>

If the neural network needed to take several raw sentences as input, it would be too difficult to use <code>LookUpWordValue</code> and <code>LookUpWordForValue</code>. Also, the input array's size needs to match the network's expected input size. For this, we have the <code><b>EasyConvertSentenceToValues</b></code> function. It takes an array of sentences and, with the help of NLTK, will break the sentences into words and convert those into numerical values. The result is an array of word value arrays (arrays within an array):

EXAMPLE:
```python
print(EasyConvertSentenceToValues(["a pet","pet pet"]))
#Converts the sentences into numerical value arrays
```

<h1>Message to Contributors</h1>
<p>Contribution to this repository is highly appreciated, and will help make the Text Encoding Kit smarter and more useful. If you encounter any strange errors or problems while using this kit, let us know in the <b>Issues</b> section of GitHub.</p>

<img src="https://assets-cdn.github.com/images/modules/logos_page/Octocat.png" width="102" height="88">
