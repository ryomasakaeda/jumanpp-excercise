from pyknp import Juman
import sys
from collections import Counter

juman=Juman()

data=""
list=[]
for line in iter(sys.stdin.readline,""):
    if line.strip()=="EOS":
        result=juman.result(data)
        for mrph in result.mrph_list():
            # print(mrph.midasi)
            list.append(mrph.midasi)
        data=""
    else:
        data+=line

c=Counter(list)
c=sorted(c.items(),key=lambda x:x[1],reverse=True)
print(c)

    