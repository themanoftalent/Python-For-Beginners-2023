def multiply_by(a, b=2):
    return a * b

print(multiply_by(3, 47))
print(multiply_by(3))  # call function using default value for b parameter


def hello(subject, name='ali'):
    print("Hello %s! My name is %s" % (subject, name))

hello("PyCharm", "Jane")    # call "hello" function with "PyCharm as a subject parameter and "Jane" as a name
hello("PyCharm")            # call "hello" function with "PyCharm as a subject parameter and default value for the name
