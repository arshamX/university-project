# import json library
import json


# Reads JSON file for finding constants of application same as digits and ..
def readJson():
    with open("constants.json","r") as file:
        try:
            return json.load(file) 
        except:
            print("Error in loading constants.json file")
    
# Reads .txt file for finding strings in it and turn each line of file to an elemnt of a list
def readInformation():
    with open("inforrmations.txt","r") as file:
        try:
            return file.read().split('\n')
        except:
            print("Error in loading inforrmations.text file")
# Does the main process of application by navigation trough the NFA chart we have(the NFA diagram shown in picture appended in the files)
def process(constants,informations):
    for line in informations:
        state = 0
        for char in line:
            if state == 0:
                if char in constants["digits"]:
                    state = 1
                elif char in constants["letters"]:
                    state = 5
                elif char == ">":
                    state = 7
                elif char == "<":
                    state = 9
            elif state == 1:
                if char in constants["digits"]:
                    state = 1
                elif char in constants["spliter"]:
                    state = 2
                elif char == '.':
                    state = 3
            elif state == 3:
                if char in constants["digits"]:
                    state = 3
                elif char in constants["spliter"]:
                    state = 4
            elif state == 5 :
                if char in constants["letters"] or char in constants["digits"]:
                    state = 5
                elif char in constants["spliter"]:
                    state = 6
            elif state == 7 :
                if char == '=':
                    state = 8
            elif state == 9 :
                if char == '=':
                    state = 10
        if state == 2:
            print("integer number")
        elif state == 4 :
            print("floating number")
        elif state == 6 :
            print("ID")
        elif state == 8 :
            print(">= oprator")
        elif state == 10 :
            print("<= oprator")   

            
