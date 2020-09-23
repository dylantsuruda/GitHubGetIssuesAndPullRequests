import os
from collections import Counter


target_directory = "GitHubInfo-NotepadPlusPlus"
target_file = "issuestitleplain.txt"
target_filepath = os.path.join(target_directory, target_file)

with open(target_filepath, "r", encoding="utf-8") as file:
    text = file.read()

text = text.replace("-D-E-L-I-M-I-T-E-R-", "")
text_list = text.split()  # Splits on all whitespace

word_freq = Counter(text_list)

i = 1
print("Twenty most frequent terms in Notepad++ issue titles:")
for word, freq in word_freq.most_common(20):
    print("#" + str(i) + ": ", end="")
    print(word + " (frequency = " + str(freq) + ")")
    i += 1
