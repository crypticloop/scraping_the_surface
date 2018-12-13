# Tokenising Words and Sentences
---

## Overview of NLP

* NLP is process of getting computer to understand written language
* Sentiment analysis looks at the sentiment of the speech about a certain topic

## NLTK

* Everything on [NLTK.org|https://www.hltk.org]
* Insert into code using:

`import nltk`

* Then need to run a download:

`nltk.download()`

* Select to download `all`

## Definitions

* **Corpora** - a body of text
* **Lexicon** - words and their meanings e.g. a dictionary
  * This can be separated on different vernaculars as well e.g. investor-speak, tech-speak etc.

## Tokenising

* This is the process of separating by some classifier, which can be:
  * word
  * sentence
  * paragraph
* Need to import the `tokenize` module:

`from nltk.tokenize import sent_tokenize, word_tokenize`

* NLTK tokenising is very effective, and will save a lot of time in writing regular expressions

## `sent_tokenize`

* Function which takes a string as an input
* Returns and array of strings
* Each of these strings is a sentence from the original string e.g.

Script:
```
exampleString = "This is a string. This is another string. These strings will be tokenised!"
print(sent_tokenize(exampleString))
```
Output:
```
["This is a string.","This is another string.", "These strings will be tokenised!"]
```

## `word_tokenize`

* Function which works exactly the same as `sent_tokenize`, but returns a list of words
