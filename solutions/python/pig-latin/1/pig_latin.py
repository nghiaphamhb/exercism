def translate_word(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = text.strip()

    # rule 1
    if text[0] in vowels or text[:2] in ['xr', 'yt']: 
        return text + 'ay'

    i = 0
    while i < len(text):
        # rule 3
        if text[i:i+2] == 'qu':
            return text[i+2:] + text[:i+2] + 'ay'

        # rule 4
        if text[i] == 'y' and i != 0:
            break

        # rule 2
        if text[i] in vowels:
            break
            
        i += 1
            
    return text[i:] + text[:i] + 'ay'
        
def translate(text):
    words = text.strip().split()
    return ' '.join(translate_word(w) for w in words)
    
