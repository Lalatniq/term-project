Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/python
... def sentiment(positive_text, negative_text, input_text):
... '''
... Function: sentiment
... Arguments: positive_text, negative_text, input_text
... Returns: socre (int)
... The 1.0 version of our sentiment analyzer will start with a string of positive and
... negative words. For any input text and the sentiment score will be calculated.
... '''
... score = 0
... positive_text = positive_text.split()
... negative_text = negative_text.split()
... input_text = input_text.split()
... for word in input_text:
... if word in positive_text:
... score += 1
... elif word in negative_text:
... score -= 1
... return score
... 
... def main():
... print 'Sentiment Analyzer 1.0'
... print 'Type \'quit\' to exit.'
... positive_text = 'happy glad like good love'
... negative_text = 'angry mad hate'
... input_text = raw_input('Enter Text: ')
... while input_text != 'quit':
... score = sentiment(positive_text, negative_text, input_text)
... if score < 0:
... print score, 'negative.'
... elif score > 0:
... print score, 'positive.'
... else:
... print '0 neutral.'
... input_text = raw_input('Enter Text: ')
