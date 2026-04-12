def response(hey_bob):
    sayings = hey_bob.strip()
    if not sayings:
        return 'Fine. Be that way!'
    elif sayings.isupper() and sayings[-1] == '?':
        return "Calm down, I know what I'm doing!"
    elif sayings.isupper():
        return 'Whoa, chill out!'
    elif sayings[-1] == '?':
        return 'Sure.'
    else: 
        return 'Whatever.'