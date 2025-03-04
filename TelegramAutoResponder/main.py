import requests
import json
from time import sleep
#>

BOT_TOKEN = ''
UPDATES_OFFSET = 0 

#>
def getUpdates():
    global UPDATES_OFFSET, BOT_TOKEN

#>
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    params = { 'offset': UPDATES_OFFSET }
    response = requests.get(url, params=params)
#>
    response = json.loads( response.text )
    updates = response['result']
#>
    for update in updates:
        update_id = update['update_id']
        UPDATES_OFFSET = update_id + 1
#>
        uid = update['message']['from']['id']
        user_text = update['message']['text']
#>
        if user_text == 'Пинг':
            sendMessage(uid, 'Понг')
        else:
            sendMessage(uid, 'Привет, я бот автоответчик')

#>
def sendMessage(uid, text):
    global BOT_TOKEN
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    params = { 'chat_id' : uid, 'text': text }
    requests.get(url, params=params)

#>
while True:
    getUpdates()
    sleep(1)