import random
import string

filename = "debatepedia_train.xml"
fin_train = open(filename, "r")

train_file = filename.split(".")
train_file[-2] += "_converted_with_and"
train_file = ".".join(train_file[:-1] + ['xml'])
fout_train = open(train_file, "w")

filename = "debatepedia_test.xml"
fin_test = open(filename, "r")

test_file = filename.split(".")
test_file[-2] += "_converted_with_and"
test_file = ".".join(test_file[:-1] + ['xml'])
fout_test = open(test_file, "w")

for (fin, fout) in [(fin_test, fout_test), (fin_train, fout_train)]:
    count = 0
    for line in fin.readlines():
        if "entailment=\"NO\"" in line:
            count += 1
            line = line.replace("entailment=\"NO\"", "entailment=\"NONENTAILMENT\"")
        elif "entailment=\"YES\"" in line:
            count += 1
            line = line.replace("entailment=\"YES\"", "entailment=\"ENTAILMENT\"")

        if "<t" in line or "<h" in line:
            sent = line.split(">")[1].split("<")[0]
            first_tag = line.split(">")[0] + '>'
            last_tag = '<' + line.split(">")[1].split("<")[1] + '>\n'
            sent = " and ".join(sent.split(".")[:-1])
            sent = sent.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
            line = first_tag + sent + last_tag
        fout.write(line)
    print(count)

