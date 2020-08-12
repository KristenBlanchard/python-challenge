# import data modules
import re

# file path/open
text_path = "PyParagraph/Resources/paragraph_1.txt"

letter_count = []
words_per_sentence = []

with open(text_path) as text:
    paragraph = text.read()

# approx. word count
word_split = paragraph.split(" ")
word_count = len(word_split)

# approx sentence count

# re-split paragraph based on sentances
sentence_split = re.split("(?<=[.!?]) +", paragraph)

# sum up sentence count
sentence_count = len(sentence_split)

# loop through the words
for word in word_split:

    # append letter count in list
    letter_count.append(len(word))


# approx. letter count per word
approx_letter_count = sum(letter_count) / len(letter_count)

# loop through sentence split for words
for sentence in sentence split:




