def is_armstrong_number(number):
    result = 0
    arr = [int(d) for d in str(number)]
    power = len(arr)
    for i in range(power):
        result += arr[i] ** power 

    return result == number
        
    
