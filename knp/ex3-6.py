from pyknp import Juman
import sys

juman=Juman()
data=""
flag_noun=False
flag_no=False
word=""

for line in iter(sys.stdin.readline,""):
    if line.strip()=="EOS":
        result=juman.result(data)
        for mrph in result.mrph_list():
            if flag_noun and mrph.midasi=="の":
                flag_noun=False
                words+="の"
                flag_no=True
            elif flag_no and mrph.hinsi=="名詞":
                words+=mrph.midasi
                flag_no=False
                print(words)
            elif mrph.hinsi=="名詞":
                flag_noun=True
                words=mrph.midasi
        data=""
    
    else:
        data+=line