def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if len(digits) > 0:
        for d in digits:
            if d < 0 or d >= input_base:
                raise ValueError("all digits must satisfy 0 <= d < input base")
                
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    value = 0
    for i in range(len(digits)):
        value += digits[i] * input_base ** (len(digits) - 1 - i)

    max_power = 0
    while output_base ** (max_power + 1) <= value:
        max_power += 1

    out_digits = []
    for k in range(max_power, -1, -1):
        out_d = value // output_base ** k
        out_digits.append(out_d)
        value = value % output_base ** k

    return out_digits