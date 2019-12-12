import json
import string

train_filename_in = "snli_1.0_train.jsonl"
test_filename_in = "snli_1.0_test.jsonl"
train_filename_out = "snli_train.xml"
test_filename_out = "snli_test.xml"

train_fin = open(train_filename_in, "r")
test_fin = open(test_filename_in, "r")
train_fout = open(train_filename_out, "w")
test_fout = open(test_filename_out, "w")

train_fout.write('''<?xml version="1.0" encoding="UTF-8"?>
<entailment-corpus lang="EN">
''')
test_fout.write('''<?xml version="1.0" encoding="UTF-8"?>
<entailment-corpus lang="EN">
''')

cur_id = 1
for (file_in, file_out) in [(train_fin, train_fout), (test_fin, test_fout)]:
    for line in file_in:
        data = json.loads(line)

        if len(data) == 0:
            continue

        i = cur_id
        cur_id += 1
        s1 = data["sentence1"].translate(str.maketrans('', '', string.punctuation))
        s2 = data["sentence2"].translate(str.maketrans('', '', string.punctuation))
        e = data["gold_label"].strip().upper()
        if e not in ["ENTAILMENT"]:
            e = "NONENTAILMENT"
        output = '''<pair id="{}" entailment="{}" task="IR">
<t>{}</t>
<h>{}</h>
</pair>'''.format(i, e, s1, s2)
        file_out.write(output)


train_fout.write("</entailment-corpus>\n")
test_fout.write("</entailment-corpus>\n")



