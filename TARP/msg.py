#!/usr/bin/python3
from twilio.rest import Client
import os
os.chdir("twilio")

account_sid = "AC005fda93c3f83474b409a266c217b613"
auth_token = "3a1ff79fb05d39af627dab5d95b568b9"
client = Client (account_sid, auth_token)
message = client.api.account.messages.create(
    to = "+919487559455",
    from_ = "+17868286381",
    body = "Person Detected Inside your car")

os.chdir("..")
os.system("python main1.py")
