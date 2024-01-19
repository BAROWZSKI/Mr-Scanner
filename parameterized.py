import socket
import argparse

def port_scanner(target_ip, start_port, end_port):

    open_ports = []

    print("initializing port scanning...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET represents ipv4 adresees
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port)) #it tries to connect the port of a target

        if result == 0:
            service = socket.getservbyport(port)
            print(f"Port {port} is open and it's runing {service} ")
            open_ports.append(port)

        sock.close()

    return open_ports

objem = argparse.ArgumentParser(description="Simple port scanner USAGE: python portscanner.py [TARGET_IP] [-p] [START PORT] [END PORT]")
objem.add_argument('target_ip',nargs='?',help='required target ip in the first parameter')
objem.add_argument('-p','--port_range',type=int,nargs=2,help='Start Port And End Port Range')

parseettim = objem.parse_args()

#defined start and end port variables

if parseettim.target_ip:
    print(f"Scanning {parseettim.target_ip}...")

    #port aralığını kontrol etmek için
    if parseettim.port_range:
        start_port, end_port = parseettim.port_range
        open_ports = port_scanner(parseettim.target_ip, start_port, end_port)
        if not open_ports:
            print("there is no open port")
        else:
            print(f"Open ports are : {open_ports}")

    else:
        print("Port range not specified scanning first 100 ports...")
        start_port = 0
        end_port = 100
        open_ports = port_scanner(parseettim.target_ip, start_port, end_port)
        if not open_ports:
            print("there is no open port")
        else:
            print(f"Open ports are : {open_ports}")
else:
    objem.print_help()
    #argparse help function
