import re
import random

train_rate = 0.9
dev_rate = 0.05
tst_rate = 0.05
def write_file(en_sentence,vi_sentence,f_en,f_vi):
	for en_word, vi_word in zip(en_sentence.strip().split(),vi_sentence.strip().split()):
		if vi_word == "<num>" or vi_word == "pun" or en_word.lower() == vi_word.lower():
			continue
		char_list = " ".join(en_word.lower())
		f_en.write(char_list + "\n")
		char_list = " ".join(vi_word.lower())
		f_vi.write(char_list + "\n")
with open("sentence_pair_clean", "r") as f, \
	open("train_lm.en", "w") as f_en, \
	open("train_lm.vi", "w") as f_vi,\
	open("tst_lm_2012.en", "w") as f_dev_en, \
	open("tst_lm_2012.vi", "w") as f_dev_vi, \
	open("tst_lm_2013.en", "w") as f_tst_en, \
	open("tst_lm_2013.vi", "w") as f_tst_vi:
	for line in f:
		if line == "": continue
		line = line.strip().split("\t")
		en_sentence = line[0]
		vi_sentence = line[1]

		rate = random.random()
		if rate <= train_rate:
			write_file(en_sentence,vi_sentence,f_en,f_vi)
		elif rate <= train_rate + dev_rate:
			write_file(en_sentence,vi_sentence,f_dev_en,f_dev_vi)
		elif rate <= train_rate + dev_rate + tst_rate:
			write_file(en_sentence,vi_sentence,f_tst_en,f_tst_vi)

