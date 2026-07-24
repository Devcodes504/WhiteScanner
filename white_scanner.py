from  colorama import Fore, Style, init
init()
import time
import os
import requests
import socket
import nmap
#banner
banner = f"""{Fore.GREEN}
╔══════════════╗
║ WHITE SCANER ║
║    by NEXUS  ║
╚══════════════╝
{Style.RESET_ALL}"""

#escanear red
def escanear_red():
    escaner = nmap.PortScanner()
    red = input(f"{Fore.CYAN}[+]{Style.RESET_ALL} {Fore.YELLOW}ingresa  la ip: ")
    time.sleep(1.0)
    print(f"{Fore.GREEN}Escaneando  red... {Style.RESET_ALL}")
    try:
        escaner.scan(hosts=red,arguments='-sn')
        for host in escaner.all_hosts():
            print(f"{Fore.CYAN}[=]{Style.RESET_ALL} {Fore.GREEN}Dispositivo encontrado: {host}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}[=]{Style.RESET_ALL}{Fore.YELLOW} Estado: {escaner[host].state()}{Style.RESET_ALL}")
            print(f"{escaner[host].hostname()}")
            print("-" * 30)
    except:
      print(f"{Fore.RED}a ocurrido un error: {e}{Style.RESET_ALL}")



#escanear puertos 
def escanear_puertos():
    ip = input(f"{Fore.CYAN}[+]{Style.RESET_ALL} {Fore.YELLOW}Ingrese la ip a escanear: {Style.RESET_ALL}")
    puertos = [21,22,23,25,53,80,110,143,443,8080,3306,3389]
    print(f"{Fore.CYAN}[+]{Style.RESET_ALL} {Fore.GREEN}Escaneando puertos de{Style.RESET_ALL}   {ip}")
    for puerto in puertos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, puerto)) == 0:
            print(f"{Fore.CYAN}[+]{Style.RESET_ALL} Puerto {puerto} abierto")
        s.close()


#salir del programa
def salir():
    exit()

#obtener mi ip publica
def ip():
    respuesta = requests.get("https://api.ipify.org?format=json")
    ip = respuesta.json()["ip"]
    print(f"{Fore.GREEN}Tu ip publica es:{Style.RESET_ALL} {ip}")
    
#opciones
while True:
    print(banner)
    print(f"{Fore.CYAN}[1]{Style.RESET_ALL} Escanear Red")
    print(f"{Fore.CYAN}[2]{Style.RESET_ALL} Escanear puertos")
    print(f"{Fore.CYAN}[3]{Style.RESET_ALL} Ver mi ip publica")
    print(f"{Fore.CYAN}[4]{Style.RESET_ALL} Salir")
    
    try:
        opcion = int(input(f"\n{Fore.CYAN}[+]{Style.RESET_ALL} {Fore.YELLOW}Ingrese una opcion: {Style.RESET_ALL}"))
    except:
         print("Ingrese una opcion valida")
    if opcion == 1:
        escanear_red()
    if opcion == 2:
        escanear_puertos()
    elif opcion == 3:
             ip()
    elif opcion == 4:
        salir()
    
