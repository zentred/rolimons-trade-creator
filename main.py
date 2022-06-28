import requests, time, configparser, json, threading, ctypes, random, colorama, os, re
from colorama import init, Fore
from threading import Thread
from requests_html import HTMLSession
session = HTMLSession()
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

    def updateRolimons(self):
        while True:
            try:
                session.get(f'https://www.rolimons.com/api/playerassets/{self.userId}').text # htmlSession request which executes page javascript which updates inventory so no more failed
                return None
            except:
                time.sleep(5)
                pass

    def highest(self):
        self.updateRolimons()
        time.sleep(15)
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

        r = requests.post(
            'https://www.rolimons.com/tradeapi/create',

            cookies = {
                '_RoliVerification': self.roliVerification,
                '_RoliData': self.roliData
                },

            json = {
                "player_id":self.userId,
                "offer_item_ids":self.currSend,
                "request_item_ids":[],
                "request_tags":["any","demand","upgrade","rap"]
                }
            )

        if r.json()['success'] == True:
            with lock: print(f'{Fore.LIGHTBLACK_EX}({Fore.LIGHTCYAN_EX}{self.userId}{Fore.LIGHTBLACK_EX}){Fore.WHITE} Created trade ad > {str(self.currSend)}')
            sent += 1
        else:
            with lock: print(f'{Fore.LIGHTBLACK_EX}({Fore.LIGHTCYAN_EX}{self.userId}{Fore.LIGHTBLACK_EX}){Fore.WHITE} Unable to create trade ad')
            failed += 1


    def overall(self):
        while True:
            self.highest()
            time.sleep(900)

def title():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Sent: {sent} | Failed: {failed}')
        time.sleep(1)

Thread(target=title).start()

for root, dirs, files in os.walk("."):
    for filename in files:
        if 'config' in filename:
            with open(f'{filename}','r') as config:
                config = json.load(config)
            c = Player(config)
