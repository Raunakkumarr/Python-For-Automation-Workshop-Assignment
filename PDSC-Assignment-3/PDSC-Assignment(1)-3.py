import os
import sys,pyperclip
email_pswd = os.environ.get('password')
fb_pswd = os.environ.get('fb_password')
passwords = {
    'email': email_pswd,
    'fb': fb_pswd
    }

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    error = "There is no account named "+account
    pyperclip.copy(error)
    print(error)
