# -*- coding: utf-8 -*-
def calnext(s):
    i = 0
    j = -1
    next = []
    next.append(-1)
    while (i < len(s) - 1):
        if (j == -1) | (s[i] == s[j]):
            i += 1
            j += 1
            next.append(j)
        else:
            j = next[j]
    return next


while True:
    try:
        m = list(map(str, input().strip().split()))
        s = list(map(str, input().strip().split()))
        next = calnext(s)
        #print(next)
        countMax = 0
        countCurrent = 0
        i = 0
        j = 0
        matchList = []
        matchMax = []
        matchLocation = -1
        location = -1
        while i < len(m):

            mf = m[i]
            sf = s[j]
            if mf == sf:
                i += 1
                j += 1
                countCurrent += 1
                matchList.append(mf)
            else:
                j = next[j]
                if j == -1:
                    i += 1
                    j = 0
                location = i
                matchList = []

            if len(matchList) > countMax:
                countMax = len(matchList)
                matchLocation = location
                matchMax = matchList
                #print(matchMax)

            if j == len(s):
                break
        print(matchMax, matchLocation)

    except EOFError:
        break
