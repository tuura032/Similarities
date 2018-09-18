from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    asplit = a.splitlines()
    bsplit = b.splitlines()

    return set(asplit).intersection(bsplit)

def sentences(a, b):
    """Return sentences in both a and b"""

    asent = sent_tokenize(a)
    bsent = sent_tokenize(b)

    return set(asent).intersection(bsent)

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    s = a
    make = set()
    for i in range((len(s))-(n-1)):
        s = s.lstrip('\n')
        sub = s[:n]
        s = s[1:]
        if len(sub) == n:
            if sub in b:
                make.add(sub)
    return make