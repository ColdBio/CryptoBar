import rumps
from pycoingecko import CoinGeckoAPI
import json
import requests
import os
import sys

cg = CoinGeckoAPI()

class Coin:
    def __init__(self, name):
        self.name = name.lower()
        
        self.coin_data = cg.get_coins_markets(vs_currency='usd', ids=f'{self.name}')
        
        self.coin_name = self.coin_data[0]['name']
        self.coin_image = self.coin_data[0]["image"]
        self.coin_price = "${:,}".format(self.coin_data[0]['current_price'])

        self.coin_circulating_supply = "{:,}".format(self.coin_data[0]["circulating_supply"])
        self.coin_market_cap = "{:,}".format(self.coin_data[0]['market_cap'])

        self.coin_high_24h = "${:,}".format(self.coin_data[0]['high_24h'])
        self.coin_low_24h = "${:,}".format(self.coin_data[0]['low_24h'])

        self.coin_price_change_percent = "{:,}%".format(round(self.coin_data[0]['price_change_percentage_24h'], 2))
        
        self.coin_ath_price = "${:,}".format(self.coin_data[0]["ath"])
        self.coin_ath_change_percent = "{:,}%".format(self.coin_data[0]["ath_change_percentage"])
        self.coin_atl = "${:,}".format(self.coin_data[0]["atl"])

btc = Coin('bitcoin')
xrp = Coin('ripple')
eth = Coin('ethereum')

top_tokens = cg.get_coins_markets(vs_currency='usd', per_page=10)

listofTokens = [f"{top_tokens[0]['name']} - ${top_tokens[0]['current_price']}",
                f"{top_tokens[1]['name']} - ${top_tokens[1]['current_price']}",
                f"{top_tokens[2]['name']} - ${top_tokens[2]['current_price']}",
                f"{top_tokens[3]['name']} - ${top_tokens[3]['current_price']}",
                f"{top_tokens[4]['name']} - ${top_tokens[4]['current_price']}",
                f"{top_tokens[5]['name']} - ${top_tokens[5]['current_price']}",
                f"{top_tokens[6]['name']} - ${top_tokens[6]['current_price']}",
                f"{top_tokens[7]['name']} - ${top_tokens[7]['current_price']}",
                f"{top_tokens[8]['name']} - ${top_tokens[8]['current_price']}",
                f"{top_tokens[9]['name']} - ${top_tokens[9]['current_price']}"]

about_text = """
Author: ColdbBio
License: MIT License
Version: v1.0
Repository:-\nhttps://github.com/ColdBio/CryptoBar
""".center(20, "0")

class CryptoBarApp(rumps.App):
    def __init__(self):
        super(CryptoBarApp, self).__init__(f"CryptoBar")
        self.about = rumps.MenuItem(title="About", callback=None)
        self.menu = listofTokens
        self.about_button = rumps.MenuItem(title="About", callback=None)
        self.menu = [self.about_button]
        
    @rumps.clicked("About")
    def about(self):
        rumps.alert("CryptoBar", f"{about_text}")
    
    
    @rumps.timer(3)
    def sayhi(self, _):
        btc = Coin('bitcoin')
        xrp = Coin('ripple')
        eth = Coin('ethereum')
        self.title = f"BTC: {btc.coin_price} - ETH: {eth.coin_price} - XRP: {xrp.coin_price}"
    
if __name__ == "__main__":
    CryptoBarApp().run()
