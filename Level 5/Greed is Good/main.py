"""  
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 points """

def score(dice):
    output = 0
    values = [0,0,0,0,0,0]
    for i in dice:
        values[i-1]+=1
    x = 0
    while(x < 6):
        if values[x] >=3:
            output+= (x+1)*100
            if x == 1:
                output+=900
            values[x]+= -3
        elif values[x]<3 and values[x]>0:
            if x+1 == 5:
                output += 50
            if x+1 == 1:
                output += 100
            values[x]+= -1
        else:
            x+=1
    print(output)
    return output