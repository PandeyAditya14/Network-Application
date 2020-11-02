import socket
import argparse
import sys

hostname = 'localhost'

def server(port):
    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.bind((hostname,port))
        sock.listen(1)
        while(True):
            print("listening on port 3000")
            client , address = sock.accept()
            op = True
            while(op):
                data = client.recv(2048)
                if(data.decode('utf8') == "END"):
                    client.close()
                    break
                print("Client: %s"%(data.decode('utf8')))
                data = input("Server: ")
                client.sendall(data.encode('utf8'))
                if(data == "END"):
                    client.close()
                    break; 
    except KeyboardInterrupt :
        try:
            client.sendall("END".encode('utf8'))
        except OSError :
            pass
        print("SERVER SHUT DOWN")
    except socket.error as er:
        print(er)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port' , action="store" , dest="port" , type= int , required=True)
    get_args = parser.parse_args()
    port = get_args.port
    server(port)