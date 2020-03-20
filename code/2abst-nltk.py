import nltk
import sys

from nltk import sent_tokenize

fname4 = "CTD-AB-sen.txt"
fw4 = open(fname4, 'w', encoding='UTF-8')
fname = "CTD-AB.txt"
fr = open(fname, 'r', encoding='UTF-8')
abstracts = fr.read().strip().split("\n")
count = 0
for abstract in abstracts:
    # print abstract

    values = abstract.strip().split("\t")
    if len(values) == 2:
        pmid = values[0]
        text = values[1]

        # print "0: ",pmid
        # print "1: ",text
        sentences = sent_tokenize(text)
        sent_count = 0
        sent_start = 0

        for sentence in sentences:
            #print sentence
            sent_len = len(sentence)
            sent_end = sent_start + sent_len
            # print "sent_start: ", sent_start, "; ", "sent_end: ", sent_end

            fw4.write(pmid + "\t" + "sen_" + str(sent_count) + "\t" + str(sent_start) + "\t" + str(
                sent_end) + "\t" + sentence + "\n")

            sent_start = sent_end + 1
            sent_count = sent_count + 1
    else:

        fw4.write(str(values[0]) + "\n")
