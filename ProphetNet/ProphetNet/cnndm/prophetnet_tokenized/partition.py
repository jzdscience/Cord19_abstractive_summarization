with open("all.tgt") as f:
    lines = f.readlines()

with open("train.tgt", "w") as f:
    f.write(''.join(lines[:-400]))

with open("valid.tgt", "w") as f:
    f.write(''.join(lines[-400:-200]))

with open("test.tgt", "w") as f:
    f.write(''.join(lines[-200:]))
