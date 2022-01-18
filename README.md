# portScanner
---
## This is a simple port scanner made using python-3 socket programming with threaded scan.

### Features of this port scanner:

- Scan for both ipv4 and ipv6 address
- Threaded scan
- Single port, multiple port and port range scan
- Scan using both host name and of ip address
- Little colourful in commandline also


### Modules used:
- socket
- optparse
- threading
- colorama


## Download and Use this port scanner:

**Note**: Python-3 must be installed before running this script.
```
Step 1: Download the file "portScan.py"
Step 2: Open cmd and run following command:
        pip install colorama
        Other modules are already included in standard python library.
Step 3: Hurray!! We are done. Let's run this script. Open cmd or terminal and use following examples,
        options: 
        -H <target host or ip address>
        -P <target port>
        _________________________________________________
        examples:
        python portScan.py --help
        python portScan.py -H 127.0.0.1 -P 80
        python portScan.py -H 127.0.0.1 -P 80,90
        python portScan.py -H 0::1 10-100
```
(**Note**: In cmd/terminal 'python' for windows and 'python3' for linux)
        
