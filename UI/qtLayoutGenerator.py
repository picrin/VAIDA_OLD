from PyQt4 import uic
import sys

files = [ "HomeLayout", "GenerateForm1Layout", "VideoVerificationFormLayout", "PrivateKeySelectorDialog", "KeySavedFormLayout", "MakeVideoFormLayout", "ExportFormLayout" ]

def generate(fileName):
    f = open(fileName + ".py", "w")
    uic.compileUi(fileName + ".ui", f);

if len(sys.argv) > 1:
    commandArg = sys.argv[1]
else:
    commandArg = "all"

if commandArg == "all":
    for filename in files:
        generate(filename)
else:
    generate(commandArg)

print("Generated")
