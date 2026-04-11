def is_valid(isbn):
    sum = 0

    characs = [c for c in isbn if c != ' ' and c != '-'] 
    if len(characs) != 10: 
        return False
    
    if characs[-1] == 'X':
        characs[-1] = '10'

    try:
        arr = [int(c) for c in characs]
    except ValueError:
        return False

    for i in range(len(arr)):
        sum += (arr[i] * (len(arr) - i))

    return sum % 11 == 0
    
