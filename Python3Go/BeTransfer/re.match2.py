# # matchObject = re.search(pattern, input_str, flags=0)
#
# import re
# # Lets use a regular expression to match a date string. Ignore
# # the output since we are just testing if the regex matches.
# regex = r"([a-zA-Z]+) (\d+)"
# if re.search(regex, "June 24"):
#     # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string
#     # If we want, we can use the MatchObject's start() and end() methods
#     # to retrieve where the pattern matches in the input string, and the
#     # group() method to get all the matches and captured groups.
#     match = re.search(regex, "June 24")
#
#     # This will print [0, 7), since it matches at the beginning and end of the
#     # string
#     print("Match at index %s, %s" % (match.start(), match.end()))
#
#     # The groups contain the matched values.  In particular:
#     #    match.group(0) always returns the fully matched string
#     #    match.group(1), match.group(2), ... will return the capture
#     #            groups in order from left to right in the input string
#     #    match.group() is equivalent to match.group(0)
#
#     # So this will print "June 24"
#     print("Full match: %s" % (match.group(0)))
#     # So this will print "June"
#     print("Month: %s" % (match.group(1)))
#     # So this will print "24"
#     print("Day: %s" % (match.group(2)))
# else:
#     # If re.search() does not match, then None is returned
#     print("The regex pattern does not match. :(")

import re
xx = str(input('Enter your text '))
richWord1 = re.findall(r"^\w+",xx) #finding the first word
print (richWord1)


