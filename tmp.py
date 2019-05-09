from web3 import Web3
import sys
import requests
import os
import base58
import json
import subprocess
from pprint import pprint
from config import *
from ipfsUtil import ipfsAdd, ipfsCat
w3 = Web3(Web3.HTTPProvider(ethereumNode))
if not w3.isConnected():
    print("ethereum node error")
    exit()


def convertIpfsBytes32(hash_string):
    bytes_array = base58.b58decode(hash_string)
    return bytes_array[2:]

if len(sys.argv) == 3:
    if sys.argv[1].lower() == "add":
        #ipfs start
        print("ready to add file to ipfs")
        fileHash = ipfsAdd(sys.argv[2])
        print(fileHash)
        picHash = json.loads(fileHash)['Hash']
        picHash = convertIpfsBytes32(picHash)
        #etherum start
        print("ready to add fileHash to ethereum")
        contract_ = w3.eth.contract(
            address="0x1c445830f83950A2D6bdD608cb9740650e21C829", abi=contract_interface["abi"])
        acct = w3.eth.account.privateKeyToAccount(privateKey)
        construct_txn = contract_.functions.addNewPic(picHash).buildTransaction({
            'from': acct.address,
            'nonce': w3.eth.getTransactionCount(acct.address),
            'gas': 1728712,
            'gasPrice': w3.toWei('21', 'gwei')})
        signed = acct.signTransaction(construct_txn)
        txId = w3.eth.sendRawTransaction(signed.rawTransaction)
        print("txid : ", w3.toHex(txId))
    elif sys.argv[1].lower() == "cat":
        print("ready to add file to ipfs")
        ipfsCat(sys.argv[2], True)
        print("file output to ./outFile.jpg")
else:
    print("read reademe, and try it again")
