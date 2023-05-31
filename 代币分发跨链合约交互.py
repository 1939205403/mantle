#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:18
# @Author  : 1939205403
# @File    : 代币分发合约交互.py
import json
import time
import datetime
import traceback

import requests
import dbm
import random
import web3
from web3 import Web3, HTTPProvider, WebsocketProvider, module,gas_strategies
def initFaucet(address,amount,ttt):
	baseFee=w3.eth.get_block("latest").baseFeePerGas
	maxPriorityFeePerGas=w3.eth.max_priority_fee
	print('nonce',ttt)
	tx = faucet_contract.functions.sendWei(address,amount).buildTransaction({
		'from': boss_address,
		# 'value': amount,
		'nonce': ttt,
		# 防止因gas过低导致交易失败
		'gas': 120000,
		'maxFeePerGas': 2*baseFee+maxPriorityFeePerGas,#	EIP-1559 标准的Gas Estimator 推荐 Max Fee = (2 * Base Fee) + Max Priority Fee
		'maxPriorityFeePerGas':maxPriorityFeePerGas ,#w3.eth.max_priority_fee返回分钟级的最大奖励
		# 'gasPrice': w3.toWei(w3.eth.gasPrice,'wei'),
		# 'nonce': nonce,
		'chainId': 5,
		# 'data': '0x1249c58b'
	})
	# 签名
	signed_tx = w3.eth.account.signTransaction(tx, boss_key)
	# 得到交易哈希
	tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w3.toHex(tx_hash)


def GetAccount(i):
    with dbm.open('AccountScroll.db', 'r') as db:
       x= str(db.keys()[i])
       # 字符串切片操作
       x = x[2:-1]

       y=str(db[db.keys()[i]])
       y = y[2:-1]
       length=len(db)
    db.close()
    return x,y,length
def WriteAccount(i):
    with dbm.open('AccountScroll.db', 'c') as db:
        # db['key'] = 'value'
        # db['today'] = 'Monday'
        # db['author'] = 'suk'
        # print(dbm.whichdb('example.db'))
        for i in range(i):
            # 创建账户
            account = w3.eth.account.create()
            # add.append(account.address)
            db['%s'%(account.address)]='%s'%account.key.hex()
        db.close()
            # pas.append(account.key.hex())
            # 分别将账户地址和私钥写入dbm


def NowTime():
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def WrightError(i):
	path1 = 'Problem\Error%s.txt' % i
	file1 = open(path1, 'a')
	file1.write("%s\n%s\n" % (NowTime(), traceback.format_exc()))
	file1.close()


def getBalance(address):
	balance=w3.eth.getBalance(address)
	if balance==0:
		print(address)
	# pass
if __name__ == '__main__':
	goerliurl = 'https://rpc.ankr.com/eth_goerli'
	goerliurl2="https://goerli.blockpi.network/v1/rpc/public"
	goerliurl3="https://eth-goerli.public.blastapi.io"
	# 填入自己的从infura申请的rpc，现在的是我的
	w3 = Web3(HTTPProvider("https://goerli.infura.io/v3/9eff8a9d4a1b404997258e00edf4b906"))
	'''这个是分发G水的合约abi和地址，abi不变，地址改为你部署的地址。
	你需要自己部署合约，我会把solidity的源码发你，
	需要知道的是，你用哪个号部署，哪个号就是合约的拥有者，
	只有你自己能调用分发水，部署完合约后往合约里转入你要分发的总数量'''
	faucet_abi=[
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "a",
				"type": "address"
			}
		],
		"name": "claim",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "a",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "b",
				"type": "uint256"
			}
		],
		"name": "sendEther",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "a",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "b",
				"type": "uint256"
			}
		],
		"name": "sendGether",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "a",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "b",
				"type": "uint256"
			}
		],
		"name": "sendWei",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
	# 下面的地址你需要替换成你的
	faucet_address=w3.toChecksumAddress("0xC9B5679ECdd19Ef8f5c1a3e1319BAcE6a3A6EE4A")
	faucet_contract=w3.eth.contract(address=faucet_address,abi=faucet_abi)
	'''这里的boss——address是你刚部署合约时用的地址，bosskey是那个地址的私钥'''
	boss_address=""
	boss_key=""
	'''test是获取主账户的nonce值'''
	test=w3.eth.getTransactionCount(boss_address)

	print(test)
	'''这里注释掉的是生成账户，你把注释取消就会生成账户，下面for循环内填入你生成账户的数量就行了'''
	# WriteAccount(2000)
	for i in range(2000):
		# while True:
		'''异常捕获,出现异常就生成对应的可查看文件'''
		try:
		# 	print(i,'while')
			'''检测有没有成功和RPC连接，没连接就打印出来，记录下来（for循环内没做处理，如果失败了不会重新发起，相当于这个账户失败了）'''
			print(w3.isConnected(),':',i)
			# 		break
			# 	else:
			# 		w3= Web3(HTTPProvider(url[random.randint(0,2)]))
			'''这个是获取生成的账户地址和私钥以及整个文件生成的数量'''
			(address,key,length)=GetAccount(i)
			balance=w3.eth.getBalance(address)
			print(i,":",balance)
			if balance==0:
				print("余额为0:",address)
			'''随机发送0.09~0.1eth,test+i目的是防止nonce太低导致交易失败'''
			result=initFaucet(address,random.randint(90000000000000000,100000000000000000),test+i)
			# time.sleep(5)
			# print(result)
		except Exception as e:
			WrightError(i)
		# else:
		# 	print(i,'error')


# pass