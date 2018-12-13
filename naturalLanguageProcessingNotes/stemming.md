# Stemming
---

* Form of data pre-processing
* Is the action of taking the root stem of the word
* This is done to extract the meaning of a sentence without having to store many different conjugations/variations of different words

* Need to import `PorterStemmer` and create an instance of it

```
from nltk.stem import PorterStemmer
ps = PorterStemmer()
```

* Can then use the `.stem` method to find the stem of an individual word
  * `stem` method takes a word as an input

```
for w in example_words:
  print(ps.stem(w))
```
