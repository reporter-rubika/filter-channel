from pyfiglet import Figlet

ZARD = "\033[93m"
SABZ = "\033[92m"
SABZ2 = "\033[32m"
ABI = "\033[94m"
GHORMAZI = "\033[91m"
RESET = "\033[0m"

f = Figlet(font='big')
ascii_art = f.renderText('HR Team')
print(SABZ + ascii_art + RESET)

print(f"{ZARD}making channel code!...{RESET}")

olgo = input(f"{ABI}Enter the (olgo): {RESET}")
bug = input(f"{ABI}Enter the (bug): {RESET}")
dxprit = input(f"{ABI}Enter the (dxprit): {RESET}")
link = input(f"{ABI}Enter the (link): {RESET}")

result = f"http://pornhub.com='{link}'{olgo}+{bug}/[{dxprit}]"

print(f"{GHORMAZI}This is your code:{RESET}")
print(f"{ABI}{(result)}{RESET}")
print(f"{SABZ2}20 other{RESET}")
print(f"{SABZ2}30 obscene{RESET}")
print(f"{SABZ2}5 spam{RESET}")
