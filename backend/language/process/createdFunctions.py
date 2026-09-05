from re import search
from shlex import split

from process.math import mathForFunctions

def createFunction(func: list, line: str, codeLines: list[str], index: int) -> int:

    """
    izveido jaunas funkcijas datus un to ieliek vajadzīgajā funkcijas sarakstā
    """

    returnFunction = False

    lineObjects = split(line, posix=False)

    # skatās vai funkcija beigās atgriezīs vērtību
    if lineObjects[0] == "atgriezta":
        returnFunction = True

    # ar regex palīdzību iegūst funkcijas nosaukumu un izmantojamos argumentus
    functionName = str(search(r"(\S+)\(", line).group(1))
    arguments = list(search(r"\((.*)\)", line).group(1).split(","))

    changedArguments = {}

    for argIndex, arg in enumerate(arguments):

        # pārbauda vai pirms argumentiem nav tukša vieta
        if " " in arg:
            changedArguments[argIndex] = arg.strip()
            continue

    # atjaunina argumentu sarakstu
    for argIndex, value in changedArguments.items():
        arguments[argIndex] = value

    # iegūst funkcijas sākuma un beigu indeksu
    start, end = findFunctionStartEndIndex(codeLines, index)

    # iekiek funkcijas datus šādā secībā: 
    # functionName - funkcijas nosaukums
    # startIndex - vieta kur jāsāk skatīties, ja izsauc konkrēto funkciju
    # endIndex - vieta kur jābeidz skatīties, ja izsauc konkrēto funkciju
    # parameters - funkcijas parametri, kur ir jāievieto, kad izsauc konkrēto funkciju
    # return - vai funkcija atgriezīs vērtību vai nē
    func.append({
        "functionName": functionName,
        "startIndex": start,
        "endIndex": end,
        "parameters": arguments,
        "return": returnFunction
    })

    return end

def startingFunction(functionName: str, functions: list, line: str, mathOp: list, var: dict) -> tuple [int, int, bool]:

    """
    izpilda izsauktās funkcijas sagatavošanās darbus un iedot nepieciešamos datus
    """
    
    functionStart, functionEnd = 0, 0
    parameters = []
    functionReturn = None
    
    for func in functions:

        # iegūst konkrētās funkcijas datus
        if func["functionName"] == functionName:
            functionStart = func["startIndex"]
            functionEnd = func["endIndex"]
            parameters = func["parameters"]
            functionReturn = func["return"]
            break

    # iegūst izsauktā funkcijas ievietotos parametrus
    arguments = list(search(r"\((.*)\)", line).group(1).split(","))
    changedArguments = {}
    
    for argIndex, arg in enumerate(arguments):

        arg = arg.strip()

        # pārtaisi parametrus, ja tajā iekšā ir matemātikas operācijas
        if any(mat in arg for mat in mathOp):
            value = mathForFunctions(arguments, argIndex, var)
            changedArguments[argIndex] = value
            continue

        # nomaini parametrus, lai tie būtu mainīgo vērtības vai arī vērtība ar pareizu datu tipu
        if arg in var:
            changedArguments[argIndex] = var[arg]
            continue

        if arg == "patiess":
            changedArguments[argIndex] = True
            continue
        elif arg == "nepatiess":
            changedArguments[argIndex] = False
            continue

        if arg.startswith('"') == True:
            changedArguments[argIndex] = arg.strip('"')
            continue

        try:
            changedArguments[argIndex] = int(arg)
        except ValueError:
            changedArguments[argIndex] = float(arg) 

    for argIndex, value in changedArguments.items():
        arguments[argIndex] = value

    i = 0


    # ievieto visus parametrus, kā jaunus pagaidu mainīgos
    while i < len(parameters):

        var[parameters[i]] = arguments[i]
        i = i + 1

    return functionStart, functionEnd, functionReturn

def findFunctionStartEndIndex(codeLines: list[str], index: int) -> tuple [int, int]:

    """
    iegūst funkcijas sākuma un beigu indeksus
    """

    startIndex = index + 2
    endIndex = 0

    lines = codeLines[index:]

    for codeIndex, line in enumerate(lines, index):

        line = line.strip()

        if line == "":
            continue

        # ja līnijā parādās iebūvētā printēšanas funkcija tad šo līniju pāriet garām
        # tas tiek darīts lai nebūtu problēmas ar split metodi un printēšanas funkciju
        if line.startswith("printet("):
            continue

        lineObjects = split(line, posix=False)

        if len(lineObjects) > 1 and lineObjects[0] == "funkcijas" and lineObjects[1] == "beigas":
            endIndex = codeIndex
            break

    return startIndex, endIndex