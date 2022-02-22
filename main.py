import requests, time, configparser, json, threading, ctypes, random, colorama, os
from colorama import init, Fore
from threading import Thread
init()

sent = 0
failed = 0
lock = threading.Lock()
os.system('cls')

class Player:
    def __init__(self, config):
        self.userId = config['userId']
        self.roliVerification = config['roliVerification']
        self.roliData = config['roliData']
        self.myAssets = []
        self.currSend = []
        Thread(target=self.overall).start()

    def highest(self):
        totalLimiteds = requests.get(f'https://inventory.roblox.com/v1/users/{self.userId}/assets/collectibles?sortOrder=Asc&limit=100&cursor=').json()['data']
        self.myAssets = [limited['assetId'] for limited in totalLimiteds]
        random.shuffle(self.myAssets)
        if len(self.myAssets) >= 4:
            self.currSend.clear()
            for i in range(4):
                self.currSend.append(self.myAssets[i])
        else:
            self.currSend = self.myAssets
        self.send()

    def send(self):
        global sent, failed
        with lock: print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}SENDING{Fore.WHITE}] {self.userId} is about to send {str(self.currSend)}')
        json = {"player_id":self.userId,"offer_item_ids":self.currSend,"request_item_ids":[],"request_tags":["any","demand","upgrade","rap"]}
        r = requests.post('https://www.rolimons.com/tradeapi/create', json=json, cookies={'_RoliVerification': self.roliVerification, '_RoliData': self.roliData})
        if r.json()['success'] == True:
            with lock: print(f'{Fore.WHITE}[{Fore.GREEN}CREATED{Fore.WHITE}] {self.userId} created a trade ad')
            sent += 1
        else:
            with lock: print(f'{Fore.WHITE}[{Fore.GREEN}FAILED{Fore.WHITE}] {self.userId} was unable to create a trade ad')
            failed += 1


    def overall(self):
        while True:
            self.highest()
            time.sleep(905)

def title():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Sent: {sent} | Failed: {failed}')

Thread(target=title).start()

for root, dirs, files in os.walk("."):
    for filename in files:
        if 'config' in filename:
            with open(f'{filename}','r') as config:
                config = json.load(config)
            c = Player(config)
