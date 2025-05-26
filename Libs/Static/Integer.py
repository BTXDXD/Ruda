from Rudadev import Data
def Lib(args: list):
    if args[3].endswith('n') and args[2] == "=":
        Data.Variables[args[1]] = {"Type": "Integer", "Value": int(args[3][:-1])}
        Data.PackageSession.append([args[1], "Integer", int(args[3][:-1])])
        return ""
    return 0