# Collect all hinglish words in the corpus and save them as a vocab file.
import codecs
count =0

with codecs.open("correct_output", "r", encoding="utf-8") as f, \
		codecs.open("correct_input", "r", encoding="utf-8") as f1:
    for (line, line1) in zip(f.readlines(), f1.readlines()):
        
        line = line.strip()
        line1 = line1.strip()
        if line != line1:
        	print(line + "|#|" + line1)
        	count += 1
    print(count)

