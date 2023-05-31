#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 19:52
# @Author  : 1939205403
# @File    : Scroll跨链多合约交互.py.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:18
# @Author  : 1939205403
# @File    : 代币分发合约交互.py
import json
import time
import datetime
import requests
import dbm
import random
import web3
from web3 import Web3, HTTPProvider, WebsocketProvider, module,gas_strategies

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
def numberAddZero(amount):
	print(amount)
	a=w3.toHex(amount)#64
	print(a)
	b=a[2:]
	print(b)
	c=len(b)
	d=64-c
	e=d*'0'
	# print(e)
	end='%s%s'%(e,b)
	# print(end)
	return end
def ToBridge(address,key):
	baseFee = w3.eth.get_block("latest").baseFeePerGas
	maxPriorityFeePerGas = w3.eth.max_priority_fee
	gas=random.randint(305180,325554)
	gasSpend=(2 * w3.toWei(2,'gwei') + maxPriorityFeePerGas)*gas
	balance=w3.eth.getBalance(address)
	print(balance)
	nonce=w3.eth.getTransactionCount(address)
	ScrollCost=w3.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	amount=balance-gasSpend-ScrollCost
	amountData=numberAddZero(amount)
	# print(amountData)
	tx = {
		'from': address,
		'to':w3.toChecksumAddress('0xe5E30E7c24e4dFcb281A682562E53154C15D3332'),
		'value': amount+ScrollCost,
		'nonce': nonce,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'maxFeePerGas': 2 * w3.toWei(2,'gwei') + maxPriorityFeePerGas,
		# EIP-1559 标准的Gas Estimator 推荐 Max Fee = (2 * Base Fee) + Max Priority Fee
		'maxPriorityFeePerGas': maxPriorityFeePerGas,  # w3.eth.max_priority_fee返回分钟级的最大奖励
		# 'gasPrice': w3.toWei(w3.eth.gasPrice,'wei'),
		# 'nonce': nonce,
		'chainId': 5,
		'data': '0x9f8420b3%s0000000000000000000000000000000000000000000000000000000000009c40'%(amountData)
	}
	# 签名
	signed_tx = w3.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w3.toHex(tx_hash)
def MintBUFFICORN(address,key,nonce):
	# baseFee = w4.eth.get_block("latest").baseFeePerGas
	# maxPriorityFeePerGas = w4.eth.max_priority_fee
	gas=random.randint(309988,311166)
	# gasSpend=(3 * baseFee + maxPriorityFeePerGas)*gas
	# balance=w4.eth.getBalance(address)
	# print(balance)
	# nonce=w4.eth.getTransactionCount(address)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost
	# amountData=numberAddZero(amount)
	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0x59Ef5D23edea409FbD03761A57D7078e475f8419'),
		# 'value': amount+ScrollCost,
		'nonce': nonce,
		# 防止因gas过低导致交易失败
		'gas': gas,
		# 'maxFeePerGas': 3 * baseFee + maxPriorityFeePerGas,
		# EIP-1559 标准的Gas Estimator 推荐 Max Fee = (2 * Base Fee) + Max Priority Fee
		# 'maxPriorityFeePerGas': maxPriorityFeePerGas,  # w3.eth.max_priority_fee返回分钟级的最大奖励
		'gasPrice': w4.toWei(
0.019078748,'gwei'),
		# 'nonce': nonce,
		'chainId': 534353,
		'data': '0xf8b81ef7000000000000000000000000000000000000000000000000000000000000000%s'%(str(random.randint(1,2)))
	}

	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)

def MintNFTArena(address,key,nonce):
	gas=random.randint(225964,305180)
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost
	# amountData=numberAddZero(amount)
	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0xaC07EE38FA79d3Cc8d27E3e765f059b3b5D0dD8a'),
		# 'value': amount+ScrollCost,
		'nonce': nonce,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'gasPrice': w3.toWei(
			0.019078748, 'gwei'),
		# 'nonce': nonce,
		'chainId': 534353,
		'data': '0x5704d4e4'
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)
	# pass
