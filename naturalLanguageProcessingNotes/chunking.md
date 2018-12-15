# Chunking
---

* The first thing you look at in a sentence is the subject
* The subject of the sentence, i.e. what the sentence is about, is called the **named entity**
* There can be many named entities in one sentence
* A **modifier** is a word that affects that noun
* Chunking splits a sentence into **noun phrases**
  * A noun surrounded by its modifiers
* Makes it easier to understand sentences with multiple named entities
* Chunking is done as a combination of **part of speech tags** and **regex**
* Use a Regex to parse a set of tagged words
  * This regex will look for a series of tags which indicate a chunk of meaningful information
* These chunks can then be analysed separately
* An example function is as follows:

```

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()     

    except Exception as e:
        print(str(e))

process_content()
```
