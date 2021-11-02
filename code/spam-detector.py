import string
from collections import Counter
from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer

def getUppercaseWordNumber(_list):
    "This calculate the number of words in uppercase in the message"
    n = 0
    for element in _list:
        length = len(element) # Token Length
        upper = sum(char.isupper() for char in element) # Character in the uppercase number      
        if upper==length: # the case all the characters are in the uppercase
            n+=1
    return n

with open('../output/English_big_data.arff', 'w') as out:
    out.write('@relation sms\n')
    out.write('\n@attribute ncharacter real\n')
    out.write('@attribute ndollars real\n')
    out.write('@attribute nnumeric real\n')
    out.write('@attribute nuppercase real\n')
    out.write('@attribute type {ham, spam}\n')
    out.write('\n@data\n')

try:
    stemmer = SnowballStemmer("english")
    file = open('../dataset/english-big.txt', 'r',encoding="ISO-8859-1" )
    for line in file: 
        counter = Counter(line) #creating a counter in the program 
        num_character = len(line) #the number of characters in the text message from the file
        num_dollars = counter['$'] #the number of dollar in the text message from the file            
        num_numeric = sum(char.isdigit() for char in line) #the number of numerics in the text message from the file
        line = line.translate(str.maketrans('.,;:/?!@#$&~#{([|-_^)]+=}*%', '                           ')) #removing any special characters in the text       
        tokens = line.split() #splitting of the message into the words
        num_uppercase_word = getUppercaseWordNumber(tokens) #the number of the upppercased words in the text      
        tokens = [stemmer.stem(token.lower()) for token in tokens] #
        tokens.insert(0,num_character) #inserting the number of characters in the first position or place in the text
        tokens.insert(1,num_dollars) #inserting the number of dollars in the second position or place in the text
        tokens.insert(2,num_numeric) #inserting the number of numeric in the third position or place in the text
        tokens.insert(3,num_uppercase_word) #inserting the number of uppercase in the fourth position or place in the text
        

        with open('../output/English_big_data.arff', 'a') as out:
            i = 0
            for token in tokens[:5]:
                i+=1
                if i!=5:
                    out.write(str(token) + ',')
                else:
                    out.write(str(token) + '\n')
                
        
        
except Exception as e:
    print('Error: ' + str(e))



