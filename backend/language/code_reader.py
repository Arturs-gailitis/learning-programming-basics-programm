from shlex import split
from re import findall
from typing import Any
from pathlib import Path

from process.variables import variables, isListElement
from process.math import math
from process.comparison import compare
from process.ifBlock import checkOperations, checkBlockStatuss, ifElseBlock, closeNotFinishedIfBlocks, getIfBlockInformation, removeLocalVariables
from process.createdFunctions import createFunction, startingFunction
from process.functions import printing, getListSize, addElementInList, removeElementInList
from process.forCycle import *
from process.whileCycle import *

MATH_OPERATORS = ["*", "/", "+", "-", "atlikums"]
COMPARISON_OPERATORS = ["un", "vai", "vienads", "nevienads", "lielaks", "mazaks", "vismaz", "neparsniedz"]

variable = {}
functions = []
printedResult = []

def readCode(codeLines: list[str], cycleTime = 0, cycleStart = 0, cycleEnd = 0, special = False) -> None | str | tuple [str, Any]:

    """
    apstrādā latviskotā pseudokoda rindas
    """

    # skatās cik pašlaik ir atvērtas ja zari
    openedIfBlocks = len(getIfBlockInformation())

    index, endIndex = 0, 0

    # iegūst beidzamo indeksu skatoties vai to palaiž vienkārši visu kodu vai arī kā ciklu
    if cycleTime == 0 and special == False:

        endIndex = len(codeLines)

    elif cycleTime > 0 or special == True :
        index = cycleStart
        endIndex = cycleEnd

    # iterē cauri dotajām koda rindām
    while index < endIndex:

        line = codeLines[index]

        # noskaidro vai rinda ir tukša vai nē
        if line.strip() == "":
            index = index + 1
            continue
        else:
            line = line.strip()

        # aiztāj koda rindā vietā kur izmanto iebūvēto masīva izmēra funkciju ar izvēlētā masīva izmēru
        line = getListSize(line, variable)

        # skatās vai ir izmantota iebūvētā printēšanas funkcija
        if line.startswith("printet("):
            # tiek izveidots printēšanas teksts skatoties vai konkrētais kod bloks ir izmantojams
            if checkBlockStatuss():
                printing(line, variable, printedResult)

            index = index + 1
            continue

        # skatās vai sākas ja, citādi ja, citādi vai beigas
        ifBlockLine = ifElseBlock(line, variable, MATH_OPERATORS, COMPARISON_OPERATORS)
            
        # skatās ja tas ir ja, citādi ja, citādi vai beigas
        if ifBlockLine == True:
            index = index + 1
            continue
            
        ifBlockActive = checkBlockStatuss()
                    
        # nostrādā ja konkrētais bloks ir atzīmēts, ka to nelasa jo nosacījums neatbilst
        if ifBlockActive == False:
            index = index + 1
            continue

        # skatās vai ir izmantota iebūvētā elementu ielikšana masīvā funkcija
        if line.startswith("ielikt"):
            addElementInList(line, variable)
            index = index + 1
            continue

        # skatās vai ir izmantota iebūvētā pēdējo elementu noņemšana no masīva funkcija
        if line.startswith("izmest"):
            removeElementInList(line, variable)
            index = index + 1
            continue

        # sagriež rindu pa gabaliem
        lineObjects = split(line, posix=False)

        # sagriež beidzamo skaitli un kolu
        regexFind = findall(r'\d+|:', lineObjects[-1])

        # skatās vai nesākās cikls 
        if lineObjects[0] == "cikls" and ":" in regexFind:

            savedVariables = list(variable.keys())

            # iegūst vajadzīgo informāciju priekš cikla
            cycleEndIndex = findCycleEnd(codeLines, index)
            startValue, forCycleTime = findForCycleRepeatTime(line, variable)

            # iterē vairākas reizes cauri konkrētajam teksta diapazonam
            for cycleTime in range(forCycleTime):

                iterationValue = startValue + cycleTime

                # iegūst iterēšanas mainīgo
                getIteration(lineObjects, variable, iterationValue)

                # ja neizdod nakamais un beidz, tad no jauna konkrētajā diapazonā iterē latviskotu kodu
                keyword = readCode(codeLines, cycleTime=forCycleTime, cycleStart=index + 1, cycleEnd=cycleEndIndex)

                if keyword == "nakamais":
                    continue
                elif keyword == "beidz":
                    break

            # izdzēš iterācijas mainīgo kad beidzās cikls
            iteration = getIteration(lineObjects, variable, value=True)
            variable.pop(iteration)

            # izdzēš ciklā izveidotos mainīgos
            removeLocalVariables(variable, savedVariables)

            # turpina lasīt tajā vietā, kur beidzās cikls
            index = cycleEndIndex + 1
            continue

        # skatās vai nesākās kamer cikls
        if lineObjects[0] == "kamer" and lineObjects[-1] == "tad":

            whileSavedVariables = list(variable.keys())

            # iegūst vajadzīgo informāciju par cikla izmēriem
            startLoopIndex = index
            endLoopIndex = findCycleEnd(codeLines, startLoopIndex)

            while True:

                # skatās vai kamer nosacījums ir patiess, ja nav tad beidz kamer ciklu
                if checkWhileCondition(codeLines, startLoopIndex, variable, MATH_OPERATORS, COMPARISON_OPERATORS) == False:
                    break

                # iterē cauri kamer cikla bloku
                keyword = readCode(codeLines, cycleStart=startLoopIndex + 1, cycleEnd=endLoopIndex, special=True)
                
                if keyword == "nakamais":
                    continue
                elif keyword == "beidz":
                    break

            removeLocalVariables(variable, whileSavedVariables)

            index = endLoopIndex + 1
            continue

        functionName = ""

        if "(" in line:
        
            for obj in lineObjects:

                # izņem no funkciju nosaukuma iekavu
                object = obj.split("(")[0]

                # pārbauda vai iepriekš tika izveidota funkcija ar tādu nosaukumu
                if any(object == name["functionName"] for name in functions):
                    functionName = object
                    break

        # ja atrada funkcijas nosaukumu
        if functionName != "":

            functionSavedVariables = list(variable.keys())

            # iegūst nepieciešamo info par funkciju, piemēram sākuma un beigu indeksu un 
            # vai šī funkcija atgriezīs vērtību
            start, end, functionReturn = startingFunction(functionName, functions, line, MATH_OPERATORS, variable)

            keyword, result = None, None

            if functionReturn == True:
                keyword, result = readCode(codeLines, cycleStart=start, cycleEnd=end, special=True)
            else:
                readCode(codeLines, cycleStart=start, cycleEnd=end, special=True)

            removeLocalVariables(variable, functionSavedVariables)

            # pārbauda vai bija atgriezt atslēgvārds un rezultāts
            if keyword == "atgriezt" and result != None:

                if "=" in lineObjects:

                    # ieliek jaunajam vai vecajam mainīgajam vērtību kuru funkcija atgrieza 
                    if lineObjects[0] == "mainigais":
                        variable[lineObjects[1]] = result
                    else:
                        variable[lineObjects[0]] = result

            index = index + 1
            continue

        # ja blokā ir atrodami nakamais, beidz un atgriezt atslēgvārdi, tad aizver ciet visus atvērtos ja zarus 
        if cycleTime > 0 or special == True:
            if lineObjects[0] == "nakamais":
                closeNotFinishedIfBlocks(openedIfBlocks, variable)
                return "nakamais"
            elif lineObjects[0] == "beidz":
                closeNotFinishedIfBlocks(openedIfBlocks, variable)
                return "beidz"
            elif lineObjects[0] == "atgriezt":
                closeNotFinishedIfBlocks(openedIfBlocks, variable)

                # atgriež tikai atslēgvārdu, ja funkcija neko neatgriež atpakaļ
                if len(lineObjects) == 1:
                    return "atgriezt", None

                returnValue = lineObjects[1]

                # atgriež atslēgvārdu un pareizu vērtību, ja funkcija atgriež atpakaļ vērtību
                if returnValue in variable:
                    return "atgriezt", variable[returnValue]
                elif returnValue == "patiess":
                    return "atgriezt", True
                elif returnValue == "nepatiess":
                    return "atgriezt", False
                elif returnValue.startswith('"'):
                    return "atgriezt", str(returnValue)

                try:
                    return "atgriezt", int(returnValue)
                except ValueError:
                    return "atgriezt", float(returnValue)
    
        hasMathSimbols, hasComparisonSimbols = checkOperations(lineObjects, MATH_OPERATORS, COMPARISON_OPERATORS)
            
        # ja abi ir iekļauti, tad sākumā izpilda matemātiku un samaina līniju un tad notiek salīdzināšana
        if hasMathSimbols == True and hasComparisonSimbols == True:
    
            changedLine = math(line, variable, returnLine=True)
            compare(changedLine, variable, COMPARISON_OPERATORS)
            index = index + 1
            continue
            
        # ja ir tikai bijusi matemātikas operātori tad tikai izpilda matemātiku
        elif hasMathSimbols == True and hasComparisonSimbols == False:
    
            math(line, variable)
            index = index + 1
            continue
            
        # ja ir tikai bijusi salīdzināšanas operātori tad tikai izpilda salīdzināšanu
        elif hasMathSimbols == False and hasComparisonSimbols == True:
                
            compare(line, variable, COMPARISON_OPERATORS)
            index = index + 1
            continue
    
        # iegūst pirmo atslēgvārdu, ko analizēt
        first_word = lineObjects[0]
            
        if first_word == "mainigais" or first_word in variable or isListElement(first_word, variable):
            variables(line, variable)
            index = index + 1
            continue
        elif first_word == "funkcija" or (first_word == "atgriezta" and lineObjects[1] == "funkcija"):
            # izveido jaunas funkcijas ierakstu
            functionEnd = createFunction(functions, line, codeLines, index)
            index = functionEnd + 1
            continue

def readFile() -> None:

    """
    nolasa visas koda rindas un aizsūta tās apstrādei
    """

    # iegūst code.txt faila ceļu
    FILEPATH = getCodeFilePath()

    # izdzēš mainīgo, funkciju un printējamā rezultāta informāciju, lai nebūtu problēmas atkārtori lasot code.txt
    variable.clear()
    functions.clear()
    printedResult.clear()
        
    # atver latviskoto koda failu lasīšanas režīmā
    with open(FILEPATH, "r", encoding="utf-8") as file:

        # izlasa visas rindas
        lines = file.readlines()

        readCode(lines)

def getPrintedResult() -> list:

    """
        var iegūt globālo printējamo rezultātu
    """
    return printedResult

def getCodeFilePath() -> Path:

    """
        iegūst code.txt faila atrašanās ceļu
    """
    # no konkrētā code_reader.py faila iegūst absalūto ceļu pirms /backend
    fileMap = Path(__file__).resolve().parent.parent.parent

    # ieliek absalūtā ceļā temp/code.txt 
    file = fileMap / "temp" / "code.txt"

    return file

# priekš testēšanas
if __name__ == "__main__":
    readFile()

    print(variable)
    print("")
    print(functions)
    print()
    print(printedResult)