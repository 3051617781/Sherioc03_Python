def kmp_search(string, patt):
    next = next_build(patt)
    i = 0 #string pointer
    j = 0 #patt pointer
    while i < len(string):
        if string[i] == patt[j]:
            i += 1
            j += 1
        elif j > 0:
            j = next[j-1]
        else: #j = 0, failed in the first char
            i += 1

        if j == len(patt): #j point the next-position of the patt 's last word  
            return i - j
    return -1 #not search


def next_build(patt):
    next = [0]
    i = 1 #patt pointer
    prefix_len = 0
    while i < len(patt):
        if patt[i] == patt[prefix_len]:
            prefix_len += 1
            next.append(prefix_len) #next[i] = prefix_len
            i += 1
        elif prefix_len > 0:
            prefix_len = next[prefix_len-1]
        else:
            next.append(0) #next[i] = 0
            i += 1
    return next