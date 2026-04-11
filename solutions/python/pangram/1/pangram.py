def is_pangram(sentence):
    letters = set()

    for x in sentence.lower():
        if 'a' <= x <= 'z':
            letters.add(x)

    return len(letters) == 26
