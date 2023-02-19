import os
from os.path import basename, isfile, join
from collections import Counter
import socket

output_string = ""

# a. List all text files in directories
output_string += f"1. All files in '{basename(os.getcwd())}':\n"

for f in os.listdir("."):
  if isfile(join(".", f)) and f.endswith(".txt"):
    output_string += f"{f}\n"

#b and #c. Count number of words in each file, and the grand total
total_word_count = 0
IF_words = [] # Save all the words in the "IF.txt" file to count frequency later
output_string += "2. Count number of words:\n"
with open(join(".", "IF.txt")) as IFfile:
  word_count_in_file = 0
  for line in IFfile:
    words = line.split()
    IF_words.extend(words)
    word_count_in_file += len(words)
  output_string += f"Word count in IF.txt is: {word_count_in_file}\n"
  total_word_count += word_count_in_file

with open(join(".", "Limerick.txt")) as LimerickFile:
  word_count_in_file = 0
  for line in LimerickFile:
    words = line.split()
    word_count_in_file += len(words)
  output_string += f"Word count in Limerick.txt is: {word_count_in_file}\n"
  total_word_count += word_count_in_file

output_string += f"Total word count in 2 files is: {total_word_count}\n"

#d. Count top 3 words with highest frequency in "IF.txt"
output_string += "3. Word frequency in IF.txt\n"
word_freq = Counter(IF_words)
# Sort the word_freq by the value
top_3_highest = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]
output_string += "Top 3 words with maximum number of counts in IF.txt are:\n"
for word, freq in top_3_highest:
  output_string += f"* {word}: {freq}\n"

#e. Find IP address of machine
# I did not know if the assignment want external IP address or Local Ip address. I chose "local"
hostname = socket.gethostname()    
IP_address = socket.gethostbyname(hostname)    
output_string += f"4. Your Computer Local IP Address is: {IP_address}\n"


print(output_string)

with open(join(".", "result.txt"), "w") as result_file:
  result_file.write(output_string)