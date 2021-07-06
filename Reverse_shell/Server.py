#!/usr/bin/env python3


import socket

BUFF_SIZE=10
HEADER=10

def commands(conn):
    command=""
    while command != 'exit':
        command=input()
        if command == '':
            print("\n")
            continue
        conn.send(str.encode(command))
        byt=int(conn.recv(HEADER).decode("utf-8"))
        full_msg=""
        count=0
        while (len(full_msg)!=byt):
            msg=conn.recv(BUFF_SIZE).decode("utf-8",'ignore')
            full_msg = full_msg + msg
 
        print(full_msg,end="")
        

def accept():
    conn,address=sock.accept()
#    print("connection established with {}:{}..",format(address[0],str(address[1])))
    commands(conn)
    conn.close()

ip='0.0.0.0'
port= 9999
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print ("binding sockets..")
sock.bind((ip,port))
print("completed binding...")

sock.listen(1)
print("listening on {}:{} ".format(ip,port))


accept()
