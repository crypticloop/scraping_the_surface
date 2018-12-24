# Lemmatizing
---

* Like stemming, but actual word given as root
  * Can be the synonym of the word
* Imported from `nltk.stem`

```
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print (lemmatizer.lemmatize("better"))
```

* Specifying the type of the word gives more information about the root
  * e.g. adjective specified with `pos="a"`
* Default parameter is noun, or `pos='n'`
