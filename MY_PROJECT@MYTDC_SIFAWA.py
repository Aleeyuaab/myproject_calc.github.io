from colorama  import Fore, Style, init
import sys
init()

def calculator():
    print("-" * 95)
    print(Fore.CYAN + Style.BRIGHT + "                       WELCOME TO THE SIMPLE ARITHMETIC CALCULATOR" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + "THIS CALCULATOR IS THE PROPERTY OF MALAM YAHAYA DIGITAL TECHNOLOGY CENTER SIFAMA, BODINGA LG." + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + "                              CODED BY (ALIYU ADAMU BODINGA) " + Style.RESET_ALL)
    print("-" * 95)
    print("")
    print(" " * 40)
    print("=" * 40)
    print(Fore.CYAN +  " + Addition " + Style.RESET_ALL)
    print(Fore.CYAN +  " - Subtraction " + Style.RESET_ALL)
    print(Fore.CYAN +  " * Multiplication " + Style.RESET_ALL)
    print(Fore.CYAN +  " / Dvision" + Style.RESET_ALL)
    print("")
    print(Fore.RED + " Exit " + Style.RESET_ALL)  # Red = Danger/Exit
    print("=" * 40)
    print("")


    while True:
        calculation = input(Fore.BLUE + "Pease enter a number: " + Style.RESET_ALL)

        if calculation.lower() == "exit":
            break
            continue

        try:
            result = eval(calculation)
            print(Fore.GREEN + f"Result = {result}" + Style.RESET_ALL)
        except:
            print(Fore.RED + "Error! Please check your calculation" + Style.RESET_ALL)
    
            
calculator()

