from pyknp import Juman
import sys

juman=Juman()
data=""
flag=False
word=""

for line in iter(sys.stdin.readline,""):
    if line.strip()=="EOS":
        result=juman.result(data)
        for mrph in result.mrph_list():
            if flag and (mrph.genkei=="する" or mrph.genkei=="できる"):
                # print(mrph.midasi)
                print(word+mrph.midasi)
            flag=False
            word=""
            if mrph.bunrui=="サ変名詞":
                flag=True
                # print(mrph.bunrui)
                word=mrph.midasi
        data=""
    
    else:
        data+=line