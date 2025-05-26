from Rudadev import Data
def Lib(args: list):
    if " ".join(args[3:]).startswith('"') and " ".join(args[3:]).endswith('"') and args[2] == "=":
        Data.Variables[args[1]] = {"Type": "String", "Value": str(" ".join(args[3:])[1:-1])}
        Data.PackageSession.append([args[1], "String", str(" ".join(args[3:])[1:-1])])
        return ""
    return 0