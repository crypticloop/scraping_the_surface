import string

def SearchForWordFrequency(arr):

    words = []

    for headline in arr:
        words.extend(headline.split())

    uniqueWords = {}

    for word in words:
        if word not in uniqueWords:
            uniqueWords[word]=1
        else:
            uniqueWords[word]+=1

    return uniqueWords
