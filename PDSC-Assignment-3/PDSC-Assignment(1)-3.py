#This is the 1st assignment of day 3, this program is executed by the windows batch file in this directory which can be called directly from windows run command, and what it does is copies the password of email and other accounts saved in windows path variables directly to clipboard.
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
