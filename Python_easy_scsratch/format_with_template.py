from string import Template

s = Template('$who likes $what')
s.substitute(who='Canan', what='Cake')

print(s.template)




