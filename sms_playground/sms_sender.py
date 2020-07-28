import os
from twilio.rest import Client

account_sid = 'ACa2e531ae1b7c96397975e2412fbe1026'
auth_token = '536ab8b3b706707c64a8477814867ef9'
client = Client(account_sid,auth_token)

message = client.messages.create(to="+919182302594",body="Hey, this is a trial test from twilio account.",from_="+14422673751")
print(message.sid,message.status)