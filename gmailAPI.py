from __future__ import print_function   #Make sure this line is always at the top of the file.
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64

class Gmail():
    def __init__(self):
        self.email = config.EMAIL_ADDRESS
        self.password = config.PASSWORD
        self.carrier = '@txt.att.net'
        self.toNumber = config.PHONE_NUMBER + '{}'.format(self.carrier)
        self.SCOPES = config.SCOPES
        self.create_message(self.email, self.toNumber, 'Test Email', self.createMsgTxt())

    def createMsgTxt(self):
        message = " Your stock is currently at the price of $" + str(Price().parsePrice())
        return message

    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject

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
