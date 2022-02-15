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


class CryptoBarApp(rumps.App):
    def __init__(self):
        super(CryptoBarApp, self).__init__(f"CryptoBar")
        self.about = rumps.MenuItem(title="About", callback=None)

    @rumps.timer(3)
    def sayhi(self, _):
        btc = Coin('bitcoin')
        xrp = Coin('ripple')
        eth = Coin('ethereum')
        self.title = f"BTC: {btc.coin_price} - ETH: {eth.coin_price} - XRP: {xrp.coin_price}"
        #print(f"BTC: {btc.coin_price} ETH: {eth.coin_price}, XRP: {xrp.coin_price}")
    
if __name__ == "__main__":
    CryptoBarApp().run()
