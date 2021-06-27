import re
def checkWebsite(text: str):
    regex_string = r'[a-zA-Z0-9]{1,30}@[a-zA-Z0-9]{1,20}.[a-zA-Z0-9]{1,10}$|[a-zA-Z0-9]{1,30}.[a-zA-Z0-9]{1,30}@[a-zA-Z0-9]{1,20}.[a-zA-Z0-9]{1,10}.[a-zA-Z0-9]{1,10}$'
    our_regex = re.compile(regex_string)
    if (our_regex.fullmatch(text)):
        print('This is an email !!')
    else:
        print('This is not an email !!!')

x = input("Enter your Email: ")
checkWebsite(x)
