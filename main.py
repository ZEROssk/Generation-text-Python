# -*- coding:utf-8 -*-
import random
import MeCab
import sys
import re
from glob import iglob

text_file = "./text_data/speech/asuka.txt"

def read_file(filepath):
    text_data = ""
    for path in iglob(filepath):
        with open(path, 'r') as f:
            text_data += f.read().strip()

    return text_data

def text_wakati(text):
    t = MeCab.Tagger('-Owakati')
    m = t.parse(text)
    result = m.rstrip(' \n').split(' ')

    return result

def first_word_dictionary(file_path):
    with open(file_path) as f:
        data = f.read()

    mecab = MeCab.Tagger()
    parse = mecab.parse(data)
    lines = parse.split("\n")
    items = (re.split("[\t,]", line) for line in lines)

    words = [item[0]
            for item in items
            if (item[0] not in ('EOS', '', 't', 'ー') and
                item[1] == '名詞' and item[2] == '一般')]

    print(words)

    first_word = random.choice(words)

    return first_word

def main_dictionary(txt):
    markov = {}
    w1 = ""
    w2 = ""

    for word in txt:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word

    return markov

def markov_generate_text(markov):
    generate_text = ""
    w1 = ""
    w2 = ""
    count = 0

    w1, w2 = random.choice(list(markov.keys()))
    while count < len(markov):
        tmp = random.choice(markov[(w1, w2)])
        generate_text += tmp
        w1, w2 = w2, tmp

        if '！' in tmp:
            break
        elif '？' in tmp:
            break
        elif '!' in tmp:
            break
        elif '?' in tmp:
            break
        elif '。' in tmp:
            break

        count += 1

    return generate_text

def main():
    read_text = read_file(text_file)
    base_text = text_wakati(read_text)
    dictionary = main_dictionary(base_text)
    test = first_word_dictionary(text_file)

    sentence = markov_generate_text(dictionary)
    print(sentence)

    #for i in range(50): 
    #    sentence = markov_generate_text(base_text)
    #    print(sentence)

if __name__ == "__main__":
    main()

