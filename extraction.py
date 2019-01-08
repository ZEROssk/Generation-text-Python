import MeCab
import sys
import re
#from collections import Counter

# ファイル読み込み
#cmd, infile = sys.argv
infile = "./text_data/asuka.txt"
with open(infile) as f:
    data = f.read()

# パース
mecab = MeCab.Tagger()
parse = mecab.parse(data)
lines = parse.split('\n')
items = (re.split('[\t,]', line) for line in lines)



# 名詞をリストに格納
words = [item[0]
         for item in items
         if (item[0] not in ('EOS', '', 't', 'ー') and
             item[1] == '名詞' and item[2] == '一般')]
print(words)

# 頻度順に出力
#counter = Counter(words)
#for word, count in counter.most_common():
#    print(f"{word}: {count}")
