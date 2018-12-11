# -*- coding:utf-8 -*-
import random
import MeCab
from glob import iglob

def text_wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")

    return result

def load_file(filepath):
    text_data = ""
    for path in iglob(filepath):
        with open(path, 'r') as f:
            text_data += f.read().strip()

    return text_data

def main():
    base_text = load_file('./*.txt')

    base_text = text_wakati(base_text)

    print(base_text)

#def main():
#    filepath_list = glob.glob('./*.txt')
#
#    for filename in filepath_list:
#        with open(filename, "r") as input:
#            test = input.read()
#
#        wordlist = text_wakati(test)
#    #wordlist = text_wakati(test)
#    markov = {}
#    w1 = ""
#    w2 = ""
#
#    for word in wordlist:
#        if w1 and w2:
#            if (w1, w2) not in markov:
#                markov[(w1, w2)] = []
#            markov[(w1, w2)].append(word)
#        w1, w2 = w2, word
#    count = 0
#    sentence = ""
#    w1, w2  = random.choice(list(markov.keys()))
#
#    while count < len(wordlist):
#        tmp = random.choice(markov[(w1, w2)])
#        sentence += tmp
#        w1, w2 = w2, tmp
#        count += 1
#    print(sentence)

if __name__ == "__main__":
    main()
