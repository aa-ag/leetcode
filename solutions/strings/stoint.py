import re

def myAtoi(s):
    '''
     - Read in and ignore any leading whitespace.
     - Check if the next character (if not already at the end of the string) 
        is '-' or '+'. Read this character in if it is either. 
    '''
    within = [-(pow(2, 31)), pow(2, 31) -1]

    s = s.lstrip(' ')

    if s.startswith('-'):
        is_negative = True
    else:
        is_negative = False

    s = s.replace('-', '')
    print(s)


myAtoi("   -42")
myAtoi("4193 with words")