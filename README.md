<h1>Text Encoding Kit Introduction</h1>
<p>The <b>Text Encoding Kit</b> was created to convert words that are meaningful for humans into numbers that are meaningful for computers, and vice versa. This is especially important in the field of <b>Natural Language Processing</b>, where Recurrent Neural Networks are used to generate articles or classify text as having negative or positive sentiment.</p>

<h2>Brief Beginner Tutorial</h2>

Welcome to the Text Encoding Kit! In this brief tutorial, you will learn how to:
- Lookup the numerical values of word strings
- Lookup word strings based on numerical values
- Add words to the lookup dictionary
- Use the <b>EasyConvertSentenceToValues</b> function to easily convert sentences into numerical values

<h3>1. How to Lookup the Numerical Values of Word Strings</h3>

Let's say we had an array of words (in string form) that we wanted a Neural Network to understand. We cannot feed the Neural Network the word array directly. Instead, we can convert the word array into a numerical array that can be used as the network's input or expected output. In the Text Encoding Kit, there is a function just for that: The <b>LookUpWordValue</b> function.
<pre>
LookUpWordValue([<font color="green"> "the"</font>,<font color="green"> "function"</font>,<font color="green">" takes"</font>,<font color="green"> "an"</font>,<font color="green"> "array"</font>,<font color="green"> "of"</font>,<font color="green"> "words"</font>])
</pre>

<h1>Message to Contributors</h1>
<p>Contribution to this repository is highly appreciated, and will help make the Text Encoding Kit smarter and more useful. If you encounter any strange errors or problems while using this kit, let us know in the <b>Issues</b> section of GitHub.</p>

<img src="https://assets-cdn.github.com/images/modules/logos_page/Octocat.png" width="102" height="88">
