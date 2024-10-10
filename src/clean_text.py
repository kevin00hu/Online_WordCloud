import re

import nltk

#=======================================================#

def remove_punctuation(string:str, *args)->str:
    """ remove punctuation from the input string """
    pattern = r"[\[\]\*,\.:-]"

    string = re.sub(pattern, "", string)

    return string


def tokenize(string:str, *args)->str:
    """ Tokenize the input string """
    tokenizer = nltk.tokenize.ToktokTokenizer()

    tokenized_string = tokenizer.tokenize(string, return_str=True)

    return tokenized_string

def stem(string:str, *args)->str:
    """ lemmatize the string """
    lemmatizer = nltk.stem.WordNetLemmatizer()

    stemmed_words_list = [lemmatizer.lemmatize(word) for word in string.split()]

    stemmed_string = ' '.join(stemmed_words_list)

    return stemmed_string

def _is_normal_word(word, stop_words, extra_stop_words):
    if word in stop_words:
        return False
    
    for pattern in extra_stop_words:
        if re.match(pattern, word):
            return False
        
    return True

def remove_stopwords(string:str, extra_stop_words:list=[])->str:
    """ Remove Stopwords and user input words """
    stop_words = nltk.corpus.stopwords.words("english")

    word_list = string.split()

    filtered_list = [word for word in word_list 
                     if _is_normal_word(word, stop_words, extra_stop_words)]
    
    filtered_string = " ".join(filtered_list)

    return filtered_string

def clean(string:str, extra_stop_words:list=[])->str:
    """ Main cleaning function """
    cleaned_string = string

    clean_funs = [
        remove_punctuation,
        tokenize,
        stem,
        remove_stopwords
    ]

    for func in clean_funs:
        cleaned_string = func(cleaned_string, extra_stop_words)

    return cleaned_string