import re

re.su

import sys

try:
    for l in sys.stdin:
        if not l:
            break
        line = l.split()
        n = int(line[0])
        words = line[1:n + 1]
        w = line[-2]
        b = int(line[-1])
        b_words = []
        sw = sorted(list(w))
        for i in words:
            if w != i and sw == sorted(list(i)):
                b_words.append(i)
        if not b_words:
            print(0)
        else:
            print(len(b_words))
            print(list(sorted(b_words))[b - 1])
except:
    pass

