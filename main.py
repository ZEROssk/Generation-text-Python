# -*- coding:utf-8 -*-
import random
import MeCab
import re
import sys

text_file_path = "./text_data/speech/asuka.txt"
#text_file = "./text_data/speech/ALL.txt"

def noun_dictionary(file_path):
    lines_data = open(file_path, "r").readlines()
    words = []
    print(dic)

    for line in lines_data:
        noun = MeCab.Tagger().parse(line).split('\n')
        items = (re.split('[\t,]', line)for line in noun)

        for item in items:
            if item[0] not in 'EOS' and item[1] == '名詞' and item[2] == 'サ変接続':
                words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == 'ナイ形容詞語幹':
                words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '一般':
                words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '形容動詞語幹':
                words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '固有名詞':
                words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '代名詞':
                words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '副詞可能':
                words.append(item[0])

    print(words)

def main_dictionary(file_path):
    lines_data = open(file_path, "r").readlines()
    main_dic = {}
    noun_words = []

    for line in lines_data:
        mecab = MeCab.Tagger(
               '-Owakati'
                    ).parse(line).rstrip(' \n').split(' ')
        w1 = ""
        w2 = ""

        for word in mecab:
            if w1 and w2:
                if (w1, w2) not in main_dic:
                    main_dic[(w1, w2)] = []
                main_dic[(w1, w2)].append(word)
            w1, w2 = w2, word

        noun = MeCab.Tagger().parse(line).split('\n')
        mecab_noun = (re.split('[\t,]', line)for line in noun)

        for item in mecab_noun:
            if item[0] not in 'EOS' and item[1] == '名詞' and item[2] == 'サ変接続':
                noun_words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == 'ナイ形容詞語幹':
                noun_words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '一般':
                noun_words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '形容動詞語幹':
                noun_words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '固有名詞':
                noun_words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '代名詞':
                noun_words.append(item[0])
            elif item[0] not in 'EOS' and item[1] == '名詞' and item[2] == '副詞可能':
                noun_words.append(item[0])

    return main_dic, noun_words

def markov_generate_text(markov):
    generate_text = ""
    w1 = ""
    w2 = ""
    count = 0

    while True:
        w1, w2  = random.choice(list(markov[0].keys()))
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
            tmp = random.choice(markov[0][(w1, w2)])
        except KeyError:
            print('KeyError')
            break

        generate_text += tmp
        w1, w2 = w2, tmp 
        if '！' in tmp or '!' in tmp or '？' in tmp or '?' in tmp or '。' in tmp:
            break

    return generate_text

def main():
    #noun_dic = noun_dictionary(text_file_path)
    dic= main_dictionary(text_file_path)

    sentence = markov_generate_text(dic)
    print(sentence)

    #for num in range(1000):
    #    sentence = markov_generate_text(dic_text)
    #    print(num,sentence)

if __name__ == "__main__":
    main()

