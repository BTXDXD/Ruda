from colorama import init, Fore, Back, Style
init(autoreset=True)
from Rudadev import Data
def Lib(args: list):
    if len(args) < 2: return 0
    try:
        parts = " ".join(args[1:]).split("..")
        result = []
        for part in parts:
            part = part.strip()
            if not part: continue
            if part.startswith('"') and part.endswith('"'): result.append(part[1:-1])
            elif part.startswith('!'):
                var_value = Data.Variables.get(part[1:], {}).get("Value")
                if var_value is None: return 0
                result.append(str(var_value))
            else: return 0
        return Fore.YELLOW + ' '.join(result) + "\n"
    except: return 0