# Text Classification
---

* Classifies text into a category that you create
* Classifier used in **Sentiment Analysis** to define whether text is positive or negative

```
documents = []

for category in movie_reviews.categories():
  for fileId in movie_reviews(category):
    documents.append(list(movie_reviews.words(fileId)), category)
```
