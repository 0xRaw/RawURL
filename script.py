import requests 
import sublist3r
import colorama
from colorama import Fore, Back, Style  
# Making a GET request 
colorama.init(autoreset=True)
link=input(Fore.WHITE+"-"+"Insert Your Link To Enumerate Subdomain\'s : ")
txtfile=input("-"+"Output file"+Fore.RED+" (should end with .txt)"+Fore.WHITE+" : ")
print(Fore.RESET)
print("Coded By 0xRaw | Twitter:"+Fore.BLUE+" @0xRaw"+Fore.RESET)
print("Be Patient Your Lovely Tool is Running...")
print(Fore.CYAN+"Note: Output File will save the Subdomain Enumration Only.")
print(Fore.RESET)
subdomains = sublist3r.main(link, 40, txtfile, ports= None, silent=True, verbose= True, enable_bruteforce= False, engines=None)
f = open(txtfile, "r")
for x in f:
    y=x
    z=x
    try:
        if "http://" not in x :
            x = "http://"+x
        req_http = requests.get(x.split()[0])
        if "https://" not in y:
            y="https://"+y
        req_https = requests.get(y.split()[0])
    except:
            continue
    finally:
        print(Fore.CYAN+"Orignal URL: "+z)
        print("using"+Fore.MAGENTA+" HTTP:") #printing the Http URL
        print(Fore.RESET)
        if req_http.status_code == 200:
            print(Fore.GREEN+"Found,200")
            print(Fore.RESET)
        elif req_http.status_code == 404 or 403:
            print(Fore.RED+ "Forbidden or NotFound")
        print("using"+Fore.MAGENTA+" HTTPS:")
        print(Fore.RESET)
        if req_https.status_code == 200:
            print(Fore.GREEN+"Found,200")
        elif req_https.status_code == 404 or 403:
            print(Fore.RED+ "Forbidden or NotFound")
        print("\n")
