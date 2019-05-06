import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk import pos_tag

def pipe(string):
    
    #Sentence Split
    result = sent_tokenize(string)

    #Remove Characters
    result = list(map(lambda i: re.sub('[^A-Za-z0]+', ' ', i), result))

    #Token
    result = list(map(lambda i: word_tokenize(i), result))

    #Lemm
    print(result)
    lemmatizer = WordNetLemmatizer()
    result = list(map(lambda i: list(map(lambda j: lemmatizer.lemmatize(j),i)),result))

    #Stemm
    print(result)
    stemmer = SnowballStemmer('english')
    result = list(map(lambda i: list(map(lambda j: stemmer.stem(j), i)), result))

    #Pos Tagging
    print(result)
    result = list(map(lambda i: pos_tag(i), result))

    return result

while True:
    try:
        text = input()
        if text == '':#flag para rodar direto no cmd
            continue
        print(pipe(text))
    except EOFError:
        break
