class MyClass:
    variable = 'Hey there'

    def foo(self):   # we'll explain self parameter later in task 4
        print("Hello from function foo")

my_object = MyClass()  # variable "my_object" holds an object of the class "MyClass" that contains the variable and the "foo" function

print(my_object.foo())
