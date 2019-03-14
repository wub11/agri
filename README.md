agri 使用文件
# 流程
1. run ifps in daemon
2. run geth with rpc api(need to open personal module)
3. if the contract didn't be deployed, please deploy it
4. ``pip3 install -r  requirements.txt``
4. set the config
![](https://i.imgur.com/GfcyPpn.png)

 BTW, all tx send from coinbase


## 添加文件到ipfs 和 contract
    python3 tmp.py add filename

![](https://i.imgur.com/vn642In.png)

## 從ipfs讀取文件
    python3 tmp.py cat filename
### 會輸出到outFile
![](https://i.imgur.com/LGteKYq.jpg)

