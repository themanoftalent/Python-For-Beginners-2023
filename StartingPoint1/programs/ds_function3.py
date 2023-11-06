def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.
    If message is not provided,
    it defaults to "Good
    morning!"
    """
    print ("Hello", name + ', ' + msg)


greet ("Kate")
greet ("Bruce", "How do you do?")
greet ('', ' ')
greet (name='Murat')
greet ('You', 'sen nasilsin')
print ('**' * 23)


def greets(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print ("Hello", name)


greets ("Monica", "Luke", "Steve", "John")
print ('**' * 23)


def selam(*esame):
    for name in esame:
        print ('Selam sana ey ', name)


selam ('ahmet', 'kemal', 'hulya')
