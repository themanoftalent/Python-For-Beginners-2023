#"repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
#repr() Parameters
#
# The repr() method takes a single parameter:
#
#     obj - object whose printable representation has to be returned

print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))
print('=======================================================================')

class Person:
    name = 'Adam'

    def __repr__(self):
        return repr(self.name)
    print(name)

repr(Person())
