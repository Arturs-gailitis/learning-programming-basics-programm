from process.variables import isVariable, getVariable, isListElement, getListElement, isBool, isString, isInt, isFloat

from re import fullmatch, search
from typing import Any

def splitPrintParts(text: str) -> list[str]:

    """
        sagriež printēšanai ievadīto tekstu 
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

        # skatās vai + simbols nav saistīts ar sadalīšanu vai arī tas ir simbols priekš teksta
        if char == "+" and quoteStatuss == True:
            part = part + char
        elif char == "+" and quoteStatuss == False:
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
    textPieces = splitPrintParts(text)

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