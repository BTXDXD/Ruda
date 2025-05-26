from Rudadev import Data
def Lib(args: list):
    if args[3].endswith('f') and args[2] == "=":
        Data.Variables[args[1]] = {"Type": "Double", "Value": float(args[3][:-1])}
        Data.PackageSession.append([args[1], "Double", float(args[3][:-1])])
        return ""
    return 0