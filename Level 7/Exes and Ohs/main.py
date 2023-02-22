""" 
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false """

def xo(s):
    #         x o
    s = s.lower()
    values = [0,0]
    for i in s:
        if i == "x":
            values[0]+=1
        if i == "o":
            values[1]+=1
    if values[0] == values[1]:
        return True
    return False