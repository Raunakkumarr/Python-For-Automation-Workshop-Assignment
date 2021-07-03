#this is the 2nd assignment of Day 4, that uses regex to check if the entered library import is of valid format: (import somelibrary) or (import somelibrary as sl) or (from somelibrary import class)
import  re
def checkWebsite(text: str):
    regex_string1 = r'^import\s[a-zA-Z0-9]{1,100}$'
    regex_string2 = r'^import\s[a-zA-Z0-9]{1,100}\sas\s[a-zA-Z0-9]{1,10}$'
    regex_string3 = r'^from\s[a-zA-Z0-9]{1,100}\simport\s[a-zA-Z0-9]{1,10}$'
    our_regex1 = re.compile(regex_string1)
    our_regex2 = re.compile(regex_string2)
    our_regex3 = re.compile(regex_string3)
    if (our_regex1.fullmatch(text)):
        print('This is a valid import !!')
    elif (our_regex2.fullmatch(text)):
        print('This is a valid import !!')
    elif (our_regex3.fullmatch(text)):
        print('This is a valid import !!')
    else:
        print('This is an invalid import !!!')
x = input("Import your module: ")
checkWebsite(x)
