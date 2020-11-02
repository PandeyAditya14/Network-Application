import socket

def remote_info(server):
    try:
        print("IP for %s is : %s"%(server,socket.gethostbyname(server)))
    except socket.error as err_msg:
        print("Error Occured %s"%(err_msg))

if __name__ == '__main__':
    server="facebook.com"
    remote_info(server)