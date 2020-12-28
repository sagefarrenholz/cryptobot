#!/usr/bin/python3
import os
import ccxt 
import panda

PUBLIC_KEYFILE = './public.key'
PRIVATE_KEYFILE = './private.key'

def start():
    print("Importing Public API key")
    with open(PUBLIC_KEYFILE) as publicKeyFile:
        publicKey = publicKeyFile.readline()
    
    print("Importing Private API key")
    with open(PRIVATE_KEYFILE) as privateKeyFile:
        privateKey = privateKeyFile.readline()

#    exchange_class = getattr(ccxt, ccxt.coinmarketcap())
    kraken = ccxt.kraken({
        'apiKey': publicKey,
	'secret': privateKey,
        'timeout': 30000,
        'enableRateLimit': True,
    })

    print(kraken.urls['api'])
    print(kraken.api)

    print("Loading markets for CoinMarketCap")
    kraken.loadMarkets()

    print(kraken.symbols)
    pass

def checkAvg():
    return -1

if __name__ == "__main__":
    start()

