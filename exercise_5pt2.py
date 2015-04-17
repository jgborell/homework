import string
import re
import operator
def analyzer():
    inputfile=raw_input("What book would you like inspected? ")
    review=open(inputfile,'r')
    review=review.read()
    tokens=([e.lower() for e in map(string.strip, re.split("(\W+)", review)) if len(e) > 0 and not re.match("\W",e)])
    return tokens


def countLetters(word): # count occurances of characters in string
    letterdict = {}
    for letter in word:
        letterdict[letter] = 0
    for letter in word:
        letterdict[letter] += 1
    return letterdict

tokens = analyzer()
dict_letters = countLetters(tokens)

sorted_dict_letters = sorted(dict_letters.items(), key=operator.itemgetter(0))          #sort dictionary keys in order
sorted(dict_letters.items(), key=lambda sorted_dict_letters: sorted_dict_letters[0])

def countLettersSorted(word):       #print Key Value pairs
     count = 0                      #5 key value pairs per line
     for key, value in word:
         if count < 5:
             print "%s --> %s " % (key, value),
             count += 1
         else:
             print "\n"
             count = 0

print "***** BEGIN RANDOM STRING *****""\n"
print "\n"
countLettersSorted(sorted_dict_letters)
print "\n"
print "*******************************"
#remove punctuation

#convert to lowercase