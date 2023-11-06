# I would recommend always using parentheses
# to indicate start and end of tuple
# even though parentheses are optional.
# Explicit is better than implicit.
zoo = ('python', 'elephant', 'penguin')
print ('Number of animals in the old zoo is : ', len (zoo))
print ('__' * 18)
new_zoo = ('monkey', 'camel', zoo)  # parentheses not required but are a good idea, adding the old zoo values as well
print ('Number of cages in the new zoo is : ', len (new_zoo))
print ('__' * 18)
print ('All animals in new zoo are :', new_zoo)
print ('__' * 18)

print ('Animals brought from old zoo are :', new_zoo[2])
print ('__' * 18)
print ('Last animal brought from old zoo is :', new_zoo[2][2])
print ('__' * 18)
print ('Number of animals in the new zoo is :', len (new_zoo) - 1 + len (new_zoo[2]))
