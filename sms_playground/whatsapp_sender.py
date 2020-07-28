def whatsapp_send(message):
    if isinstance(message,list) or isinstance(message,set):
        return('[!]Can Not send the message in list or set format.')
    import os
    from twilio.rest import Client

    account_sid = 'ACa2e531ae1b7c96397975e2412fbe1026'
    auth_token = '536ab8b3b706707c64a8477814867ef9'
    client = Client(account_sid,auth_token)

    message = client.messages.create(to="whatsapp:+919182302594",
                                     body=message,
                                     from_='whatsapp:+14155238886')
    print(message.sid,message.status)

    return None