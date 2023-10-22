import re


#1. Extract the user id, domain name and suffix from the following email addresses.
emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

desired_output = [('zuck26', 'facebook', 'com'),
 ('page33', 'google', 'com'),
 ('jeff42', 'amazon', 'com')]

my_pattern=r'(\w+)\@([A-Za-z0-9]+)\.([a-zA-Z]{2,4})'
print(re.findall(my_pattern,emails, flags=re.IGNORECASE))
#or
# pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
# print(re.findall(pattern,emails, flags=re.IGNORECASE))
