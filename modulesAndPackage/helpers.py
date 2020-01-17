# helpers.py
from colorama import init,Fore

init(autoreset=True) 

def display(message,is_warning=False):
    if is_warning:
        print(Fore.RED+'Warning!')
    else:
        print(Fore.BLUE+message)

