# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 21:51:06 2019

@author: Mehmet Öztürk
"""
import socket
import threading

HEADER = 64 
PORT = 5050  
SERVER = "192.168.0.0" 
ADDR = (SERVER, PORT)  
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) 




def handle_client(conn, addr):
    
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) 
        if msg_length: 
            msg_length = int(msg_length) 
            msg = conn.recv(msg_length).decode(FORMAT) 
            if msg == DISCONNECT_MESSAGE: 
                connected = False 
            print(f"[{addr}] {msg}") 
            conn.send("Msg received".encode(FORMAT)) 
            
            with open ("C:\\Users\\User\\Desktop\\data.txt","w") as data:
                data.write(msg)
                
            
    conn.close()

def start(): 
    server.listen() 
    print(f"[LISTENING] Server is listening on {SERVER}") 
    while True:
        conn, addr = server.accept() 
        thread = threading.Thread(target=handle_client, args=(conn, addr)) 
        thread.start() 
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    

print("[STARTING] server is starting...")
start()


