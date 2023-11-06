# 3. Split the following irregular sentence into words
import re
sentence = """A, very   very; irregular_sentence"""
#desired_output = "A very very irregular sentence"
print(re.split('[;,_ \s]+',sentence))
print('\n')
print(" ".join(re.split('[;,_ \s]+', sentence)),end='.')

#print(re.sub('\s+',' ',sentence)) ayrica extra whitespace bu sekilde de yok edilebilir

#print(" ".join(re.split('[;,_ s]+', sentence))) #bu haliyle 's' harfini cumleden siler
