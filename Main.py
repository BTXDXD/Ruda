from colorama import init, Fore, Back, Style
init(autoreset=True)
import Exparlex, sys
from Rudadev import Data
from pathlib import Path

def Main():
    args = sys.argv[1:]
    if len(args) == 1:
        Libsdir = Path("Libs")
        if not Libsdir.exists(): Libsdir.mkdir()
        with open(args[0], 'r', encoding="utf-8") as F:
            F = F.read()
            C = Exparlex.Execute(F)
            if Data.DebugMode == True:
                print(Fore.LIGHTBLACK_EX + str(Exparlex.Lexing(F)))
                print(Fore.LIGHTBLACK_EX + str(Data.Variables))
                print(Fore.LIGHTBLACK_EX + "Package ID: " + Data.PackageID)
                print(Fore.LIGHTBLACK_EX + "Package Session: " + str(Data.PackageSession))
            if isinstance(C, list):
                for i in C: print(i, end="")
            else: print(C)
        package_dir = Path(f"UPIDs/{Data.PackageID}")
        package_dir.mkdir(parents=True, exist_ok=True)
        for item in Data.PackageSession:
            if len(item) >= 2:
                file_path = package_dir / f"{item[1]}/{item[0]}"
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, 'w', encoding='utf-8') as f:
                    if len(item) >= 3: f.write(str(item[2]))
                    else: f.write('')
    else: return None

if __name__ == "__main__": Main()