# -*- coding:utf-8 -*-
import random
import MeCab
import sys
import re
from glob import iglob
import inspect

text_file = "./text_data/speech/asuka.txt"
#text_file = "./text_data/speech/ALL.txt"

#def read_file(filepath):
#    text_data = ""
#    for path in iglob(filepath):
#        with open(path, 'r') as f:
#            text_data += f.read().strip()
#
#    return text_data
#
#def text_wakati(text):
#    t = MeCab.Tagger('-Owakati')
#    m = t.parse(text)
#    result = m.rstrip(' \n').split(' ')
#
#    return result

#def first_word(sorce_data):
#    with open(text_file) as f:
#        data = f.read()
#
#    mecab = MeCab.Tagger()
#    parse = mecab.parse(data)
#    lines = parse.split("\n")
#    items = (re.split("[\t,]", line) for line in lines)
#
#    words = [item[0]
#            for item in items
#            if (item[0] not in ('EOS', '', 't', 'ー') and
#                item[1] == '名詞' and item[2] == '一般')]
#
#    f_word_dictionary = []
#    print(sorce_data)
#    for sorce in sorce_data:
#        print(sorce)
#        for comparison in words:
#            if sorce in comparison:
#                print('done')
#                f_word_dictionary.append(sorce)
#
#    return f_word_dictionary

def dic(fil):
    data = open(text_file, "r")
    lines = data.readlines()
    markov = {}
    for line in lines:
        t = MeCab.Tagger('-Owakati')
        m = t.parse(line)
        result = m.rstrip(' \n').split(' ')
        w1 = ""
        w2 = ""        
        for word in result:
            if w1 and w2:
                if (w1, w2) not in markov:
                    markov[(w1, w2)] = []
                markov[(w1, w2)].append(word)
            w1, w2 = w2, word

        return markov
    data.close()

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
    check = 0

    while True:
        w1, w2  = random.choice(list(markov.keys()))
        if '！' in w1:
            print('skip ',w1,w2)
            continue
        elif '？' in w1:
            print('skip ',w1,w2)
            continue
        elif '!' in w1:
            print('skip ',w1,w2)
            continue
        elif '?' in w1:
            print('skip ',w1,w2)
            continue
        elif '。' in w1:
            print('skip ',w1,w2)
            continue
        elif '、' in w1:
            print('skip ',w1,w2)
            continue
        elif '！' in w2:
            print('skip ',w1,w2)
            continue
        elif '？' in w2:
            print('skip ',w1,w2)
            continue
        elif '!' in w2:
            print('skip ',w1,w2)
            continue
        elif '?' in w2:
            print('skip ',w1,w2)
            continue
        elif '。' in w2:
            print('skip ',w1,w2)
            continue
        else:
            break
            generate_text += w1,w2
            print('generate ',generate_text)

    #first_word_tmp = first_word(str(markov))
    #print(first_word_tmp)

    while count < len(markov):
        tmp = random.choice(markov[(w1, w2)])
        #print(tmp)
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
    #read_text = read_file(text_file)
    #base_text = text_wakati(read_text)
    #dictionary = main_dictionary(base_text)
    text = dic(text_file)

    #sentence = markov_generate_text(dictionary)
    #print(sentence)

    #for num in range(1000000):
    #    sentence = markov_generate_text(dictionary)
    #    print(num,sentence)

if __name__ == "__main__":
    main()

