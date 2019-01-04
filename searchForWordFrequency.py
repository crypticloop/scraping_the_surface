import string
import operator

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

def SortDictionary(dict):

    sortedList = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

    return sortedList

def PrintFormattedListOfTuples(listTuples):
    for item in listTuples:
        print('Word: {0}    Frequency {1}.'.format(item[0], item[1]))
