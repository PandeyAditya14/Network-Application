import socket
import argparse
import sys

host = 'localhost'

def echo_server(port):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    sock.bind((host,port))
    sock.listen(5)
    while(True):
        try :
            print("Listening on port 3000")
            client , address = sock.accept()
            # print("%s connected Receiving Data"%(address))
            data = client.recv(2048)
            if data:
                print("Recieved: %s "%data)
                client.sendall(data)
            client.close()
        except KeyboardInterrupt:
            print("\nGood Bye !!")
            break
        except socket.error as er:
            print("An Error occured %s"%(er))
if __name__ == '__main__':
    parser =  argparse.ArgumentParser()
    parser.add_argument('--port',action="store",dest="port",type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)