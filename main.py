# -*- coding:utf-8 -*-
import random
import MeCab

text_file_path = "./text_data/speech/asuka.txt"
#text_file = "./text_data/speech/ALL.txt"

def dic(file_path):
    lines_data = open(file_path, "r").readlines()
    markov_dic = {}

    for line in lines_data:
        mecab = MeCab.Tagger(
                '-Owakati'
                    ).parse(line).rstrip(' \n').split(' ')
        w1 = ""
        w2 = ""

        for word in mecab:
            if w1 and w2:
                if (w1, w2) not in markov_dic:
                    markov_dic[(w1, w2)] = []
                markov_dic[(w1, w2)].append(word)
            w1, w2 = w2, word

    return markov_dic

def markov_generate_text(markov):
    generate_text = ""
    w1 = ""
    w2 = ""
    count = 0

    while True:
        w1, w2  = random.choice(list(markov.keys()))
        if '！' in w1 or '？' in w1 or '!' in w1 or '?' in w1 or '。' in w1 or '、' in w1 or '・' in w1:
            print('skip ',w1,w2)
            continue
        elif '！' in w2 or '？' in w2 or '!' in w2 or '?' in w2 or '。' in w2:
            print('skip ',w1,w2)
            continue
        else:
            generate_text += w1
            generate_text += w2
            print('generate ',generate_text)
            break

    while True:#count < len(markov):
        try:
            tmp = random.choice(markov[(w1, w2)])
        except KeyError:
            print('KeyError')
            break
        generate_text += tmp
        w1, w2 = w2, tmp

        if '！' in tmp or '!' in tmp or '？' in tmp or '?' in tmp or '。' in tmp:
            break

    return generate_text

def main():
    dic_text = dic(text_file_path)

    #sentence = markov_generate_text(dic_text)
    #print(sentence)

    for num in range(1000):
        sentence = markov_generate_text(dic_text)
        print(num,sentence)

if __name__ == "__main__":
    main()

