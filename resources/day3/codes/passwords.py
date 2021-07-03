#This code automatically copies the password of your fb or eamil or any other acoount durectly to your clipboard.
import sys, pyperclip

PASSWORDS = {'email': 'your_email_password',
             'fb' : 'your_fb_password',               
             }


if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')

else:
    print('There is no account named ' + account)


