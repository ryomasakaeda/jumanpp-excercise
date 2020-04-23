import sys
from pyknp import Juman
juman=Juman()

input_sentence=sys.stdin.readline()
result=juman.analysis(input_sentence)

for mrph in result.mrph_list():
    print(mrph.midasi,end=" ")
print()