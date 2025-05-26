import os

def Execute(args: str):
    result = Lexing(args)
    result = Parsing(result)
    return result

def Lexing(args: str):
    lines = args.strip().split('end')
    result = []
    for line in lines:
        line = line.strip()
        if '//' in line: line = line.split('//')[0].strip()
        if line:
            words = line.split()
            result.append(words)
    return result

def Parsing(args: list):
    Line = 0
    def E(): return f"[#] String {Line}"
    def noLib(): return f"[#] String {Line}. No Lib() in {sublist[1]}"
    def zeroReturn(): return f"[#] String {Line}. Lib() -> Error"
    result = []
    for sublist in args:
        Line += 1
        path_parts = sublist[0].split('.')
        file_path = os.path.join('Libs', *path_parts) + '.py'
        if not os.path.exists(file_path): return E()
        with open(file_path, "r", encoding="utf-8") as F: code = F.read()
        Namespace = {}
        try: exec(code, Namespace)
        except Exception as e: return E()
        if "Lib" not in Namespace: return noLib()
        try:
            lib_result = Namespace["Lib"](sublist)
            if lib_result == 0: return zeroReturn()
            result.append(lib_result)
        except Exception as e: return E()
    while '' in result: result.remove('')
    return result