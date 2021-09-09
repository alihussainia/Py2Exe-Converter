from subprocess import call
from sys import platform
from PIL import Image
from os import path, remove
class convert:
    """
        It will allow you to make an exe file, by providing the following params:
        args1 (str): Provide a path of your main file.
        args2 (str): Provide a path of requirement file which contains all the necessary dependancies.
        args3 (str): Provide an icon if there is any available, it is an optional params. 
    """
    def __init__(self,filename, p=None, icon=None):
        self.filename = filename
        self.p = p
        self.icon = icon
        self.convert()

    def convert(self):
       
        if self.p!=None:
            with open(self.p, 'r') as names:
                mylist = names.readlines()
                print(mylist)
                newstring = []
                for word in mylist:
                    word = word.strip()
                    newstring.append(word)
                    print(word)
                if platform == "linux" or platform == "linux2":
                    call("touch modules.txt", shell=True)
                    with open("modules.txt", 'w') as modules:
                        for module in newstring:
                            modules.write(module+',')

                elif platform == 'win32':
                    call("type nul >  modules.txt", shell=True)
                    with open("modules.txt", 'w') as modules:
                        for module in newstring:
                            modules.write(module+',')

                if platform == "linux" or platform == "linux2":
                    call("mapfile -t my_Array < modules.txt", shell=True)  

                    name, ext = path.splitext(self.icon)
                    
                    print("Icon is: {}".format(ext))

                    if ext == '.ico':
                        print("This is a Icon file extension is ico")
                    else:
                        img = Image.open(self.icon)
                        if path.exists('icon.ico'):
                            remove('icon.ico')
                            print('This file is already existed!')
                        else:
                            img.save('icon.ico')
                            print("Succesfully created an Icon file!")

                    if path.exists('icon.ico'):
                        call("pyinstaller --hidden-import \{} --onefile {} --icon={}".format('${my_Array[*]}',self.filename, self.icon), shell=True)
                    else:
                        call("pyinstaller --hidden-import \{} --onefile {}".format('${my_Array[*]}',self.filename), shell=True)

                    call(f"rm -R modules.txt", shell=True)

                    
                elif platform == "win32":
                    # call("@echo off \ set var", shell=True)
                    call("for /f \"tokens=* delims=,\" %f in (\'type modules.txt\') do (var = !var[%f]!)", shell=True)  
                    
                    name, ext = path.splitext(self.icon)
                    
                    print("Icon is: {}".format(ext))

                    if ext == '.ico':
                        print("This is a Icon file extension is ico")
                    else:
                        img = Image.open(self.icon)
                        if path.exists('icon.ico'):
                            remove('icon.ico')
                            print('This file is already existed!')
                        else:
                            img.save('icon.ico')
                            print("Succesfully created an Icon file!")
                    if path.exists('icon.ico'):
                        call("pyinstaller --hidden-import {} --onefile {} --icon={}".format('${%var%}',self.filename, self.icon), shell=True)
                    else:
                        call("pyinstaller --hidden-import {} --onefile {}".format('${%var%}',self.filename), shell=True)

                    call("del /q \"modules.txt\"", shell=True)
        else:
            call("pyinstaller --onefile {}".format(self.filename), shell=True)

        if platform == "linux" or platform == "linux2":
            call("mv dist/* .", shell=True)                
            call(f"rm -R dist build {self.filename[:-3]}.spec", shell=True)
            call("clr", shell=True)
            print(f"Congratulations! Your {self.filename} has been converted into {self.filename[:-3]}.exe")

        elif platform == "win32":
            call("move dist\*.* .", shell=True)                
            call("rmdir /s /q build\\ dist\\", shell=True)
            call("del /q \"{}.spec\"".format(self.filename[:-3]), shell=True)
            call("cls", shell=True)
            print(f"Congratulations! Your {self.filename} has been converted into {self.filename[:-3]}.exe")

