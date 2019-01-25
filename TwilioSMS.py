"""
CIS4360Assign1
Assignment 1 - Calling Twilio and Google APIs
Part 1: Twilio
"""

from twilio.rest import Client

account_sid = "ACbfc6fb54f17475ad4c94dc95c4808623"
auth_token  = "[Auth_token]"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12157794163",
    from_="+12673231648",
    body="Hello from Python!")

print(message.sid)

