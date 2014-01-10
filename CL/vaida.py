import sys
import generate_vaida
import verify_vaida

def set_player(new_player):
    return

if len(sys.argv) < 2:
    print ("Please enter a command. For help use 'help' command")
    exit()

command = sys.argv[1]
print (command)

if command == "generate":
    generate_vaida.generate()
    # Generate
elif command == "verify":
    vaida_file = sys.argv[2]
    verify_vaida.verify(vaida_file)
    # Verify
elif command == "help":
    print ("Command line VAIDA")
    print ("The available commands are:")
    print ("   generate    Interactively generate a VAIDA file")
    print ("   verify      Interactively verify a VAIDA file")
    print ("   set-player  Set the video player used to verify VAIDA files")
elif command == "set-player":
    if len(sys.argv) < 3:
        print ("Please enter a video player after set-player")
    else:
        new_player = sys.argv[2]
        set_player(new_player)
    
else:
    print("Unknown command '" + command + "'. For help enter help")
