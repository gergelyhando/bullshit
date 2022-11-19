import colorama
from colorama import Fore

print("\nHelló Nirikém!!!")
print("                     ")
# Itt most valami egész más következik, mégpedig pár változó :-)
print("Itt most valami egész más következik, mégpedig pár változó :-)\n")
x = 5
y = "John"
print(x)
print(y) #Ide pl hogy rakok sortörést, mert a \n hibát dob?
print("ezek a következőböl születtek:")
print(Fore.GREEN + "print(x) x = 5 <<<---Ebből lett az x változó értéke 5\n")
print('y = "John"'' ''<<<---Ebből lett John\n')
colorama.init()
print(Fore.BLUE + "Hello\n " + Fore.RESET)  # ITT ütöm ki a blue-t, mégpedig ezzel: + Fore.RESET
string = "Fasza!!! :::::)))))"
print(string.upper())
print(Fore.GREEN + "#Ez itt a (string.upper)() segítségével lett nagybetűs")
