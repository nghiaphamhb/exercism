def is_isogram(string):
    str_without_sign = ''.join(c for c in string if c != ' ' and c != '-')
    arr = [c for c in str_without_sign.lower()]
    my_set = set(arr)
    return len(my_set) == len(str_without_sign)
