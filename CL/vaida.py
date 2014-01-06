import sys
import generate_vaida
import verify_vaida

if len(sys.argv) < 2:
    print ("Please enter a command")
    exit()

command = sys.argv[1]
print (command)

if command == "generate":
    x = 0
    # Generate
elif command == "verify":
    vaida_file = sys.argv[1]
    verify_vaida.verify(vaida_file)
    # Verify
elif command == "help":
    x = 1
    # Help
else:
    print("Unknown command '" + command + "'. For help enter help")
