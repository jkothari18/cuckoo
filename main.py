import time
from gmailAPI import gmail
from prasePrice import Price
from datetime import datetime
import config

class cuckoo():
    def __init__(self):
        pass


if __name__ == "__main__":
    while True:
        service = gmail().getCreds()
        if float(Price().parsePrice()) > 5:
            print('gotta get that bag @ {}'.format(datetime.now()))
            gmail().sendMessage(service, "me", gmail().buildMessage('me', config.PHONE_NUMBER, "Price Update", gmail().textMessage()))
            time.sleep(20)
        elif float(Price().parsePrice()) < 3.7:
            print('Bruhhhhhhh you losing money @ {}'.format(datetime.now()))
            gmail().sendMessage(service, "me", gmail().buildMessage('me', config.EMAIL_ADDRESS, "Price Update",
                                                                    gmail().textMessage()))
            gmail().sendMessage(service, "me", gmail().buildMessage('me', config.PHONE_NUMBER, "Price Update", gmail().textMessage()))

