full_colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def value(colors):
    first = full_colors.index(colors[0])
    second = full_colors.index(colors[1])
    return int(str(first) + str(second))
