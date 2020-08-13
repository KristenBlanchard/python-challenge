# import data modules
import re

# file path/open
text_path = "PyParagraph/Resources/paragraph_2.txt"

paragraph = ""
letter_count = []
words_per_sentence = []

with open(text_path) as text:
    paragraph = text.read().replace("\n", " ")

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
for sentence in sentence_split:

    # find out how many of words per sentance
    words_per_sentence.append(len(sentence.split(" ")))

# find the average of the words per sentence
average_sentence = sum(words_per_sentence) / float(len(words_per_sentence))

# output
output = (
     f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {approx_letter_count}\n"
    f"Average Sentence Length: {average_sentence}\n")

# print statements
print(output)


# export to textfile
file_output = 'PyParagraph/Analysis/Paragraph2_Analysis.txt'

with open(file_output, "w") as txtfile:
    txtfile.write(output)