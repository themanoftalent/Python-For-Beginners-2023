#!/usr/bin/env python

import sys

# Command line args are in sys.argv[1], sys.argv[2] ...
# sys.argv[0] is the script name itself and can be ignored
def main():
	print "Hello, world" , sys.argv[0]	

if __name__ == "__main__":
	main()
