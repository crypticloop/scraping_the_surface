# Stop Words
---

## Overview

* Stop words are words that you either stop analysing when you reach, or discard before analysis
* This is a stage of pre-processing
* Need to import the following module:

```
from nltk.corpus import stopwords
```

* Can access the stopwords already inside NLTK using:

```
stop_words = set(stopwords.words("english"))
```

* To filter a sentence, compare it to an array of preloaded stop words
