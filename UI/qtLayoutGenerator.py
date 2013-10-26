from PyQt4 import uic
import sys

files = [ "HomeLayout", "GenerateForm1Layout" ]

def generate(fileName):
    f = open(fileName + ".py", "w")
    uic.compileUi(fileName + ".ui", f);

commandArg = sys.argv[1]

if commandArg == "all":
    for filename in files:
        generate(filename)
else:
    generate(commandArg)

