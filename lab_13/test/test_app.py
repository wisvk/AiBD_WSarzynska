from app import bubblesort
from app import extract_sentiment
from app import text_contain_word
import pytest

test1 = [('I think today will be a horrible day','negative'),
         ('I think today will be a great day','positive')]
@pytest.mark.parametrize('example, sentiment',test1)
def test_extract_sentiment(example,sentiment):
    text_sentiment = extract_sentiment(example)
    if sentiment == 'positive':
        assert text_sentiment > 0
    if sentiment == 'negative':
        assert text_sentiment < 0

    
test2 = [('There is a duck in this text', 'duck', True),
         ('There is nothing here', 'duck', False)]
@pytest.mark.parametrize('example, word, expected', test2)
def test_text_contain_word(example, word, expected):
    assert text_contain_word(word, example) == expected


test3 = [([9,8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8,9]),
        ([2,4,5,1,3,9,7,6,8],[1,2,3,4,5,6,7,8,9])]
@pytest.mark.parametrize('example, expected', test3)
def test_bubblesort(example,expected):
    sorted = bubblesort(example)
    print(sorted)
    assert sorted==expected

