from __future__ import print_function
#import requests
#from bs4 import BeautifulSoup
import time
import smtplib
import config
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
import simplejson as json
from prasePrice import Price


class stockTrack():
    def __init__(self):
        self.email = config.EMAIL_ADDRESS
        self.password = config.PASSWORD
        self.carrier = '@txt.att.net'
        self.toNumber = config.PHONE_NUMBER + '{}'.format(self.carrier)
        self.SCOPES = config.SCOPES
        self.create_message(self.email, self.toNumber, 'Test Email', self.createMsgTxt())


    # def emailAlert(self, subject, msg):
    #
    #     server = smtplib.SMTP('smtp.gmail.com:587')
    #     server.ehlo()
    #     server.starttls()
    #     server.login(self.email, self.password)
    #
    #     message = 'Subject: {}\n\n{}'.format(subject, msg)
    #     #server.sendmail(self.email, self.email, message)
    #     #server.sendmail(self.email, self.toNumber , message)
    #     server.quit()

    def createMsgTxt(self):
        message = " Your stock is currently at the price of $" + str(Price().parsePrice())
        return message

    # def base64_url_decode(self, inp):
    #     padding_factor = (4 - len(inp) % 4) % 4
    #     print(type(inp))
    #     inp += "="*padding_factor
    #     return base64.b64decode(str(inp).translate(dict(zip(map(ord, u'-_'), u'+/'))))

    def create_message(self, sender, to, subject, message_text):
      message = MIMEText(message_text)
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject


      # JSON NOT Serializable bug
      #b64String = base64.urlsafe_b64decode(b64Bytes).decode("utf-8")
      #print(b64Bytes)

      # or .decode("utf-8")
      return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


    def send_message(self, service, user_id, message):
      # try:
      message = (service.users().messages().send(userId=user_id, body=message).execute())
      print('Message Id: %s' % message['id'])
      return message
      # except:
      #     print('ERR')


    def authorization(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        return service
        # Call the Gmail API
        #results = service.users().labels().list(userId='me').execute()


if __name__ == "__main__":
    while True:
        service = stockTrack().authorization()

        if float(Price().parsePrice()) > 5.23:
            print('gotta get that bag')
            stockTrack().send_message(service, "me", stockTrack().create_message('me','2037510584@txt.att.net', ' Price Update', stockTrack().createMsgTxt()))
            time.sleep(20)
