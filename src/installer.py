from pip._internal.cli.main import main
import importlib
import sys

print("version : "+str(sys.version_info[0])+"."+str(sys.version_info[1]))
if sys.version_info[0] != 3:
	print("Warning : you are not using python 3. There may be bugs in other versions of python !")
elif sys.version_info[1] != 8:
	print("Warning : you are not using exact version python 3.8. There may be small bugs !")

def check(name):
	try:
		importlib.import_module(name)
	except ImportError:
		print("Module "+name+" non installé ! Installation...")
		main(['install', name])
		importlib.import_module(name)
	print("Module "+name+" installé !")


check("pygame")
