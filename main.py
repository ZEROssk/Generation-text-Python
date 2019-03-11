# -*- coding:utf-8 -*-
import random
import MeCab
import re
import sys
import time
import os
import json
import csv
import ast

data_set_name = input('Pleas directory name: ')
main_dic_path = data_set_name + '/' + data_set_name + '_main.json'
noun_dic_path = data_set_name + '/' + data_set_name + '_noun.csv'
#text_file_path = "./text_data/eva/asuka.txt"
#text_file_path = "./text_data/eva/ALL.txt"

def read_dictionary():
    with open(main_dic_path) as f:
        rmd = json.load(f)
        read_main_dic = ast.literal_eval(rmd['test'])
        print(type(read_main_dic))

    with open(noun_dic_path) as f:
        read_noun_dic = []
        rnd = csv.reader(f)
        for r in rnd:
            read_noun_dic.append((r[0], r[1]))

    return read_main_dic, read_noun_dic

def write_dictionary_data(data_name):
    with open(main_dic_path, 'w') as f:
        write_main_dic = {"test":str(data_name[0])}
        json.dump(write_main_dic, f, indent=4)

    with open(noun_dic_path, 'w') as f:
        writer = csv.writer(f, lineterminator = '\n')
        for wnd in data_name[1]:
            write_noun_dic = list(wnd)
            writer.writerow(write_noun_dic)

    return write_main_dic, write_noun_dic

def make_dictionary(file_path):
    lines_data = open(file_path, "r").readlines()
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

    return main_dic, noun_dic

def markov_generate_text(dictionaries):
    generate_text = ""
    w1 = ""
    w2 = ""

    #select first word set
    w1, w2  = random.choice(dictionaries[1])
    print(w1,w2)
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
    if os.path.exists(data_set_name):
        dic = read_dictionary()
        for num in range(100):
            sentence = markov_generate_text(dic)
            print(num,sentence)
    else:
        os.mkdir(data_set_name)
        text_file_path = input('Pleas txt file path: ')
        dic = make_dictionary(text_file_path)
        write_dic = write_dictionary_data(dic)
        sentence = markov_generate_text(dic)
        print(sentence)

if __name__ == "__main__":
    start = time.time()
    main()
    elapsed_time= time.time() - start
    print('elapsed_time:{0}'.format(elapsed_time) + '[sec]')

