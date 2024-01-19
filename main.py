import subprocess   #checks if colorama installed or not
import sys          #for installing colorama using pip
import time         #for animations
import socket       #for port scanning and connections
import os           #for cleaning the terminal

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#nt (new technology) stands for Windows, and 'cls' is used to clear the terminal. In Linux or Macos, 'clear' is used for the same purpose.

clear_screen()

print("checking if coloroma installed...")

def check_installation(package):
    try:
        subprocess.check_output([sys.executable, '-m', 'pip', 'show', package])
        print(f"{package} already installed")
        return True
    except subprocess.CalledProcessError:
        print(f"{package} coloroma is not exist, installing...")
        return False

def install_colorama():
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'colorama'])
        print("colorma installation succesfull!")
        print("don't worry it's just a python library")
    except Exception as e:
        print(f"Error occured : {e}")

package_name = "colorama"

if not check_installation(package_name):
        install_colorama()

from colorama import init, Fore, Back, Style #for coloring the logo

init(autoreset=True)
#resets the color settings

def print_color(text, color):
    print(f"{color}{text}")
#animate_start function calls it it is contains the main colors in port scanner

def GetIpAdress(domain):
    try:
        ip_adress = socket.gethostbyname(domain)
        # ghostbyname
        print(f"ip adress : {ip_adress}")
    except socket.error as e:
        print(f"error {e}")

def port_scanner(target, start_port, end_port):

    open_ports = []

    print("initializing port scanning...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET represents ipv4 adresees
        sock.settimeout(1)

        result = sock.connect_ex((target, port)) #it tries to connect the port of a target

        if result == 0:
            service = socket.getservbyport(port)
            print(f"Port {port} is open and it's runing {service} ")
            open_ports.append(port)

        sock.close()

    return open_ports

def animate_start():
    print_color("███╗   ███╗██████╗        ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗", Fore.RED)
    time.sleep(0.2)
    print_color("████╗ ████║██╔══██╗       ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗", Fore.YELLOW)
    time.sleep(0.2)
    print_color("██╔████╔██║██████╔╝       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝", Fore.GREEN)
    time.sleep(0.2)
    print_color("██║╚██╔╝██║██╔══██╗       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗", Fore.CYAN)
    time.sleep(0.2)
    print_color("██║ ╚═╝ ██║██║  ██║██╗    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║", Fore.BLUE)
    time.sleep(0.2)
    print_color("╚═╝     ╚═╝╚═╝  ╚═╝╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝", Fore.MAGENTA)
    time.sleep(0.2)
    print_color("------------------------------created by  Yiğit Durbak----------------------------------",Fore.LIGHTCYAN_EX)
    time.sleep(0.5)
animate_start()

print(Fore.RED + '''For scanning ports , the ip of a website required. If you dont know the ip choose first section
1- Find ip by domain
2- Port scanning
q- Quit
''')

while True:
    user_choice = input(Fore.CYAN + "Choose 1 or 2 and q for quit : ")

    if user_choice == '1':

        user_input = input(Fore.LIGHTRED_EX + "enter a domain : ")
        GetIpAdress(user_input)
        print()

    if user_choice == '2':

        target = input(Fore.GREEN + "Enter your target ip : ")
        start_port = int(input(Fore.YELLOW + "Enter your start port : "))
        end_port = int(input(Fore.LIGHTMAGENTA_EX + "Enter your end port : "))

        open_ports = port_scanner(target, start_port, end_port)

        if not open_ports:
            print(Fore.RED + "there is no open port")
        else:
            print(f"Open ports are : {open_ports}")

        print()

    if user_choice == 'q':
        print(Fore.YELLOW + "Bye! Bye!")
        break