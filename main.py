import time
from gmailAPI import gmail
from prasePrice import Price
from datetime import datetime

class cuckoo():
    def __init__(self):
        pass


if __name__ == "__main__":

    while True:
        service = gmail().getCreds()
        if float(Price().parsePrice()) > 5:
            print('gotta get that bag @ {}'.format(datetime.now()))
            gmail().sendMessage(service, "me", gmail().buildMessage('me', '2037510584@txt.att.net', "Price Update", gmail().textMessage()))
            time.sleep(20)
