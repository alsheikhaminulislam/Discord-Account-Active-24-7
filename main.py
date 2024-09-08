import os
import sys
import json
import time
import requests
import websocket
import threading
import random
# pip install websocket-client
 
status = "online"
GUILD_ID = '823785341201940500'
CHANNEL_ID = '1142048374758056016'
# SELF_MUTE = True
SELF_DEAF = False

SELF_MUTE_X = [
  True,
  False
]
status=[
  "online",
  "dnd",
  "idle" 
]


def keep_online(token, status, SELF_MUTE, SELF_DEAF):
    headers = {"Authorization": token, "Content-Type": "application/json"}

    validate = requests.get(
        'https://discordapp.com/api/v9/users/@me', headers=headers)
    if validate.status_code != 200:
        print("[ERROR] Your token might be invalid. Please check it again.")
        sys.exit()
    userinfo = requests.get(
        'https://discordapp.com/api/v9/users/@me', headers=headers).json()
    username = userinfo["username"]
    discriminator = userinfo["discriminator"]
    userid = userinfo["id"]

    print(f"Logged in as {username}#{discriminator} ({userid})")

    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {"op": 2, "d": {"token": token, "properties": {"$os": "Windows 11", "$browser": "Google Chrome",
                                                          "$device": "Windows"}, "presence": {"status": status, "afk": False}}, "s": None, "t": None}
    vc = {"op": 4, "d": {"guild_id": GUILD_ID, "channel_id": CHANNEL_ID,
                         "self_mute": SELF_MUTE, "self_deaf": SELF_DEAF}}
    ws.send(json.dumps(auth))
    ws.send(json.dumps(vc))
    online = {"op": 1, "d": "None"}
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps(online))


def run_keep_online(token, status, SELF_MUTE, SELF_DEAF):
  while True: 
    keep_online(token, status, SELF_MUTE, SELF_DEAF) 
    time.sleep(30)
    os.system('cls')


token = [
  "OTAwNzI5MzA2ODIzNjU1NTA0.Ge9_Hk.xxxxxxxxxxx"
]
 
for i in range(0, len(token)):  
  server = threading.Thread(target=run_keep_online, args=(token[i],str(random.choice(status)), bool(random.choice(SELF_MUTE_X)), SELF_DEAF,))
  server.start()

 