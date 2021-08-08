from setuptools import setup

setup(
    long_description = """The package allows users (linux) to convert python scripts into executable files by simply using the py2exe-converter -f <python-file-name.py>. 
    One can also use another option after entering python filename which is -p for packages to be included into the executable file. -p takes requirement.txt as input. I have included an example in the demo folder as well. Enjoy! And yup, please, do come forward if you think you can improve or add more functionalities to the project :). 
    Lastly, a huge shoutout to pyinstaller developers who made such an incredible solution that provided a solid base to this project. Thanks amigos!""",
    name = 'py2exe_converter',
    packages = ['py2exe_converter'],
    version = 'v1.0.0',
    description = 'Python to Exe file converter package',
    author = 'Muhammad Ali',
    author_email = 'malirashid1994@gmail.com',
    url = 'https://github.com/alihussainia/Py2Exe-Converter',
    download_url = 'https://github.com/alihussainia/Py2Exe-Converter/archive/refs/tags/v1.0.0.tar.gz',
    keywords = ['py2exe', 'pyinstaller', 'python to exe converter', 'converter'],
    zip_safe=False
)
