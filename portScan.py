from socket import *
import optparse
from threading import *
from colorama import Back,Fore,Style

def port_scan(host,port): # port scanning function
    try:
        if len(host.split("."))==4: # checking if the host/ip is ipv4 or ipv6
            sock = socket(AF_INET,SOCK_STREAM)
        else:
            sock = socket(AF_INET6,SOCK_STREAM)
        sock.connect((host,port))
        print(Back.GREEN+"Port: "+str(port)+" is Opened [+] "+Style.RESET_ALL)
    except:
        print(Back.RED+"Port: "+str(port)+" is Closed [!] "+Style.RESET_ALL)
    finally:
        sock.close()

def portscanner(host,port): 
    try:
        t_ip = getaddrinfo(host,80) # to get ip addr information
    except:
        print(Back.RED+"[!] Unknown host: ",t_ip[0],Style.RESET_ALL)

    try:
        t_name = gethostbyaddr(t_ip[0][4][0]) # to get ip of host
        print(Back.GREEN+"[+] Scan results for: "+t_name[0]+Style.RESET_ALL)
    except:
        print(Back.GREEN+"[+] Scan results for: ",t_ip[0][4][0],Style.RESET_ALL)

    if "-" in port: # checking if port are in range
        ports = port.split("-")
        setdefaulttimeout(2)
        for p in range(int(ports[0]),int(ports[1])):
            t = Thread(target=port_scan, args=(host,int(p))) # now calling port_scan function
            t.start()
    else: # if no range is there it will check for single port or multiple ports seperated by commas
        ports = port.split(",")
        setdefaulttimeout(2)
        for p in ports:
            t = Thread(target=port_scan, args=(host,int(p))) # now calling port_scan function
            t.start()

# defining our main function and commandline argunments value
def main():
    parser = optparse.OptionParser("Usage of program: "+" \n-H <target host> Enter host name or ipv4/ipv6 address \n-P <target port> Enter port number or seperated by commans or range of ports \n\t\t example: 80 or 80,90 or 80-1000")
    parser.add_option("-H", dest="t_host", type="string",help="Specify the target host")
    parser.add_option("-P", dest="t_ports", type="string",help="Specify the target port, ports or range")
    (options,args) = parser.parse_args()
    t_host = str(options.t_host)
    t_ports = str(options.t_ports)

    # checking if the host and port is not empty
    if ((t_host==None) or (t_ports==None)):
        print(parser.usage)
        exit()
    else:
        portscanner(t_host,t_ports)
        

if __name__=="__main__":
    main()
