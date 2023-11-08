'''
#alinti
sys.argv represents the command line options you execute a script with.

sys.argv[0] is the name of the script you are running. All additional options are contained in sys.argv[1:].

You are attempting to open a file that uses sys.argv[1] (the first argument) as what looks to be the directory.

Try running something like this:

python ConcatenateFiles.py /tmp

'''

import sys

if len(sys.argv) < 2:
    print("Fatal: You forgot to include the directory name on the command line.")
    print("Usage:  python %s <directoryname>" % sys.argv[0])
    sys.exit(1)
