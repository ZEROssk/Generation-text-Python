# -*- coding:utf-8 -*-
import random
import MeCab
import re
import sys
import time
import os

#text_file_path = "./text_data/speech/asuka.txt"
#text_file_path = "./text_data/speech/ALL.txt"

def read_dictionary(path):

    return save_dic

def make_dictionary(file_path, data_name):
    lines_data = open(file_path, "r").readlines()
    main_dic_path = data_name + '/' + data_name + '_main.txt'
    noun_dic_path = data_name + '/' + data_name + '_noun.txt'
    main_dic = {}
    noun_dic = []

    #create dictionary
    for line in lines_data:
        #create main dictionary
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

        #create noun dictionary
        mecab_noun = (re.split(
                        '[\t,]',line
                        ) for line in (
                            MeCab.Tagger().parse(line).split('\n')))
        noun_list = list(mecab_noun)

        for i1,i2 in zip(noun_list,noun_list[1:2]):
            if i1[0] not in 'EOS' and i1[1] == '名詞' and i1[2] == 'サ変接続':
                noun_dic.append((i1[0], i2[0]))
            elif i1[0] not in 'EOS' and i1[1] == '名詞' and i1[2] == 'ナイ形容詞語幹':
                noun_dic.append((i1[0], i2[0]))
            elif i1[0] not in 'EOS' and i1[1] == '名詞' and i1[2] == '一般':
                noun_dic.append((i1[0], i2[0]))
            elif i1[0] not in 'EOS' and i1[1] == '名詞' and i1[2] == '形容動詞語幹':
                noun_dic.append((i1[0], i2[0]))
            elif i1[0] not in 'EOS' and i1[1] == '名詞' and i1[2] == '固有名詞':
                noun_dic.append((i1[0], i2[0]))
            elif i1[0] not in 'EOS' and i1[1] == '名詞' and i1[2] == '代名詞':
                noun_dic.append((i1[0], i2[0]))
            elif i1[0] not in 'EOS' and i1[1] == '名詞' and i1[2] == '副詞可能':
                noun_dic.append((i1[0], i2[0]))

    with open(main_dic_path, 'a') as f:
        f.write(str(main_dic))

    with open(noun_dic_path, 'a') as f:
        f.write(str(noun_dic))

    return main_dic, noun_dic

def markov_generate_text(dictionaries):
    generate_text = ""
    w1 = ""
    w2 = ""

    #select first word set
    w1, w2  = random.choice(dictionaries[1])
    generate_text += w1
    generate_text += w2

    while True:
        try:
            tmp = random.choice(dictionaries[0][(w1, w2)])
        except KeyError:
            print('KeyError')
            break

        generate_text += tmp
        w1, w2 = w2, tmp 
        if '！' in tmp or '!' in tmp or '？' in tmp or '?' in tmp or '。' in tmp:
            break

    return generate_text

def main():
    data_set_name = input('Pleas directory name: ')
    if os.path.exists(data_set_name):
        dic = read_dictionary(data_set_name)
        print('read data')
        #sentence = markov_generate_text(dic)
        #print(sentence)
    else:
        os.mkdir(data_set_name)
        print('mkdir')
        text_file_path = input('Pleas txt file path: ')
        print('input txt file path')
        dic = make_dictionary(text_file_path, data_set_name)
        sentence = markov_generate_text(dic)
        print(sentence)

    #for num in range(100):
    #    sentence = markov_generate_text(dic)
    #    print(num,sentence)

if __name__ == "__main__":
    start = time.time()
    main()
    elapsed_time= time.time() - start
    print('elapsed_time:{0}'.format(elapsed_time) + '[sec]')

