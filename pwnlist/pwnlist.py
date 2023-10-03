#!/usr/bin/env python3

pwlist = ["dumbledore", "hermione"]
charlist = ["@", "$", "!"]
mutatedlist = []
charmutlist = []
finallist = []

for pwtmp in pwlist:
    mutatedlist.append(pwtmp)
    mutatedlist.append(pwtmp.capitalize())

for x in [1,2,3,4,5,6,7,8,9,0]:
    for chartmp in charlist:
        charmutlist.append(str(x) + chartmp)
        charmutlist.append(chartmp + str(x))

for a in mutatedlist:
    for b in charmutlist:
        finallist.append(str(a)+str(b))

for x in finallist:
    print(x)