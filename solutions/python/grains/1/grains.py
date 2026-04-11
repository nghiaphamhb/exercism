def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    final_result = 0
    
    for i in range(64):
        final_result += square(i + 1)
        
    return final_result
