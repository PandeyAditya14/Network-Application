#!/usr/bin/python3.8.2
# This is program to display Host info
import socket
def print_info():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    print("Hostname: ",hostname, sep=" ")
    print("Ip Address",ip_addr,sep=" ")

if __name__ == '__main__':
    print_info()