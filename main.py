import requests, time, configparser, json, threading, ctypes
from threading import Thread
req = requests.Session()

payloads = []
failed = 0
sent = 0

config = configparser.ConfigParser()
config.read('config.ini')

userid = int(config['info']['UserID'])
roliverification = config['info']['RoliVerification']
rolidata = config['info']['RoliData']
req.cookies['_RoliVerification'] = roliverification
req.cookies['_RoliData'] = rolidata

def title():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Sent: {sent} | Failed: {failed}')

Thread(target=title).start()

for x in config:
    if 'trade' in x:
        for z in config[x]:
            if 'my_side' in z:
                my_side = json.loads(config[x][z])
            elif 'their_items' in z:
                their_items = json.loads(config[x][z])
            elif 'their_tags' in z:
                their_tags = json.loads(config[x][z])
        check_m = len(my_side)
        check_t = len(their_items) + len(their_tags)
        if check_m <= 4 and check_t <= 4:
            payloads.append({"player_id":userid,"offer_item_ids":my_side,"request_item_ids":their_items,"request_tags":their_tags})
        else:
            print('\nError occured.\nMy side: {check_m} items\nTheir side: {check_t} items+tags\n\nIf any of these values are above 4, please read the information provided in config and fix the config')

while True:
    for payload in payloads:
        while True:
            r = req.post('https://www.rolimons.com/tradeapi/create', json=payload)
            if r.json()['success'] == True:
                sent += 1
                break
            else:
                print(f'{r.text}')
                failed += 1
                time.sleep(20)
                break
        time.sleep(905)
