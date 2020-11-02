import socket 

def get_serv_info():
    for i in range(1,1025):
        try:
            print("Port : %s has Service: %s"%(i , socket.getservbyport(i)))
        except socket.error as err:
            pass
            # print("Error : %s occured at port %s"%(err,i))
if __name__ == '__main__':
    get_serv_info()