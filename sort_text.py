# -*- coding:utf-8 -*-

import re
import sys
import os

path = './eva.txt'

with open(path) as f:
    text_data = f.readlines()

text = [line.strip() for line in text_data]

for line in text:
    name = line[:line.find("「")]
    file_path = './text_data/ALL.txt'#'./text_data/' + name + '.txt'

    text_line_base = line[line.find("「") + 1:line.find("」")] + '\n'
    text_line = text_line_base

    if os.path.exists(file_path):
        write = open(file_path, "a")
        write.write(text_line)
        print("write: ", text_line)
    else:
        new_file = open(file_path, "w")
        new_file.write(text_line)
        print("write: ", text_line)

