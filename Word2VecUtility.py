# licensed under ieee project
#Auhor Rahul Kumar Chauhan


import re
import nltk

import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from nltk.corpus import stopwords


class Word2VecUtility(object):

    @staticmethod
    def review_to_wordlist( review, remove_stopwords=False ):
       
        review_text = BeautifulSoup(review).get_text()

        review_text = re.sub("[^a-zA-Z]"," ", review_text)
        
        words = review_text.lower().split()

        if remove_stopwords:
            stops = set(stopwords.words("english"))
            words = [w for w in words if not w in stops]
       
        return(words)

    @staticmethod
    def review_to_sentences( review, tokenizer, remove_stopwords=False ):
        
        raw_sentences = tokenizer.tokenize(review.decode('utf8').strip())
        
        sentences = []
        for raw_sentence in raw_sentences:
            
            if len(raw_sentence) > 0:
                
                sentences.append( Word2VecUtility.review_to_wordlist( raw_sentence, \
                  remove_stopwords ))
        
        return sentences
