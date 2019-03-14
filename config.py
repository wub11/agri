pwd = '' #password of account
url = "http://localhost:5001/api/v0/" #ipfs
gethNode = "http://127.0.0.1:8545" #geth
contractAddr = "0x5777AB7438Df651Ab32aF9C80De2EEBf667AC98b" 
contractABI = [
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
]

