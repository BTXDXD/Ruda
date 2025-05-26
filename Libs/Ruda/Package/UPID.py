from Rudadev import Data
def Lib(args: list):
    if args[1].startswith('"') and args[1].endswith('"'):
        Data.PackageID = args[1][1:-1]
        return ""
    return 0