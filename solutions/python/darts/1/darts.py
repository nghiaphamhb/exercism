import math 

def score(x, y):
    radius = math.sqrt(x ** 2 + y ** 2)
    
    if radius > 10:
        return 0
    elif 5 < radius <= 10: 
        return 1
    elif 1 < radius <= 5: 
        return 5
    else:
        return 10
