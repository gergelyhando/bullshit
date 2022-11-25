import colorama
from colorama import Fore
print("  ")
print(
    Fore.RED + f"print(x) x = 5" + Fore.RESET + "  " "<<<---Ebből lett az x változó értéke 5" + "\n" + Fore.RED + 'y = "John"' + Fore.RESET + '  '' <<<---Ebből lett John\n')
colorama.init()
print(Fore.BLUE + "Hello\n " + Fore.RESET)  # ITT ütöm ki a blue-t, mégpedig ezzel: + Fore.RESET
string = "Fasza!!! :::::)))))"
fasza = string.upper()
print("Egyik megoldás")
print(f'{Fore.GREEN}{fasza + Fore.RESET}' ' ''#Ez itt a (string.upper)() segítségével lett nagybetűs\n')
print("Másik megoldás")
print(Fore.GREEN + string.upper(), end=""+ Fore.RESET)
print(" ""#Ez itt a (string.upper)() segítségével lett nagybetűs")
