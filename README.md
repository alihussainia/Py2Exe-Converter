# Py2Exe-Converter

For `WINDOWS USERS`: 

If you are working in a command prompt on windows then follow these guidelines:

1. Install the `pyinstaller` package using the below mentioned command:
```bash
pip install pyinstaller
```
2. Now run the below mentioned command to convert the `.py` file to `.exe` file.
```bash
pyinstaller --hidden-import 'pandas' --onefile 'example.py'
```
3. Open the `dist` folder and you will find your .exe file. 
