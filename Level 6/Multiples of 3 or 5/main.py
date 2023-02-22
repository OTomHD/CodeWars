def solution(number):
    output = 0
    i = 0
    while(i < number):
        if(i%3==0 or i%5==0):
            output = output + i
        i = i+1
    return output