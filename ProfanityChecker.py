'''
Created on Oct 20, 2016

@author: erexsha
'''
import urllib

def read_text():
    quotes = open(r"c:\code\tmp\quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()