""" 
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

Additional Notes:

    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
    All tested numbers are valid, you don't need to validate them """

numbers = {
           "zero":    0,
           "one":     1, # All different numbers
           "two":     2,
           "three":   3,
           "four":    4,
           "five":    5,
           "six":     6,
           "seven":   7,
           "eight":   8,
           "nine":    9,
           "ten":     10,
           "eleven":  11,
           "twelve":  12,
           "thirteen":13,
           "fourteen":14,
           "fifteen":15,
           "sixteen":16,
           "seventeen":17,
           "eighteen":18,
           "nineteen":19,
           "twenty": 20,
           "thirty": 30,
           "forty":  40,
           "fifty":  50,
           "sixty":  60,
           "seventy":70,
           "eighty": 80,
           "ninety": 90}


hun = "hundred"
tho = "thousand"
mil = "million"

def parse_int(string:str):
    output = 0
    string = string.lower()
    string = string.split(" ")
    string.reverse()
    for word in string:                         # Remove unwanted words
        if "and" in string: string.remove("and")

    for x in range(len(string)):
        multi = 1
        value = string[x]
        if value == hun or value == tho or value == mil: continue # Skip words#
        
        nextValues = ["","",""]
        if x!=0 : nextValues[0] = string[x-1]
        if x > 1: nextValues[1] = string[x-2]
        if x > 2: nextValues[2] = string[x-3]
            
        if nextValues[0] == hun: multi = 100
        if nextValues[0] == tho: multi = 1000
        if nextValues[0] == hun and (nextValues[1] == tho or nextValues[2] == tho): multi  = 100000
        if nextValues[0] == mil: multi = 1000000

        if "-" in value:
            value = value.split("-")
            output+= (numbers.get(value[0])+numbers.get(value[1])) * multi
            continue

        output += numbers.get(value) * multi
    return output