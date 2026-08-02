from shlex import split
from re import findall

from process.variables import variables
from process.math import math
from process.comparison import compare
from process.ifBlock import checkOperations, checkBlockStatuss, ifElseBlock, closeNotFinishedIfBlocks, getIfBlockInformation, removeLocalVariables
from process.forCycle import *

FILE_PATH = "temp/code.txt"
MATH_OPERATORS = ["*", "/", "+", "-"]
COMPARISON_OPERATORS = ["un", "vai", "vienads", "nevienads", "lielaks", "mazaks", "vismaz", "neparsniedz"]

variable = {}

def readCode(codeLines: list[str], cycleTime = 0, cycleStart = 0, cycleEnd = 0) -> None | str:

    """
    apstrādā latviskotā pseudokoda rindas
    """

    # skatās cik pašlaik ir atvērtas ja zari
    openedIfBlocks = len(getIfBlockInformation())

    index, endIndex = 0, 0

    # iegūst beidzamo indeksu skatoties vai to palaiž vienkārši visu kodu vai arī kā ciklu
    if cycleTime == 0:

        endIndex = len(codeLines)

    else :
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

        # sagriež rindu pa gabaliem
        lineObjects = split(line, posix=False)

        # sagriež beidzamo skaitli un kolu
        regexFind = findall(r'\d+|:', lineObjects[-1])

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

        # skatās vai nesākās cikls 
        if lineObjects[0] == "cikls" and ":" in regexFind:

            savedVariables = list(variable.keys())

            # iegūst vajadzīgo informāciju priekš cikla
            cycleEndIndex = findForCycleEnd(codeLines, index)
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

        # ja ciklā ir atrodami nakamais vai beidz atslēgvārdi, tad aizver ciet visus atvērtos ja zarus 
        if cycleTime > 0:
            if lineObjects[0] == "nakamais":
                closeNotFinishedIfBlocks(openedIfBlocks, variable)
                return "nakamais"
            elif lineObjects[0] == "beidz":
                closeNotFinishedIfBlocks(openedIfBlocks, variable)
                return "beidz" 
    
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
            
        if first_word == "mainigais" or first_word in variable:
            variables(line, variable)
            index = index + 1
            continue

def readFile() -> None:

    """
    nolasa visas koda rindas un aizsūta tās apstrādei
    """
        
    # atver latviskoto koda failu lasīšanas režīmā
    with open(FILE_PATH, "r", encoding="utf-8") as file:

        # izlasa visas rindas
        lines = file.readlines()

        readCode(lines)

readFile()

print(variable)