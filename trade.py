import requests, time
req = requests.Session()

userid = int(input('Enter your ROBLOX User ID: '))
roliverification = input('Enter your _RoliVerification: ')
rolidata = input('Enter your _RoliData: ')
req.cookies['_RoliVerification'] = roliverification
req.cookies['_RoliData'] = rolidata

offers = []

print('This bot will loop creating trade posts, however you may want to send different trades')
print('If you want to send a loop of only 1 type of trade, input the number 1')
print('If you want to send a loop of multiple types of trades, input the amount you would like')
trade_amount = int(input('Enter amount of DIFFERENT trades to send: '))

for i in range(trade_amount):
    print(f'\nTRADE NUMBER {i+1} ---------------------------\n')
    my_offer = []
    their_offer_tags = []
    their_offer_items = []

    amt_mo = int(input('Amount of limiteds to use on MY side (maximum 4): '))
    for i in range(amt_mo):
        lim = int(input('Enter limited ID: '))
        my_offer.append(lim)

    choice = input('\nTHEIR side can use tags/limiteds, choose if you would like to use only limiteds, only tags or both (maximum 4 limiteds/tags)\n[1] Only Limiteds\n[2] Only Tags\n[3] Limiteds and Tags\n')

    if choice == '1':
        amt_toi = int(input('Amount of limiteds to use on THEIR side (maximum 4): '))
        for i in range(amt_toi):
            lim = int(input('Enter limited ID: '))
            their_offer_items.append(lim)
        json = {"player_id":userid,"offer_item_ids":my_offer,"request_item_ids":their_offer_items,"request_tags":their_offer_tags}
        offers.append(json)

    elif choice == '2':
        print('Tags: any, demand, rares, rap, robux, upgrade, downgrade, wishlist\n')
        amt_tot = int(input('Amount of tags to use on THEIR side (maximum 4): '))
        for i in range(amt_tot):
            tag = input('Enter tag: ')
            their_offer_tags.append(tag)
        json = {"player_id":userid,"offer_item_ids":my_offer,"request_item_ids":their_offer_items,"request_tags":their_offer_tags}
        offers.append(json)

    elif choice == '3':
        print('You can only use 4 choices all together, so that means 3 tags + 1 limited would work, but 3 tags 3 limiteds would not work.')
        print('Tags: any, demand, rares, rap, robux, upgrade, downgrade, wishlist\n')
        amt_toi = int(input('Amount of limiteds to use on THEIR side (maximum 4): '))
        amt_tot = int(input('Amount of tags to use on THEIR side (maximum 4): '))
        for i in range(amt_tot):
            tag = input('Enter tag: ')
            their_offer_tags.append(tag)
        for i in range(amt_toi):
            lim = int(input('Enter limited ID: '))
            their_offer_items.append(lim)
        json = {"player_id":userid,"offer_item_ids":my_offer,"request_item_ids":their_offer_items,"request_tags":their_offer_tags}
        offers.append(json)

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'origin': 'https://www.rolimons.com',
    'referer': 'https://www.rolimons.com/tradeadcreate',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44',
    }

while True:
    for line in offers:
        json = line
        print('\nIf response says success: true, that means it worked and you can go check if it shows up\n')
        r = req.post('https://www.rolimons.com/tradeapi/create', headers=headers, json=json)
        print(r.text)
        time.sleep(905)
