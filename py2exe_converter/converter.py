from subprocess import call
class convert:
    def __init__(self,filename, p=None):
        self.filename = filename
        self.p = p
        self.convert()
    
    def convert(self):
        if self.p!=None:
            with open(self.p, 'r') as names:
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
                call("pyinstaller --hidden-import \{} --onefile {}".format('${my_Array[*]}',self.filename), shell=True)
                call(f"rm -R modules.txt", shell=True)
        else:
            call("pyinstaller --onefile {}".format(self.filename), shell=True)

        call("mv dist/* .", shell=True)                
        call(f"rm -R dist build {self.filename[:-3]}.spec", shell=True)
        call("clear", shell=True)
        print(f"Congratulations! Your {self.filename} has been converted into {self.filename[:-3]}.exe")

