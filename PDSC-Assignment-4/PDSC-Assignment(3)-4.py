#This is the 3rd assignment of Day 4, using regex to check if the entered website is of valid format: (alphanumeric.com) or (http://alphanumeric.com) or (http://www.alphanumeric.com)
import re
def checkWebsite(text: str):
    regex_string = r'^(http://|http://www.)[a-zA-Z0-9]*.com$|[a-zA-Z0-9]*.com$'
    our_regex = re.compile(regex_string)
    if (our_regex.fullmatch(text)):
        print('This is a website !!')
    else:
        print('This is not a website !!')

x = input("Enter the Website: ")
checkWebsite(x)