def startQuest(address,key,nonce):
	gas=random.randint(68926,78926)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost
	# amountData=numberAddZero(amount)
	test = NFTArena.functions.getPlayers(address).call()
	amountData = numberAddZero(test[0])
	# print(amountData)

	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0xaC07EE38FA79d3Cc8d27E3e765f059b3b5D0dD8a'),
		# 'value': amount+ScrollCost,
		'nonce': nonce,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'gasPrice': w4.toWei(
			0.019078748, 'gwei'),

		# 'gasPrice': w3.toWei(w3.eth.gasPrice,'wei'),
		# 'nonce': nonce,
		'chainId': 534353,
		'data': '0x9e563544%s'%(amountData)#startQuest(uint256 _tokenId)
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)

def endQuest(address,key,nonce):
	gas=random.randint(43802,53802)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost
	test = NFTArena.functions.getPlayers(address).call()
	amountData = numberAddZero(test[0])

	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0xaC07EE38FA79d3Cc8d27E3e765f059b3b5D0dD8a'),
		# 'value': amount+ScrollCost,
		'nonce': nonce,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'gasPrice': w4.toWei(
			0.019078748, 'gwei'),
		'chainId': 534353,
		# 'nonce': nonce,
		'data': '0x235dad5b%s'%(amountData)#endQuest(uint256 _tokenId)
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)
	# pass
def Deposit(address,key,nonce):
	gas=random.randint(45904,55904)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost

	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0x5300000000000000000000000000000000000004'),
		'value': w4.toWei(0.001,'ether'),
		'nonce': nonce,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'chainId': 534353,
		'gasPrice': w4.toWei(
			0.019078748, 'gwei'),

		# 'nonce': nonce,
		'data': '0xd0e30db0'#endQuest(uint256 _tokenId)
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)
def approveETH(address,key,nonce):
	gas=random.randint(57759,65759)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost

	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0x5300000000000000000000000000000000000004'),
		# 'value': w4.toWei(0.001,'ether'),
		'nonce': nonce,
		'chainId': 534353,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'gasPrice': w4.toWei(
			0.001, 'gwei'),

		# 'nonce': nonce,
		'data': '0x095ea7b3000000000000000000000000111690a4468ba9b57d08280b2166aff2bac65248ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'#endQuest(uint256 _tokenId)
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)
def UniSwapV3SwapUSDT(address,key,nonce):
	gas=random.randint(150404,170404)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	amount=int(time.time()+1000)
	amountdaTatimeStamp=numberAddZero(amount)
	swapAmount=w4.toWei(0.0005, 'ether')
	swapAmountData=numberAddZero(swapAmount)
	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0x111690A4468ba9b57d08280b2166AFf2bAC65248'),
		# 'value': w4.toWei(0.001,'ether'),
		'nonce': nonce,
		'chainId': 534353,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'gasPrice': w4.toWei(
			0.001, 'gwei'),

		# 'nonce': nonce,
		'data': '0x5ae401dc%s00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000e404e45aaf0000000000000000000000005300000000000000000000000000000000000004000000000000000000000000a0d71b9877f44c744546d649147e3f1e70a937600000000000000000000000000000000000000000000000000000000000000bb8000000000000000000000000%s%s0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'%(amountdaTatimeStamp,address[2:],swapAmountData)
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)
def approveETH2(address,key,nonce):
	gas=random.randint(57759,65759)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost

	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0x5300000000000000000000000000000000000004'),
		# 'value': w4.toWei(0.001,'ether'),
		'nonce': nonce,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'chainId': 534353,
		'gasPrice': w4.toWei(
			0.001, 'gwei'),

		# 'nonce': nonce,
		'data': '0x095ea7b3000000000000000000000000bd1a5920303f45d628630e88afbaf012ba078f37ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'#endQuest(uint256 _tokenId)
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)
def approveUSDC(address,key,nonce):
	gas=random.randint(55856,65856)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost

	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0xA0D71B9877f44C744546D649147E3F1e70a93760'),
		# 'value': w4.toWei(0.001,'ether'),
		'nonce': nonce,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'chainId': 534353,
		'gasPrice': w4.toWei(
			0.001, 'gwei'),

		# 'nonce': nonce,
		'data': '0x095ea7b3000000000000000000000000bd1a5920303f45d628630e88afbaf012ba078f37ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'#endQuest(uint256 _tokenId)
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)

