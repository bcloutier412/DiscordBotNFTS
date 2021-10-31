import requests
import random
import time

# channel_id = 903943388527742978

token = input("What is your token? :")
channel_id = int(input("What is the channel_id? :"))
delay = int(input("How long is the delay in seconds? :"))
message_count = int(input("How many messages do you want to send? :"))


def send_message(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    print(r.status_code)


messages = ['Aye whats up guys hows it going today?', 'LOLOL', 'XDXD', 'nathan is an idiot']

for i in range(message_count):
    send_message(token, channel_id, random.choice(messages))
    time.sleep(delay)
