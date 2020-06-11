import string

results = []
with open("train7.article") as f:
    for raw_line in f:
        line = raw_line.strip()
        line = line.replace('\"', '')
        line = line.translate(str.maketrans({key: " {0} ".format(key) for key in string.punctuation}))
        line = ' '.join(line.split())
        line = line.replace(' .', ' . <S_SEP>')
        line = line + " <S_SEP>"
        results.append(line)

with open("train.article", "w") as f:
    f.write('\n'.join(results))