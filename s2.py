# s2
import os
import sys
import time
import requests
from colorama import Fore
def __1__():
        os.system("clear")

        print(Fore.GREEN + "Hello\nWelcome Back ;) ")
        time.sleep(2)
        url = input(Fore.YELLOW + "Enter Your Address Target ==>  " )
        time.sleep(1)
        if url == "" or None:
            try:
                print(Fore.RED + "\nOk Good Lunch ;)")
                time.sleep(1)
                sys.exit()
            except:
                pass
        else:
            pass
        print(Fore.YELLOW + "\n[!] - This Is Test The Target ;)")
        time.sleep(2)
        print(Fore.YELLOW + "\n[!] - Pleass 3 Sec Latter ;)")
        time.sleep(3)
        r = requests.get("http://" + url + "/wp-content/plugins/")
        if r.status_code == 404 or r.status_code == 500:
            try:
                print(Fore.RED + "\n[-] - Your Target Not WordPress ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        else:
            try:
                print(Fore.GREEN + "\n[+] - Your Target Is WordPress ;)")

            except:    
             print(Fore.GREEN + "\nPleass Enter You Go To The Mano")
             input("")
             os.system("clear")
__1__()
