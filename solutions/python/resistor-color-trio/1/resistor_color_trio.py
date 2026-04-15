full_colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def label(colors):
    first_index = full_colors.index(colors[0])
    second_index = full_colors.index(colors[1])
    third_index = full_colors.index(colors[2])
    
    number = int(str(first_index) + str(second_index))
    power = 10 ** third_index
    value = number * power

    level = 0
    unit = ''
    while value % 1000 == 0 and value > 0:
        value = value // 1000
        level += 1

    if level == 1:
        unit = 'kiloohms'
    elif level == 2:
        unit = 'megaohms'
    elif level == 3:
        unit = 'gigaohms'
    else:
        unit = 'ohms'
    
    return ' '.join([str(value), unit])
    
