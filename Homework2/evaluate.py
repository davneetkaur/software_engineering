# evaluate a string

def parse_integer(s):
    i = int(s)
    return i

def parse_float(s):
    i = float(s)
    return i

def parse_string(s):
    i = str(s).lower()
    return i

def evaluate_string(s):
    try:
        st = parse_string(s)
        if any(i in st for i in 'aeiou'):
            return True
        else:
            return False
    except ValueError:
        return False