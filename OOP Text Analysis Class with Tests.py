'''
OOP exercise involving creating a language analysis utility tool that can perform analysis on a
given piece of text, a class containing 3 methods:
1. Takes in text, makes it lower case, and removes any periods, exclamation marks, commas, and question marks.
2. Return dictionary containing all unique words in text along with number of their occurences.
3. Returns frequence of the word passed in the arg.

2nd half of code is a test written to test the class and its methods.
'''

import sys

class analysedText(object):
    
    def __init__ (self, text):
        # utilized method chaining
        self.fmtText = text.lower().replace('.','').replace('!','').replace(',','').replace('?','')
    
    def freqAll(self):  
        # splits text into words      
        split_list = self.fmtText.split(' ')
        
        # initialize empty dictionary
        dictcount = {}
        
        for word in set(split_list): # set used to remove dupes in list
            dictcount[word] = split_list.count(word)
                      
        return dictcount
    
    def freqOf(self,word):
        # use frequency dictionary from previous method
        wordsdictcount = self.freqAll()
        
        if word in wordsdictcount:
            return wordsdictcount[word]
        else:
            return 0


# test functions below:
sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )