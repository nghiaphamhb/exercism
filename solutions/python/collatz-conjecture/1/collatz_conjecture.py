def steps(number):
    step = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    result = number
    while True:
        if result == 1:
            break

        step += 1
        if result % 2 == 0:
            result /= 2
        else:
            result = result * 3 + 1
    return step