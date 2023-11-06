import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for mstch in re.finditer(pattern, text, flags=re.IGNORECASE):
    s = mstch.start()
    e = mstch.end()

print('Matching found "%s" at %d:%d' % (text[s:e], s, e))
