#!/usr/bin/env python
import socket
import sys

protocols = {
        "21": "FTP",
        "22": "SSH",
        "23": "TELNET",
        "25": "SMTP",
        "53": "DNS",
        "69": "TFTP",
        "80": "HTTP",
        "443": "HTTPS",
        "110": "POP3",
        "123": "NTP",
        "143": "IMAP",
        "389": "LDAP",
        "67": "DHCP",
        "68": "DHCP",
        }

if len(sys.argv) > 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    hosts = sys.argv[3:]

    for host in hosts:
        if len(host.split(".")) < 4:
            host = socket.gethostbyname(host)
        for port in range(start,end+1):
            info = str(host)+", "+str(port)+", "
            if str(port) in protocols.keys():
                protocol = ", "+protocols[str(port)]
            else:
                protocol = ""
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, port))
                sock.close()
                print info+"OPEN"+protocol
            except socket.error, exc:
                if exc.args[0] == 111:
                    print info+"CLOSED"+protocol
                else:
                    print info+"DROPPED"+protocol
            except KeyboardInterrupt:
                print ""
                sys.exit()

else:
    print "Not enough input arguments."
