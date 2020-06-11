predicted = []
actual = []
remainder = 0
with open("output_ck3_pelt1.2_test_beam5_9_processed.txt") as f:
    for line in f:
        remainder = (remainder + 1) % 4
        if remainder == 2:
            line_processed = line.strip()
            line_processed = line_processed.split('\t')[1]
            actual.append(line_processed)

        if remainder == 3:
            line_processed = line.strip()
            line_processed = line_processed.split('\t')[2]
            predicted.append(line_processed)

with open("test_9.tgt", "w+") as f:
    f.write('\n'.join(actual))

with open("test_9.decodes", "w+") as f:
    f.write('\n'.join(predicted))