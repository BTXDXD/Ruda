from Rudadev import Data
def Lib(args: list):
    if   args[3] == 'true' and args[2] == "=":
        Data.Variables[args[1]] = {"Type": "Boolean", "Value": True}
        Data.PackageSession.append([args[1], "Boolean", True])
        return ""
    elif args[3] == 'false' and args[2] == "=":
        Data.Variables[args[1]] = {"Type": "Boolean", "Value": False}
        Data.PackageSession.append([args[1], "Boolean", False])
        return ""
    return 0