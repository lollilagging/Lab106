"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

def getWords() :
    """GETS WORDS BASE ON ARTICLES NOUNS VERBS AND PREPOSITION"""
    txtNames = ("articles", "nouns", "verbs", "prepositions")

    articlesTemp = []
    nounsTemp = []
    verbsTemp = []
    prepositionsTemp = []
    
    for check in txtNames :
        TextFiles = open(check + ".txt", 'r')
        temp = TextFiles.readlines()

    #wanted to use a variable that changes name but i havent researched that yet
        for i in temp:
            if i[-1] == "\n":
                if check == "articles" :
                    articlesTemp.append(i[:-1])
                elif check == "nouns" :
                    nounsTemp.append(i[:-1])
                elif check == "verbs" :
                    verbsTemp.append(i[:-1])
                elif check == "prepositions" :
                    prepositionsTemp.append(i[:-1])                                        
            else:
                if check == "articles" :
                    articlesTemp.append(i)
                elif check == "nouns" :
                    nounsTemp.append(i)
                elif check == "verbs" :
                    verbsTemp.append(i)
                elif check == "prepositions" :
                    prepositionsTemp.append(i)    
            TextFiles.close()       
    
    return tuple(articlesTemp), tuple(nounsTemp), tuple(verbsTemp), tuple(prepositionsTemp)

articles, nouns, verbs, prepositions = getWords(); 

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    
    """GETS THE LIST OF VOCABS FROM THE TEXT FILES """ 

    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()

