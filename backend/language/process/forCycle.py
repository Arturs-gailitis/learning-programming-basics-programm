from shlex import split

def findCycleEnd(CodeLines: list[str], startIndex: int) -> int:

    """
    iegūst indeksu, kur dotais cikls beidz strādāt
    """

    searchLines = CodeLines[startIndex + 1:]
    BlockCount = 0
    endIndex = 0

    for position, line in enumerate(searchLines, startIndex + 1):

        line = line.strip()

        if line == "":
            continue

        lineObjects = split(line, posix=False)
        firstWord = lineObjects[0]

        forCycleBlock = False
        whileCycleBlock = False

        # skatās vai sākas latviskotais for vai while cikls
        forCycleBlock = firstWord == "cikls" and "lidz" in lineObjects
        whileCycleBlock = firstWord == "kamer" and "tad" in lineObjects

        # nosaka kurā indeksā cikls beidzās
        if firstWord == "ja" or forCycleBlock == True or whileCycleBlock == True:
            BlockCount = BlockCount + 1
            continue
        elif firstWord == "beigas" and BlockCount > 0:
            BlockCount = BlockCount - 1
            continue
        elif firstWord == "beigas" and BlockCount == 0:
            endIndex = position
            return endIndex

def findForCycleRepeatTime(line: str, var: dict) -> tuple [int, int]:

    """
    iegūst cikla iterāciju daudzumu
    """

    start, end = 0, 0

    lineObjects = split(line, posix=False)

    # iegūst iterāciju sākuma un beigu vērtības teksta formātā
    startValue = lineObjects[lineObjects.index("lidz") - 1]
    endValue = lineObjects[lineObjects.index("lidz") + 1].rstrip(":")

    # iegūst iterāciju sākuma un beigu vērtības cipara formātā
    if startValue in var:
        start = var[startValue]
    else:
        start = int(startValue)

    if endValue in var:
        end = var[endValue]
    else:
        end = int(endValue)

    time = end - start + 1

    return start, time

def getIteration(lineObject: list, var: dict, startValue = 0, value = False) -> None | str:

    """
    izveido cikla iterācijas mainīgo vai iegūsti tās nosaukumu
    """

    name = lineObject[1]

    if value == False:
        var[name] = startValue
    else:
        return name