def addLiquidity(address,key,nonce):
	gas=random.randint(437087,561449)
	# ScrollCost=w4.toWei(0.00000076314992,'ether')
	# amount指的是要传入'data'的发送数量
	# amount=balance-gasSpend-ScrollCost
	amount=int(time.time()+1000)
	amountdaTatimeStamp=numberAddZero(amount)


	# print(amountData)
	tx = {
		'from': address,
		'to':w4.toChecksumAddress('0xbd1A5920303F45d628630E88aFbAF012bA078F37'),
		# 'value': w4.toWei(0.001,'ether'),
		'nonce': nonce,
		'chainId': 534353,
		# 防止因gas过低导致交易失败
		'gas': gas,
		'gasPrice': w4.toWei(
			0.001, 'gwei'),

		# 'nonce': nonce,
		'data': '0x883164560000000000000000000000005300000000000000000000000000000000000004000000000000000000000000a0d71b9877f44c744546d649147e3f1e70a937600000000000000000000000000000000000000000000000000000000000000bb8fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2764c00000000000000000000000000000000000000000000000000000000000d89b4000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000010207de3f800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000%s%s'%(address[2:],amountdaTatimeStamp)#endQuest(uint256 _tokenId)
	}
	# 签名
	signed_tx = w4.eth.account.signTransaction(tx, key)
	# 得到交易哈希
	tx_hash = w4.eth.sendRawTransaction(signed_tx.rawTransaction)
	return w4.toHex(tx_hash)

def getTx(address):
	'''查看账户一共进行了多少次成功的交易,方便判断某个账户是否执行了正确的交互'''
	x = requests.get("https://blockscout.scroll.io/api?module=account&action=txlist&address=%s" % address)
	print("TxAmount:",len(x.json()['result']))
	# if  type(x.json()['result']) is  None:
	# 	print("noneTypeError",i)
	# else:
	# 	number=len(x.json()['result'])
	# 	return number

def WrightErrorAccount(address,key,amount):
	'''如果tx小于某个数值,将该账户写入错误文件amount是int类型的'''
	test=getTx(address)
	if test<amount:
		with dbm.open('AccountScrollError.db', 'c') as db:
			# db['key'] = 'value'
			# db['today'] = 'Monday'
			# db['author'] = 'suk'
			# print(dbm.whichdb('example.db'))
				# 创建账户
			# add.append(account.address)
			db['%s' % address]= '%s' % key
			db.close()
def getBalance(address):
	balance=w3.eth.getBalance(address)
	if balance==0:
		print(address)

