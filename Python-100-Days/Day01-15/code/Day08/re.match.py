import re

text = """
101 COM   Computers
205 MAT   Mathematics
189 ENG   English
206 HIS   History
190 FR    French
102 DEU   Deutch
203 PS    Psychology
199 TR    Turkish
"""
# regex = re.compile('\s+')
# print('The same')
# print(re.split('\s+', text))
# print(regex.split(text))

print('\nAnd different one is')

# find all numbers within the text
print(text)
regex_num = re.compile('\d+')
regex_num.findall(text)

# ============================
print('\nRe.search is different in that\t')

"""Unlike findall which returns the matched portions of the text as a list, regex.search() 
returns a particular match object that contains the starting and ending positions of the first 
occurrence of the pattern."""

# define the text
text2 = """COM    Computers
205 MAT   Mathematics 189"""

# compile the regex and search the pattern
regex_num2 = re.compile('\d+')
s = regex_num2.search(text2)

print('Starting Position: ', s.start())
print('Ending Position: ', s.end())
print('The start and the end position :',text2[s.start():s.end()])
print('When grouping ',s.group())
# ============================
print('\nSub is different in that\t')

regex=re.compile('\s+')
print(regex.sub(' ',text))
#or
print(re.sub('\s+',' ',text))

# ============================
print('\nSub is different in that\t')

regex=re.compile('((?!\n),\s+)')
print(regex.sub('',text))
# ============================
print('\nRe.find all in that\t')

print(re.findall('[a-z]{3}',text),'\n') #lowercase leri ayirdi
print(re.findall('[A-Z]{3}', text)) #uppercase leri ayirdi
print('\n')
print(re.findall('[A-Za-z]{3,}', text))
print('\n')
print(re.findall('[A-Za-z]{4,}', text))
print('\n')
print(re.findall('[0-9]+',text)) #sadece rakamalari extarct

print('\n')
print(re.findall('[^a-zA-z0-9]',text))
print('\n')
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
print(re.findall(course_pattern,text))
