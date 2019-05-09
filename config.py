pwd = ''  # password of account
ipfsUrl = "https://ipfs.infura.io/ipfs/"  # ipfs
ethereumNode = "https://ropsten.infura.io/v3/1e75bf07513f4829b9dbe0618cd00b4d"  # infura node
privateKey = "F9BCC02A332B262AF849BBD2A8D4D735B057E052F67923168BD4EF4042480AEB"
contractAddr = "0x1c445830f83950A2D6bdD608cb9740650e21C829"
contract_interface = {
    "abi":
        [
            {
                "constant": False,
                "inputs": [
                    {
                        "name": "picHash",
                        "type": "bytes32"
                    }
                ],
                "name": "addNewPic",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [
                    {
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "name": "farmPicHash",
                "outputs": [
                    {
                        "name": "",
                        "type": "bytes32"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            }
        ],
    "bin": "0x608060405234801561001057600080fd5b50610153806100206000396000f3fe608060405260043610610046576000357c010000000000000000000000000000000000000000000000000000000090048063384ef6ee1461004b578063e0f3f10f14610086575b600080fd5b34801561005757600080fd5b506100846004803603602081101561006e57600080fd5b81019080803590602001909291905050506100d5565b005b34801561009257600080fd5b506100bf600480360360208110156100a957600080fd5b8101908080359060200190929190505050610104565b6040518082815260200191505060405180910390f35b600081908060018154018082558091505090600182039060005260206000200160009091929091909150555050565b60008181548110151561011357fe5b90600052602060002001600091509050548156fea165627a7a72305820b51929c6b14a4d5db8e02df0676cfb8f662aa06c91e224ba3d04a95ab73332850029"
}
