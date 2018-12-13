# Part Of Speech Tagging
---

* Need to import NLTK as a whole, and also some sample text from corpus to analyse:

```
import nltk
from nlt.corpus import state_union
```

* Then can call the `pos_tag` method inside NLTK

```
tagged =  nltk.pos_tag(words)
```

* This returns a tuple of the words, and a **part of speech identifier**
* These are classified as follows:

| Tag | Meaning | Example |
| --- | --- | --- |
| CC | coordinating conjunction | |
| CD | cardinal digit | |
| DT | determiner| |
| EX | existential there | "there is", "there exists" |
| FW |	foreign word |
| IN | preposition/subordinating conjunction | |
| JJ | adjective  | 'big' |
| JJR |	adjective, comparative | 'bigger' |
| JJS | adjective, superlative | 'biggest' |
| LS | list marker | 1) |
| MD | modal | could, will |
| NN | noun, singular | 'desk' |
| NNS | noun plural | 'desks' |
| NNP | proper noun, singular | 'Harrison' |
| NNPS | proper noun, plural | 'Americans' |
| PDT | predeterminer | 'all the kids' |
| POS | possessive ending | parent\'s |
| PRP | personal pronoun | I, he, she |
| PRP$ | possessive pronoun | my, his, hers |
| RB | adverb | very, silently, |
| RBR | adverb, comparative | better |
| RBS | adverb, superlative | best |
| RP | particle | give up |
| TO | to	go | 'to' the store. |
| UH | interjection | errrrrrrrm |
| VB | verb, base form | take |
| VBD | verb, past tense | took |
| VBG | verb, gerund/present participle | taking |
| VBN | verb, past participle | taken |
| VBP | verb, sing. present, non-3d | take |
| VBZ | verb, 3rd person sing. present | takes |
| WDT | wh-determiner | which |
| WP | wh-pronoun | who, what |
| WP$ | possessive wh-pronoun | whose |
| WRB | wh-abverb	 | where, when |

* Common error points:
  * Nouns where they are specified with lower-case etc
  * Dependent on your source e.g. Twitter or written prose
