from twilio.rest import TwilioRestClient

ACCOUNT_SID = "AC289f7d8e9decded34363ffa03b469cb8" 
AUTH_TOKEN = "74083a3f504a0e4f2d912be47445228e" 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


client.messages.create(   
    body="Good night bra",  # Message body, if any
    to="+12132459084",
    from_="+14159694232",)





