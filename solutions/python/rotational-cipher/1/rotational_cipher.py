def rotate(text, key):
    ch = [c for c in text.strip()]
    for i in range(len(ch)):
        if ch[i].isalpha():
            base = ''
            if ch[i].islower():
                base = 'a'
            else:
                base = 'A'
                
            temp = (ord(ch[i]) - ord(base)) + key
            temp = temp % 26 + ord(base)
            ch[i] = chr(temp)
    return ''.join(ch)
