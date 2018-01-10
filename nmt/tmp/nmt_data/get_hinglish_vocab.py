# Collect all hinglish words in the corpus and save them as a vocab file.
import codecs


word_dict = dict()
with codecs.open("train_lm.vi", "r", encoding="utf-8") as f:
    for line in f.readlines():
        if line == "": continue
        line = line.strip()
        for word in line.split(" "):
            word_dict[word] = word_dict.get(word, 0) + 1

vocab = sorted(word_dict.items(), key=lambda x: -x[1])

with codecs.open("vocab_lm.vi", "w", encoding="utf-8") as f:

    f.write("<unk>" + "\n" + "<s>" + "\n" + "</s>" + "\n")
    for item in vocab:
        f.write(item[0] + "\n")
