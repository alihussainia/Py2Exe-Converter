# -*- coding: utf-8 -*-
from subprocess import call
call("pip install pyinstaller", shell=True)
from .converter import convert
