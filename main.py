import os
os.system("pip install TBPG")
os.system('clear')
from TBPG import *
import time
import random
import sys

# ANSI escape codes for colors
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
TTP_LOGO = """
 ______  ____   ____    ____ 
|      T|    \ |    \  /    T
|      ||  o  )|  o  )Y   __j
l_j  l_j|     T|   _/ |  T  
  |  |  |  O  ||  |   |  l_ |
  |  |  |     ||  |   |     |
  l__j  l_____jl__j   l___,_j
                             
"""

def random_color(text):
    colors = [RED, GREEN, YELLOW, CYAN, BLUE, MAGENTA]
    return f"{random.choice(colors)}{text}{RESET}"

def display_logo():
    print(f"{GREEN}{BOLD}{TTP_LOGO}{RESET}")

def welcome_message():
    display_logo()
    message = "Welcome to TBPG - Time-Based Password Generator!                   "
    for char in message:
        print(f"{CYAN}{char}{RESET}", end='', flush=True)
        time.sleep(0.06)
    print("\n")

def display_menu():
    os.system('clear')
    print(f"{BLUE}{BOLD}-"*40)
    display_logo()
    print(f"{BLUE}{BOLD}-"*40)
    print(f"{BLUE}{BOLD}| {RESET}{CYAN}{BOLD}1. Get password using current date    {RESET}{BLUE}{BOLD}|")
    print(f"{BLUE}{BOLD}-"*40)
    print(f"{BLUE}{BOLD}|{RESET}{CYAN}{BOLD}2. Receive password using desired date {RESET}{BLUE}{BOLD}|")
    print(f"{BLUE}{BOLD}-"*40)
    print(f"{BLUE}{BOLD}|{RESET}{RED}{BOLD}3. Exit{RESET}                                {RESET}{BLUE}{BOLD}|{RESET}")
    print(f"{BLUE}{BOLD}-"*40)
    print(RESET)
def save_password_to_file(password):
    with open("TBPG.txt", "a") as file:
        file.write(password + "\n")
    print(f"{GREEN}Password saved to TBPG.txt!{RESET}")

def main():
    welcome_message()

    while True:
        display_menu()
        option = input("> ").strip()

        if option == '1':
            os.system('clear')
            password = generaten_now_time_password()
            print(f"{MAGENTA}{password}{RESET}")
            save_option = input(f"{CYAN}Do you want to save this password? (y/n): {RESET}").strip().lower()
            if save_option == 'y':
                save_password_to_file(password)
        
        elif option == '2':
            os.system('clear')
            entered_date = input(f"{CYAN}Enter the date (e.g., 2025-01-28 17:29:13): {RESET}")
            os.system('clear')
            print(f"{CYAN}Converting date to password...{RESET}")
            os.system('clear')
            
            password = None
            try:
                password = convert_time(entered_date)
                print(f"{GREEN}{password}{RESET}")
            except ValueError:
                print(f"{RED}Invalid time format. Please use 'YYYY-MM-DD HH:MM:SS' format.{RESET}")
            
            if password:
                save_option = input(f"{CYAN}Do you want to save this password? (y/n): {RESET}").strip().lower()
                if save_option == 'y':
                    save_password_to_file(password)
        
        elif option == '3':
            print(f"{RED}Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid option! Try again.{RESET}")
        
        print("")
        print("")
        print("")
        input(f"{CYAN} Press  {RESET}{BOLD}{GREEN}Enter {RESET}{CYAN}to CONTINUE...{RESET}")

if __name__ == "__main__":
    main()
