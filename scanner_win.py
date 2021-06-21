import socket
import pyperclip


#input data format example:
#1.1.1.1 80
#2.2.2.2 443


def port_scan(host_ip, host_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    result = sock.connect_ex((host_ip, int(host_port)))
    if result == 0:
        sock.close()
        return "Host {0} Port {1}: Open".format(host_ip, host_port)
    elif result == 10061:
        sock.close()
        return "Host {0} Port {1}: Connection refused - TCP RST received".format(host_ip, host_port)
    elif result == 10060:
        sock.close()
        return "Host {0} Port {1}: Connection Timeout".format(host_ip, host_port)
    elif result == 10035:
        sock.close()
        return "Host {0} Port {1}: Connection Timeout".format(host_ip, host_port)
    else:
        sock.close()
        return "Host {0} Port {1}: Connection ended with WinSock error code: {2}".format(host_ip, host_port, result)


ip_port = list()

for line in pyperclip.paste().splitlines():
    ip_port.append(line.split())

for ip, port in ip_port:
    print(port_scan(ip, port))
