import os, sys, subprocess, json
from bs4 import BeautifulSoup as bs

import itertools

#from pyjsparser import parse
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor

bot = '/pycryptobot.py'
path = os.path.dirname(os.path.abspath(__file__))
bot = path + bot

with open(r'ecosystem.config.js', 'r') as infile:
    data = infile.read()
    data = data.split('=')[-1]
    json.loads(data)




    # args = ["python", bot, "--exchange", "binance", "--stats", "--statgroup"]
    
    # for b in pairs:
    #     args.append(str(b).strip())

    # print(args)  
    #subprocess.call(args, cwd=path)
