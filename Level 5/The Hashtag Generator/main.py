""" 
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""

def generate_hashtag(s):
    words = s.split(" ")
    i = 0
    newWords = []
    for word in words:
        if word == "":
            continue
        newWords.append(word.capitalize())
        i+=1
    newWords.insert(0, "#")
    output = "".join(newWords)
    if len(output) > 140: # More then 140 characters
        return False
    if output == "#":     # Empty String
        return False
    return output         # Succesful