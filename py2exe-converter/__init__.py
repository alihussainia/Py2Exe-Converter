import getopt, sys
from subprocess import call
import os
import io

call("pip install pyinstaller", shell=True)
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
filename = sys.argv[2]
# Options
options = "pf:"

# Long options
long_options = ["packages =","filename ="]

# # checking each argument
arguments, values = getopt.getopt(argumentList, options, long_options)
for currentArgument, currentValue in arguments:
    if currentArgument in ("-p", "--packages"):
        with open("requirements.txt", 'r') as names:
            mylist = names.readlines()
            newstring = []
            for word in mylist:
                word = word.strip()
                newstring.append(word)
            call("touch modules.txt", shell=True)
            with open("modules.txt", 'w') as modules:
                for module in newstring:
                    modules.write(module+',')
            
            call("mapfile -t my_Array < modules.txt", shell=True)  
            call("pyinstaller --hidden-import \{} --onefile {}".format('${my_Array[*]}',filename), shell=True)
            call(f"rm -R modules.txt", shell=True)
    else:
        call("pyinstaller --onefile {}".format(filename), shell=True)

call("mv dist/* .", shell=True)                
call(f"rm -R dist build {filename[:-3]}.spec", shell=True)
print("\n")
print("\n")
print("\n")
call("clear", shell=True)
print(f"Congratulations! Your {filename} has been converted into {filename[:-3]}.exe")
