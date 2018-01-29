# kopano-scan-attachments.py
Python program to scan all attachments of a Kopano user with ClamAV and if required remove them if infected.

## Python Requirements
- clamd
- six
- python-kopano

## System Requirements
- clamav-daemon

# Command line options
```
Options:
  -h, --help                         show this help message and exit
  -c FILE, --config=FILE             load settings from FILE
  -s SOCKET, --server-socket=SOCKET  connect to server SOCKET
  -k FILE, --ssl-key=FILE            SSL key file
  -p PASS, --ssl-pass=PASS           SSL key password
  -C NAME, --company=NAME            run program for specific company
  -u NAME, --user=NAME               run program for specific user
  -b DATE, --period-begin=DATE       run program for specific period
  -e DATE, --period-end=DATE         run program for specific period
  --all                              run program for all users
  --autoremove                       remove infected attachments
```
# Some Examples
## Run only scanning user kato
```
$ python kopano-scan-attachments.py -u kato
```
```
Scanning user [kato]
        Scanning folder [Suggested Contacts]
        Scanning folder [Quick Step Settings]
        Scanning folder [Conversation Action Settings]
        Scanning folder [RSS Feeds]
        Scanning folder [Junk E-mail]
        Scanning folder [Tasks]
        Scanning folder [Notes]
        Scanning folder [Journal]
        Scanning folder [Drafts]
        Scanning folder [Calendar]
                Virus found: [Meet Dr. Frikandel] [FOUND] [Eicar-Test-Signature]
        Scanning folder [Contacts]
                Virus found: [Piet Frikandel] [FOUND] [Eicar-Test-Signature]
        Scanning folder [Sent Items]
        Scanning folder [Deleted Items]
        Scanning folder [Outbox]
        Scanning folder [Inbox]
                Virus found: [Introduction to Dr Frikandel] [FOUND] [Eicar-Test-Signature]
```
## Run for user kato and autoremove any infected items
```bash
$ python kopano-scan-attachments -u kato --autoremove
```
```
Scanning user [kato]
        Scanning folder [Suggested Contacts]
        Scanning folder [Quick Step Settings]
        Scanning folder [Conversation Action Settings]
        Scanning folder [RSS Feeds]
        Scanning folder [Junk E-mail]
        Scanning folder [Tasks]
        Scanning folder [Notes]
        Scanning folder [Journal]
        Scanning folder [Drafts]
        Scanning folder [Calendar]
                Virus found: [Meet Dr. Frikandel] [FOUND] [Eicar-Test-Signature]
                Autoremoving attachment: [Meet Dr. Frikandel] [eicar.com]
        Scanning folder [Contacts]
                Virus found: [Piet Frikandel] [FOUND] [Eicar-Test-Signature]
                Autoremoving attachment: [Piet Frikandel] [eicar.com]
        Scanning folder [Sent Items]
        Scanning folder [Deleted Items]
        Scanning folder [Outbox]
        Scanning folder [Inbox]
                Virus found: [Introduction to Dr Frikandel] [FOUND] [Eicar-Test-Signature]
                Autoremoving attachment: [Introduction to Dr Frikandel] [eicar.com]
```
# Todo's
- None at the moment, suggestions are welcomed
