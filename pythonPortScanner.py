import socket
import sys
from datetime import datetime
target = input("please Type the IP to be Scanned: ")
ports = int(input("How many Ports u need to be scanned (ex.500): "))
protocolname = 'tcp'

#banner
print("="*80)
print("checking for Open ports on {}".format(target))
print("time started: ", str(datetime.now()))
print("="*80)

try:
    for port in range(1, ports):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        connecting = s.connect_ex((target,port))
        if connecting == 0:
            print("Port {} is up!".format(port), "and is running", socket.getservbyport(port, protocolname))
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program..")
    sys.exit()

except socket.gaierror:
    print("{} address can't be resolved".format(target))
    sys.exit()

except socket.error:
    print("Can't contact Target.")
    sys.exit()
