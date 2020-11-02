import socket
import argparse
import sys

def talk_server(hostname , port):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
    try:
        print("Connecting to server %s on port %s"%(hostname,port))
        sock.connect((hostname,port))
        data = input("Enter the message to be echoed")
        sock.sendall(data.encode('utf8'))
        data=sock.recv(2048)
        if(data):
            print("Server said:%s"%(data))
        sock.close()
    except KeyboardInterrupt:
        print("BYE!")
    except socket.error as er:
        print("an Error occured %s"%(er))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host',action="store",dest="host",type=str ,required=True)
    parser.add_argument('--port',action="store",dest="port",type=int ,required=True)
    get_args = parser.parse_args()
    hostname = get_args.host
    port = get_args.port
    talk_server(hostname,port)


