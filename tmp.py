import sys
import requests
import os
import base58
import json
import subprocess
from pprint import pprint

from config import *

from web3 import Web3
w3 = Web3(Web3.HTTPProvider(gethNode))
if not w3.isConnected():
    print("ethereum node error")
    exit()

coinBase = w3.eth.coinbase
w3.personal.unlockAccount(coinBase,pwd)

agri = w3.eth.contract(
    address=contractAddr,
    abi=contractABI,
)

def convertIpfsBytes32(hash_string):
    bytes_array = base58.b58decode(hash_string)
    return bytes_array[2:]

if len(sys.argv) == 3:
    if sys.argv[1].lower() == "add":
        print("ready to add file to ipfs")
        files = {'file': open(sys.argv[2], 'rb')}
        r = requests.post(url + "add", files=files)
        print(r.text)
        picHash = json.loads(r.text)['Hash']
        picHash = convertIpfsBytes32(picHash)
        txID = agri.functions.addNewPic(picHash).transact({'from': coinBase})
        print(txID)

    elif sys.argv[1].lower() == "cat":
        print("ready to add file to ipfs")
        with open("outFile", "wb") as out:
            subprocess.Popen(["ipfs", "cat", sys.argv[2]], stdout=out)
        print("file output to ./outFile")
else:
    print("try it again")
