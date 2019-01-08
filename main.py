# -*- coding:utf-8 -*-
import random
import MeCab
from glob import iglob

def text_wakati(text):
    t = MeCab.Tagger('-Owakati')
    m = t.parse(text)
    result = m.rstrip(' \n').split(' ')

    return result

def first_word_check(first_word):
    filter="名詞"
    check = 0
    mecab = MeCab.Tagger('mecabrc')
    node = mecab.parseToNode(first_word)

    if node.feature.startswith(filter):
        print('名詞')
        check = 1
    else:
        print('NO')
        check = 0

    return check

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

    #辞書作成
    for word in txt:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word

    w1, w2  = random.choice(list(markov.keys()))

    #文章の生成
    while count < 10:#len(txt):
        tmp = random.choice(markov[(w1, w2)])
        print(count)
        print(w1, w2, tmp)
        if count == 0:
            check = first_word_check(tmp)
            print(check)
            if check == 0:
                w1, w2 = w2, tmp
                print('continue')
                continue

            #if '！' in tmp:
            #    print("test！")
            #    continue

            #elif '？' in tmp:
            #    print("test？")
            #    continue

            #elif '!' in tmp:
            #    print("test!")
            #    continue

            #elif '?' in tmp:
            #    print("test?")
            #    continue

            #elif '。' in tmp:
            #    print("test。")
            #    continue

            #elif '、' in tmp:
            #    print("test、")
            #    continue

        generate_text += tmp
        w1, w2 = w2, tmp
        print(w1, w2, '=', w2, tmp)
        count += 1
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

    return generate_text

def main():
    base_text = load_file('./text_data/ALL.txt')
    #base_text = load_file('./text_data/asuka.txt')

    base_text = text_wakati(base_text)

    sentence = markov_generate_text(base_text)
    print(sentence)

    #for i in range(50): 
    #    sentence = markov_generate_text(base_text)
    #    print(sentence)

if __name__ == "__main__":
    main()

