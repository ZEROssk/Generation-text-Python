while count < len(txt):
    tmp = random.choice(markov[(w1, w2)])
    if count == 0:
        if '！' in tmp:
            continue
        elif '？' in tmp:
            continue
        elif '!' in tmp:
            continue
        elif '?' in tmp:
            continue
        elif '。' in tmp:
            continue
        elif '、' in tmp:
            continue

