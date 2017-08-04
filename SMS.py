
from twilio.rest import Client

# Find these values at https://twilio.com/user/account



def sendSMS():
    account_sid = "AC0871eb3f17f7e9044bcf55df2331f4b8"
    auth_token = "cf93f2cbf676363263759290dec0506d"
    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(to="+19036811366",
                                                 from_="+19722157984",
                                                 body="Security Breach!!")