# Py2Exe-Converter

For `Linux Users`:

Follow the two-step guide to easily convert your python scripts to executable files:

1. Install the `py2exe-converter` package using the below mentioned command:
```bash
pip install py2exe-converter
```
2. Now import the package by running the below mentioned command:
```bash
import py2exe_converter as pec 
```
Note: You can use `-p requirements.txt` along with the above command in order to install all the packages in the `.exe` file that are used by your `.py` file.

3. Now run the following command to convert the `.py` file to `.exe` file:
```bash
pec.convert('example.py`, `requirements.txt')
```
Note: Inputting `requirements.txt` is optional.

4. Open the `example.exe` file and confirm that the program is running fine :) 

### **Try `Py2Exe-Converter`in your browser**:

[MyBinder-Link](https://mybinder.org/v2/gh/alihussainia/Py2Exe-Converter/main?urlpath=lab)
