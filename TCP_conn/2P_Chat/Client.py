import socket
import argparse
import sys

def talk_server(hostname , port):
    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.connect((hostname,port))
        while(True):
            data = input("Client: ")
            sock.sendall(data.encode('utf8'))
            if(data == "END"):
                sock.close()
                break
            data = sock.recv(2048)
            data = data.decode('utf8')
            print("Server: %s"%(data))
            if(data == "END"):
                sock.close()
                break
    except KeyboardInterrupt:
        try:
            sock.close()
        except OSError :
            pass
        print("Connection Closed")
    except socket.error as er:
        print(er)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host',action="store",dest="host",type=str ,required=True)
    parser.add_argument('--port',action="store",dest="port",type=int ,required=True)
    get_args = parser.parse_args()
    hostname = get_args.host
    port = get_args.port
    talk_server(hostname,port)
