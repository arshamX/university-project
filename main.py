# import implemented methods in modules.py file
from modules import *

if __name__ =="__main__":
    # call readJason method
    constant = readJson()
    # call readInformation method
    strings = readInformation()
    # call process method
    process(constant,strings)
    # asking client to press enter to end the app
    input("end of process press enter to end")