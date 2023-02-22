""" 
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types. """

def find_short(s):
    l = s.__len__()
    words = s.split(" ")
    for word in words:
        if word.__len__() < l:
            l = word.__len__()
    return l