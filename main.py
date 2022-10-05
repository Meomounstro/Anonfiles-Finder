import os, requests, re, json, time, random
from bs4 import BeautifulSoup
from colorama import Fore

os.system("cls")

wor = 'abcdefghijklmnopqrstuvwxyz'
wor2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '123456789'
uni = f'{wor}{num}'
pas = ''.join(random.sample(uni,10))


art = """

 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██████╗ 
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║╚════██╗
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║  ▄███╔╝|
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║  ▀▀══╝ 
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║  ██╗   
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═╝   
                                             
"""
print(art)
a = input("""[+] Presiona enter para continuar..
""")

while True:
    user = ""
    uni = f'{wor}{num}{wor2}'
    pas = ''.join(random.sample(uni,10))

    response = requests.get(f"https://anonfiles.com/{pas}")

    if (response.status_code == 200):
        print(Fore.WHITE + "[+] " + Fore.CYAN + f"FOUNDED: {pas}")
    elif (response.status_code == 404):
        print(Fore.WHITE + "[-] " + Fore.RED + f"NOT FOUND: {pas}")
