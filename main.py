# -*- coding:utf-8 -*-
import random
import MeCab
from glob import iglob

def text_wakati(text):
    t = MeCab.Tagger('-Owakati')
    m = t.parse(text)
    result = m.rstrip(' \n').split(' ')

    return result

def load_file(filepath):
    text_data = ""
    for path in iglob(filepath):
        with open(path, 'r') as f:
            text_data += f.read().strip()

    return text_data

def markov_generate_text(txt):
    markov = {}
    count = 0
    w1 = ""
    w2 = ""
    generate_text = ""

    for word in txt:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word

    w1, w2  = random.choice(list(markov.keys()))

    while count < 15:#len(txt):
        tmp = random.choice(markov[(w1, w2)])
        generate_text += tmp
        w1, w2 = w2, tmp
        print(tmp,w1,w2)
        count += 1

    return generate_text

def main():
    base_text = load_file('./text_data/アスカ.txt')

    base_text = text_wakati(base_text)

    sentence = markov_generate_text(base_text)
    print(sentence)

   # for i in range(1): 
   #     sentence = markov_generate_text(base_text)
   #     print(sentence)

if __name__ == "__main__":
    main()
