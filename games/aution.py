import os
record = {}

more_bid = True

while more_bid :
    name = input(" Enter Bidder Name : ")
    bid= input ("Enter Bid Amount : ")
    record[name] = bid
    want_to_enter_more = input('Do you want to enter more bid : yes/no : ')
    if want_to_enter_more == 'no' :
        more_bid = False
    else:
        os.system('clear')

winner = ''
winning_bid = 0
for key in record :
    print (f" {key} bids {record[key]}")
    if winning_bid < int(record[key]) :
        winning_bid = int(record[key])
        winner = key

print(f"{winner} won this auction by bidding {winning_bid}")



