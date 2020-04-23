from pyknp import Juman
import sys

juman=Juman()

data=""
count_all=0
count_jyutugo=0
for line in iter(sys.stdin.readline,""):
    if line.strip()=="EOS":
        result=juman.result(data)
        for mrph in result.mrph_list():
            count_all+=1
            if mrph.hinsi=="動詞" or (mrph.hinsi=="形容詞"and"イ形容詞" in mrph.katuyou1) or (mrph.hinsi=="形容詞" and"ナ形容詞" in mrph.katuyou1):
                print(mrph.hinsi)
                count_jyutugo+=1

        data=""
    else:
        data+=line
print(count_all)
print(count_jyutugo)
print(count_jyutugo/count_all)