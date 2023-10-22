def say_hello():
    """Here we create a function and then we begin to call it twice
    we can call it once as wel...
    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    """

    # block belonging to the function
    print('hello world')


# End of function


say_hello()  # call the function
say_hello()  # call the function again

#print(help())
print(__doc__.__class__)
print(dir())
print(__builtins__)

