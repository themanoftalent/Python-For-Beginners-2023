#5. Extract all the text portions between the tags from the following
# HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
import re
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text  # html text is contained here

#desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ',
                  #'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
print(re.findall('<.*?>(.*)< /.*?>', r.text) )


print('========================')

import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print ('Found "%s"' % match)
    break
