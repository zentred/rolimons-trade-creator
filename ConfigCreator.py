print('If you would only like to loop create 1 specific trade, input 1, otherwise if you want to rotate between multiple, input the amount\n')
amount = input('Enter amount of DIFFERENT trades to send: ')

with open('config.ini','a') as p:
    p.writelines('# my_side has to have a maximum of 4 ids, EXAMPLE = [3253252, 64363, 7656756, 213124]\n')
    p.writelines("# their_items has maximum of 4 ids, EXAMPLE = [32532532, 3564346]\n")
    p.writelines("# their_tags has maximum of 4 ids, EXAMPLE = ['rap', 'demand']\n")
    p.writelines('# dont know how to get your roliverification or rolidata? read this https://github.com/zentred/rolimons-trade-creator/blob/main/README.md\n\n')
    p.writelines("# their_items AND their_tags can only have a combined maximum of 4, so 2 tags and 2 items would work, 3 tags and 2 items wouldn't work\n\n")
    p.writelines("# tag choices are = any, demand, rares, rap, robux, upgrade, downgrade, wishlist\n\n")
    p.writelines('[info]\nUserID = x\nRoliVerification = x\nRoliData = x\n\n')


for i in range(int(amount)):
    with open('config.ini','a') as p:
        p.writelines(f'[trade{i+1}]\nmy_side{i+1} = []\ntheir_items{i+1} = []\ntheir_tags{i+1} = []\n\n')
