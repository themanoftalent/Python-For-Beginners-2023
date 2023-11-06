#! /usr/bin/python
# Filename: using_mymodule.py
# Description: This script is used to test
# the module I wrote in mymodule.py

import mymodule

mymodule.sayHello() # using . to set which module to use
print mymodule.version 

### Note: if using from mymodule import *, then we could 
### use every function and varible without '.'
