'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
Example

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

'''
ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alphabet_position(text):
    newText =""
    i = 0
    for char in text.lower():
        i+=1
        newText = newText + findPos(char)
    return newText[:-1]

def findPos(char):
    if char in ALPHA:
        pos = ALPHA.index(char) + 1
        return str(pos)+" "
    return ""