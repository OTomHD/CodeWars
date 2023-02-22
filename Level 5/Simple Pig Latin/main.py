""" 
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
 """


def pig_it(text):
    words = text.split(" ")
    newWords = ""
    for word in words:
        if word == "!" or word == "?" :
            newWords+= (word + " ")
            continue
        word = (word + word[0]+"ay ")
        word = word[1:]
        newWords+= word
    return newWords[:-1]