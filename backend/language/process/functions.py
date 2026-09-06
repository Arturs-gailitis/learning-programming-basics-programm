from process.variables import isVariable, getVariable, isListElement, getListElement, isBool, isString, isInt, isFloat

from re import fullmatch, search
from typing import Any

def splitParts(text: str, simbol: str) -> list[str]:

    """
        sagriež funkcijas parametrus
    """

    splittingParts = []
    part = ""
    quoteStatuss = False
    quoteSimbol = '"'

    # iet cauri katram simbolam
    for char in text:

        # skatās vai pašreizējais simbols neatrodās string tekstā
        if char == quoteSimbol and quoteStatuss == False:
            quoteStatuss = True
        elif char == quoteSimbol and quoteStatuss == True:
            quoteStatuss = False

        # skatās vai simbols nav saistīts ar sadalīšanu vai arī tas ir simbols priekš teksta
        if char == simbol and quoteStatuss == True:
            part = part + char
        elif char == simbol and quoteStatuss == False:
            splittingParts.append(part.strip())
            part = ""
        else:
            part = part + char

    splittingParts.append(part.strip())

    return splittingParts

def printing(line: str, var: dict, printedResult: list) -> None:

    """
        izveido printēšanas tekstu, kuru pados lietotājam pēc visa pseudokoda nolasīšanas 
    """

    # pārbauda vai rinda pinībā atbilst printet(printēšanas_teksts)
    match = fullmatch(r"printet\s*\((.*)\)", line.strip())

    # ja nē tad beidz darboties un iet nākošo rindu
    if match is None:
        return

    # iegūst tikai to daļu, kas atrodās printēšanas funkciju iekavās
    text = match.group(1).strip()
    result = ""

    # sagriež tekstu daļās skatoties + zīmes lokāciju
    textPieces = splitParts(text, "+")

    for piece in textPieces:

        piece = piece.strip()

        # pārbauda un iegūst konkrēto vērtību no iepriekš izveidotajiem mainīgajiem, sarakstiem vai arī iegūst jaunas vērtības ar to pareizu datu tipu
        if isVariable(piece, var):
            value = getVariable(piece, var)
            value = changingBool(value)
        elif isListElement(piece, var):
            value = getListElement(piece, var)
            value = changingBool(value)
        elif isBool(piece):
            value = changingBool(piece).strip('"\'')
        elif isString(piece):
            value = piece.strip('"\'')
        elif isInt(piece):
            value = int(piece)
        elif isFloat(piece):
            value = float(piece)

        # visu saliek kopā lai tiktu iegūts printēšanai vajadzīgais teksts
        result = result + str(value)

    printedResult.append(result)


def changingBool(value: Any) -> str | int | float | list:

    """
        pārtaisa bool vērtību lai tā atbilstu latviskotajam pseudokodam 
    """

    if isinstance(value, bool):

        if value == True:
            return "patiess"
        else:
            return "nepatiess"

    else:
        return value

def getListSize(line: str, var: dict) -> str:

    """
        iegūst izvēlētā masīva kopējo garumu un to aizvieto  
    """

    # iegūst no pseudokoda rindas masīva nosaukumu
    match = search(r"izmers\(\s*(\w+)\s*\)", line)

    if match is None:
        return line

    name = match.group(1)
    list = getVariable(name, var)
    size = str(len(list))

    # nomaina koda rindas vietu, kur atradās izmers() funkcija ar izvēlētā masīva garuma skaitu
    line = line.replace(match.group(0), size)

    return line

def addElementInList(line: str, var: dict) -> None:

    """
        ieliek jaunu elementu masīva beigās 
    """

    # pārbauda vai rinda pinībā atbilst ielikt() funkcijai
    match = fullmatch(r"ielikt\s*\((.*)\)", line.strip())

    if match == None:
        return

    text = match.group(1).strip()
    variables = splitParts(text, ",")

    # uzreiz nodefinē kā list mainīgo, lai ar pitona list funkcijām būtu okey
    targetedList: list = getVariable(variables[0], var)
    value = None

    if isVariable(variables[1], var):
        value = getVariable(variables[1], var)
    elif isListElement(variables[1], var):
        value = getListElement(variables[1], var)
    elif isBool(variables[1]):

        if variables[1] == "patiess":
            value = True
        else:
            value = False

    elif isString(variables[1]):
        value = variables[1].strip('"\'')
    elif isInt(variables[1]):
        value = int(variables[1])
    elif isFloat(variables[1]):
        value = float(variables[1])

    targetedList.append(value)

def removeElementInList(line: str, var: dict) -> None:

    """
        izmet pēdējo elementu no masīva  
    """

    # pārbauda vai rinda pinībā atbilst izmest() funkcijai
    match = fullmatch(r"izmest\s*\((.*)\)", line.strip())

    if match == None:
        return

    variable: list = getVariable(match.group(1).strip(), var)

    variable.pop()
