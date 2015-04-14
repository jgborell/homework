import string
import random
import operator
my_randoms = []

for i in range(10):         #generate 10 randomized random lengthed strings
    my_randoms.append(''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(random.randint(0, 10))))

text = ''.join(my_randoms) # convert into one long string

def countLetters(word): # count occurances of characters in string
    letterdict = {}
    for letter in word:
        letterdict[letter] = 0
    for letter in word:
        letterdict[letter] += 1
    return letterdict

dict_letters = countLetters(text)

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
print text
print "\n"
countLettersSorted(sorted_dict_letters)
print "\n"
print "*******************************"
