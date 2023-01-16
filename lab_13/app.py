from textblob import TextBlob
from typing import List

def extract_sentiment(text):
    text = TextBlob(text)
    return text.sentiment.polarity

def text_contain_word(word,text):
    return word in text

def bubblesort(input: List):
    length = len(input)
    for repeats in range(0,length-1):
        for iteration in range(0,length-1):
            if input[iteration] > input[iteration+1]:
                (input[iteration],input[iteration+1]) = (input[iteration+1],input[iteration])
    return input