if __name__ == '__main__':
	goerliurl = 'https://rpc.ankr.com/eth_goerli'
	goerliurl2="https://goerli.blockpi.network/v1/rpc/public"
	goerliurl3="https://eth-goerli.public.blastapi.io"
	# url=[goerliurl,goerliurl3]
	'''w3 w4分别是G网和scroll的rpc'''
	w3 = Web3(HTTPProvider("https://goerli.infura.io/v3/9eff8a9d4a1b404997258e00edf4b906"))
	w4= Web3(HTTPProvider("https://alpha-rpc.scroll.io/l2"))
	'''经过G网水分发后,每个账户都有了余额
	接下来进行合约交换
	主要有以下NFTArena_address这个是某个小游戏的挖矿'''
	NFTArena_address=w4.toChecksumAddress('0xaC07EE38FA79d3Cc8d27E3e765f059b3b5D0dD8a')
	NFTArena_abi=[{"type":"constructor","stateMutability":"nonpayable","inputs":[]},{"type":"event","name":"ApprovalForAll","inputs":[{"type":"address","name":"account","internalType":"address","indexed":True},{"type":"address","name":"operator","internalType":"address","indexed":True},{"type":"bool","name":"approved","internalType":"bool","indexed":False}],"anonymous":False},{"type":"event","name":"TransferBatch","inputs":[{"type":"address","name":"operator","internalType":"address","indexed":True},{"type":"address","name":"from","internalType":"address","indexed":True},{"type":"address","name":"to","internalType":"address","indexed":True},{"type":"uint256[]","name":"ids","internalType":"uint256[]","indexed":False},{"type":"uint256[]","name":"values","internalType":"uint256[]","indexed":False}],"anonymous":False},{"type":"event","name":"TransferSingle","inputs":[{"type":"address","name":"operator","internalType":"address","indexed":True},{"type":"address","name":"from","internalType":"address","indexed":True},{"type":"address","name":"to","internalType":"address","indexed":True},{"type":"uint256","name":"id","internalType":"uint256","indexed":False},{"type":"uint256","name":"value","internalType":"uint256","indexed":False}],"anonymous":False},{"type":"event","name":"URI","inputs":[{"type":"string","name":"value","internalType":"string","indexed":False},{"type":"uint256","name":"id","internalType":"uint256","indexed":True}],"anonymous":False},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"GOLD","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"PLAYER","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"SHIELD","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"SILVER","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"SWORD","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"URIs","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"_mintPlayer","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"addressToPlayers","inputs":[{"type":"address","name":"","internalType":"address"},{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"addressToSwords","inputs":[{"type":"address","name":"","internalType":"address"},{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"open","internalType":"bool"},{"type":"uint256","name":"hostId","internalType":"uint256"},{"type":"address","name":"hostAddress","internalType":"address payable"}],"name":"arena","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"arenaOpen","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balanceOf","inputs":[{"type":"address","name":"account","internalType":"address"},{"type":"uint256","name":"id","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256[]","name":"","internalType":"uint256[]"}],"name":"balanceOfBatch","inputs":[{"type":"address[]","name":"accounts","internalType":"address[]"},{"type":"uint256[]","name":"ids","internalType":"uint256[]"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"craftSword","inputs":[{"type":"uint256","name":"_tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"endQuest","inputs":[{"type":"uint256","name":"_tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"endTraining","inputs":[{"type":"uint256","name":"_tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"enterArena","inputs":[{"type":"uint256","name":"_tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"equipSword","inputs":[{"type":"uint256","name":"_tokenId","internalType":"uint256"},{"type":"uint256","name":"_swordId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"fightArena","inputs":[{"type":"uint256","name":"_tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getBlocktime","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256[]","name":"","internalType":"uint256[]"}],"name":"getPlayers","inputs":[{"type":"address","name":"_address","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256[]","name":"","internalType":"uint256[]"}],"name":"getSwords","inputs":[{"type":"address","name":"_address","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"isApprovedForAll","inputs":[{"type":"address","name":"account","internalType":"address"},{"type":"address","name":"operator","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bytes4","name":"","internalType":"bytes4"}],"name":"onERC1155BatchReceived","inputs":[{"type":"address","name":"","internalType":"address"},{"type":"address","name":"","internalType":"address"},{"type":"uint256[]","name":"","internalType":"uint256[]"},{"type":"uint256[]","name":"","internalType":"uint256[]"},{"type":"bytes","name":"","internalType":"bytes"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bytes4","name":"","internalType":"bytes4"}],"name":"onERC1155Received","inputs":[{"type":"address","name":"","internalType":"address"},{"type":"address","name":"","internalType":"address"},{"type":"uint256","name":"","internalType":"uint256"},{"type":"uint256","name":"","internalType":"uint256"},{"type":"bytes","name":"","internalType":"bytes"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"openArena","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"owners","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"playerCount","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"hp","internalType":"uint256"},{"type":"uint256","name":"attack","internalType":"uint256"},{"type":"uint8","name":"status","internalType":"enum NFTArena.Status"},{"type":"uint256","name":"wins","internalType":"uint256"},{"type":"bool","name":"item","internalType":"bool"}],"name":"players","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"endTime","internalType":"uint256"}],"name":"quests","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"safeBatchTransferFrom","inputs":[{"type":"address","name":"from","internalType":"address"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256[]","name":"ids","internalType":"uint256[]"},{"type":"uint256[]","name":"amounts","internalType":"uint256[]"},{"type":"bytes","name":"data","internalType":"bytes"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"safeTransferFrom","inputs":[{"type":"address","name":"from","internalType":"address"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"id","internalType":"uint256"},{"type":"uint256","name":"amount","internalType":"uint256"},{"type":"bytes","name":"data","internalType":"bytes"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setApprovalForAll","inputs":[{"type":"address","name":"operator","internalType":"address"},{"type":"bool","name":"approved","internalType":"bool"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"startQuest","inputs":[{"type":"uint256","name":"_tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"startTraining","inputs":[{"type":"uint256","name":"_tokenId","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"supportsInterface","inputs":[{"type":"bytes4","name":"interfaceId","internalType":"bytes4"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"swordCount","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"available","internalType":"bool"},{"type":"address","name":"owner","internalType":"address"}],"name":"swords","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"startTime","internalType":"uint256"}],"name":"trainings","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"uri","inputs":[{"type":"uint256","name":"_id","internalType":"uint256"}]}]
	NFTArena=w4.eth.contract(address=NFTArena_address,abi=NFTArena_abi)
	# test=NFTArena.functions.getPlayers("0xE7073295f45c4e32F6cf119F5aD978b6f0d47999").call()
	# getTx("0x6D119046FD125d9eCeF8Dc7C976099d1BcE79e65")
	for i in range(2000):#1074/;;
		print(i)
		(account, key, length) = GetAccount(i)
		print(key)
		# result=ToBridge(account,key)
		# print(result)
	# 	# WrightErrorAccount(account,key)
	# 	try:
	# 		'''for循环遍历账户'''
	# 		(account,key,length)=GetAccount(i)
	# 		print("第%s个，地址是：  %s"%(i,account))
	#
	# 		x=w4.eth.getTransactionCount(w4.toChecksumAddress(account))
	# 		MintBUFFICORN(w4.toChecksumAddress(account),key,x)
	# 		MintNFTArena(w4.toChecksumAddress(account),key,x+1)
	# 		time.sleep(10)
	# 		'''其中NFTArena可以挖矿和mintNFT为了防止还没mint就先挖矿和还没挖矿就先停矿,所以加延时'''
	# 		startQuest(w4.toChecksumAddress(account),key,x+2)
	# 		time.sleep(10)
	#
	# 		endQuest(w4.toChecksumAddress(account),key,x+3)
	# 		'''将eth换成weth'''
	# 		Deposit(w4.toChecksumAddress(account),key,x+4)
	# 		'''授权weth给uniswapV3池子'''
	# 		approveETH(w4.toChecksumAddress(account),key,x+5)
	# 		'''把weth换成usdt'''
	# 		UniSwapV3SwapUSDT(w4.toChecksumAddress(account),key,x+6)
	# 		'''把weth授权给pair'''
	# 		approveETH2(w4.toChecksumAddress(account),key,x+7)
	# 		'''把usdt授权给pair'''
	# 		approveUSDC(w4.toChecksumAddress(account),key,x+8)
	# 		'''加池子'''
	# 		test=addLiquidity(w4.toChecksumAddress(account),key,x+9)
	# 		# print(i+900)
	# 		# test = NFTArena.functions.getPlayers(account).call()
	# 		print(test,account)
	# 	except Exception as e:
	# 		print("Error:第%s个，地址是：  %s"%(i,account))
	# print(test[0],type(test[0]))
	# print(time.time(),int(time.time()))

	# pass