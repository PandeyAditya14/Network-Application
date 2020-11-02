import ntplib 
from time import ctime

def ntp_time():
    ntp_client = ntplib.NTPClient()
    res = ntp_client.request('pool.ntp.org')
    print(ctime(res.tx_time))

if __name__ == '__main__':
    ntp_time()