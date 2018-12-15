# Chinking
---

* This is the method of intentionally excluding some types of words from the chunking process
* It is done inside the REGEX string
* Must be specified as a REGEX
  * Comes after the chunking regex
  * Is contained with reversed curly brackets
* An example is seen below:

```
chunkGram = r"""Chunk: {<.*>+}
                        }<VB.?|IN|DT|TO>+{"""
```
