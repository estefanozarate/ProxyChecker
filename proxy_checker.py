import requests 
from termcolor import colored
import time
import threading


title_proxy_checker_1 = """
    ____                           ________              __            
   / __ \_________  _  ____  __   / ____/ /_  ___  _____/ /_____  _____
  / /_/ / ___/ __ \| |/_/ / / /  / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
 / ____/ /  / /_/ />  </ /_/ /  / /___/ / / /  __/ /__/ ,< /  __/ /    
/_/   /_/   \____/_/|_|\__, /   \____/_/ /_/\___/\___/_/|_|\___/_/     
                      /____/                                                                          
"""
author = """
Github https://github.com/estefanozarate
"""
proxy_dataset = list()
up_proxies = list()
down_proxies = list()

def display_title(title_1, author):
    time.sleep(1)
    print(colored(title_1, "green"))
    time.sleep(0.1)
    print(colored(author, "white"))
    time.sleep(0.1)

def getAndCleanProxyFile(file) -> None:
    with open("proxy_list_100.txt", "r") as proxy_dirty_file:
        for proxy in proxy_dirty_file:
            proxy_dataset.append(proxy.replace("\n", ""))

def getAllProxyList() -> None:
    time.sleep(1)
    print(colored("             Showing All The Proxy IPs        \n  ", "blue"))
    time.sleep(1)
    for proxy in proxy_dataset:
        time.sleep(0.3)
        print(colored(f"Proxy_IP: [ {proxy} ]", "yellow"))
    print("\n")

def checkProxyFunction(proxy_dataset_lst_2) -> None:
    for proxy in proxy_dataset_lst_2:
        try:
            proxy_response = requests.get("http://ipinfo.io/json", proxies={
                                                "http": proxy,"https": proxy}, timeout=5)
        except:
                print(colored(f"[!] Proxy {proxy}: DOWN!", "red"))
                f_down = open("down_proxy.txt", "a")
                f_down.write(f"{proxy} \n")

        print(colored(f"[+] Proxy {proxy}: UP!", "green"))
        f_up = open("up_proxy.txt", "a")
        f_up.write(f"{proxy} \n")
                

def check_all_proxies_with_threads(list_proxies, sublist_size):
    list_of_lists = []
    lst_thread = []
    for i in range(0, len(list_proxies), sublist_size):
        list_of_lists.append(list_proxies[i:i+sublist_size])
    for list_proxy in list_of_lists:
        n_thread = threading.Thread(target= checkProxyFunction, kwargs={
                "proxy_dataset_lst_2": list_proxy})
        n_thread.start()
        lst_thread.append(n_thread)
    for thread in lst_thread:
        thread.join()

if __name__ == "__main__":
    display_title(title_proxy_checker_1,  author)
    getAndCleanProxyFile(file= "proxy_list_100.txt")
    check_all_proxies_with_threads(proxy_dataset, 30)