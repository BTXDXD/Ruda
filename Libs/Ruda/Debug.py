from Rudadev import Data
def Lib(args: list):
    if args[1] == "false": Data.DebugMode = False; return ""
    if args[1] == "true": Data.DebugMode = True; return ""
    return 0