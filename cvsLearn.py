#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/31 20:31
# @Author  : 1939205403
# @File    : cvsLearn.py.py
import pandas as pd
from web3 import Web3, HTTPProvider, WebsocketProvider, module,gas_strategies

w3 = Web3(HTTPProvider())
def WriteAccount(i):
    '''

    '''
    address=[]
    key=[]
    dict={"地址":address,"私钥":key}
    df = pd.DataFrame(dict)
    for j in range(i):
        account = w3.eth.account.create()

        df.loc['%s'%j] = [account.address,account.key.hex()]

    df.to_csv('test.csv')
def GetAccount(i):
    
    df=pd.read_csv('test.csv')
    address=df.loc[i]['地址']
    key=df.loc[i]['私钥']
    length=len(df)
    print(len(df))
    return address,key,length

# WriteAccount(10)

