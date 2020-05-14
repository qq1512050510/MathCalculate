# -*- coding: utf-8 -*-
while True:
    try:
        iList = list(map(int,input().strip().split()))
        print(iList[0]+iList[1])
    except EOFError:
        break
