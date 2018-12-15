# Named Entity Recognition
---

* Named entities can be used in chunking
* Looks to fix the errors in chunking where names and countries etc are split up
* These entities are recognised and specified into the following categories

| Named Entity Type | Example |
| --- | --- |
| Organisation | Georgia-Pacific Corp. |
| Person | President Obama, George Bush |
| Location | Mount Everest |
| Date | June, 08/03/2018 |
| Time | Two Fifty AM, 13:30 PM |
| Money | 17 million Canadian Dollars, GBP 10.40 |
| Percent | twenty pct, 18.75% |
| Facility | Washington Monument, Stone Henge |
| GPE | South East Asia, Midlothian |

* Called using the `nltk.ke_chunk()` method from `nltk` module
* Setting `binary=True` inside the method will assign a `1` to a named entity, but not specify entity type
* False positives and error rates are quite high with this method
