import random

filename = "SICK.txt"
fin = open(filename, "r")

test_file = filename.split(".")
test_file[-2] += "_test"
test_file = ".".join(test_file[:-1] + ['xml'])
fout_test = open(test_file, "w")

train_file = filename.split(".")
train_file[-2] += "_train"
train_file = ".".join(train_file[:-1] + ['xml'])
fout_train = open(train_file, "w")

all_file = filename.split(".")
all_file[-2] += "_all"
all_file = ".".join(all_file[:-1] + ['xml'])
fout_all = open(all_file, "w")

test_id = random.sample(range(1, 10001), 3000)

for fout in [fout_all, fout_train, fout_test]:
    fout.write('''<?xml version="1.0" encoding="UTF-8"?>
<entailment-corpus lang="EN">
''')

for line in fin.readlines()[1:]:
    line = line.split('\t')
    if len(line) < 4:
        continue
    i = line[0]
    s1 = line[1]
    s2 = line[2]
    e = line[3].strip()
    if e not in ["ENTAILMENT"]:
        #e = "UNKNOWN"
        e = "NONENTAILMENT"
    output = '''<pair id="{}" entailment="{}" task="IR">
<t>{}</t>
<h>{}</h>
</pair>'''.format(i, e, s1, s2)
    if int(i) in test_id:
        fout_test.write(output)
    else:
        fout_train.write(output)
    fout_all.write(output)

for fout in [fout_all, fout_train, fout_test]:
    fout.write("</entailment-corpus>\n")
