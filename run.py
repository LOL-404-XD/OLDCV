import os, sys
os.system('xdg-open https://facebook.com/Muhammad.Meithun')
try:
    __import__("oldcv").Main()
except Exception as e:
    exit(str(e))
