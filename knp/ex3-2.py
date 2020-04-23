from pyknp import Juman
import sys

juman = Juman()

data = ""
for line in iter(sys.stdin.readline, ""): # 解析結果ファイルを1行ずつ読む
    if line.strip() == "EOS": # 1文の解析結果を読み込んだら
        result = juman.result(data) # 内部構造に変換
        for mrph in result.mrph_list():
            if mrph.hinsi=="動詞":
                print(mrph.genkei)
        data=""
    else:
        data+=line

# for line in iter(sys.stdin.readline,""):
#     result=juman.result(line)
#     for mrph in result.mrph_list():
#         if mrph.hinsi=="動詞":
#             print(mrph.genkei)
    