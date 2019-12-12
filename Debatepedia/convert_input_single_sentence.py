import random
import string



def finish(buf, fout):
    if "entailment=\"NO\"" in buf[0]:
        buf[0] = buf[0].replace("entailment=\"NO\"", "entailment=\"NONENTAILMENT\"")
    elif "entailment=\"YES\"" in buf[0]:
        buf[0] = buf[0].replace("entailment=\"YES\"", "entailment=\"ENTAILMENT\"")

    sent = buf[1].split(">")[1].split("<")[0]
    first_tag = buf[1].split(">")[0] + '>'
    idi = int(first_tag.split('"')[1])
    last_tag = '<' + buf[1].split(">")[1].split("<")[1] + '>\n'
    buf[1] = []
    sents = sent.split(".")
    for i in range(len(sents)):
        if sents[i] == "":
            continue
        s = first_tag.split('"')[0] + '"' + str(idi*100+i) + '"' + first_tag.split('"')[2] + sents[i].translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))) + last_tag
        buf[1] += [s]

    sent = buf[2].split(">")[1].split("<")[0]
    first_tag = buf[2].split(">")[0] + '>'
    last_tag = '<' + buf[2].split(">")[1].split("<")[1] + '>\n'
    sent = sent.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    buf[2] = first_tag + sent + last_tag

    for i in range(len(buf[1])):
        idi = int(buf[0].split("topic")[0].split("id=")[1].split('"')[1])
        idi = idi*100 + i
        s = buf[0].split("id=")[0] + 'id="' + str(idi) + '" topic' + buf[0].split("topic")[1]

        fout.write(s)
        fout.write(buf[1][i])
        fout.write(buf[2])
        fout.write(buf[3])

    return len(buf[1])


filename = "debatepedia_train.xml"
fin_train = open(filename, "r")

train_file = filename.split(".")
train_file[-2] += "_converted_single_sentence"
train_file = ".".join(train_file[:-1] + ['xml'])
fout_train = open(train_file, "w")

filename = "debatepedia_test.xml"
fin_test = open(filename, "r")

test_file = filename.split(".")
test_file[-2] += "_converted_single_sentence"
test_file = ".".join(test_file[:-1] + ['xml'])
fout_test = open(test_file, "w")

for (fin, fout, name) in [(fin_test, fout_test, "test"),
                          (fin_train, fout_train, "train")]:
    count = 0
    buf = []
    for line in fin.readlines():
        if len(buf) == 0 and "<pair" in line:
            buf += [line]
        elif len(buf) != 0:
            buf += [line]

            if "</pair" in line:
                count += finish(buf, fout)
                buf = []
        else:
            fout.write(line)

    print("{} size: {}".format(name, count))
    fout.close()
