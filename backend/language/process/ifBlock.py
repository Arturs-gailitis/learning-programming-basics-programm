from shlex import split

from process.comparison import compare, getBoolValue
from process.math import math

ifBlocks = []

def checkOperations(line: list, mathOp: list, conditionOp: list) -> bool:
    """
    skatās vai konkrētajā līnijā priekš koda blokiem ir iekļauti matemātikas vai salīdzināšanas operātori 
    """

    hasMathSimbols = False
    hasComparisonSimbols = False

    for l in line:

        if l in mathOp:
            hasMathSimbols = True

        if l in conditionOp:
            hasComparisonSimbols = True

        if hasComparisonSimbols == True and hasMathSimbols == True:
            break
    
    return hasMathSimbols, hasComparisonSimbols

def checkConditions(lineObjects: list, var: dict, mathOp: list, conditionOp: list) -> bool:

    """
    pārbauda vai nosacījumi ir patiesi vai nepatiesi 
    """

    hasMath, hasComparison = checkOperations(lineObjects, mathOp, conditionOp)

    line = ""

    for l in lineObjects:

        line = line + " " + l

    # ja matemātika un salīdzināšana ir iekļauta, tad sākumā izpilda matemātiku un samaina līniju un 
    # tad notiek salīdzināšana
    if hasMath == True and hasComparison == True:
        changedLine = math(line, var, mathOp, returnLine=True)
        result = compare(changedLine, var, conditionOp, loops=True)
        return result
    
    # ja ir tikai bijusi salīdzināšanas operātori tad tikai izpilda salīdzināšanu
    elif hasMath == False and hasComparison == True:
        result = compare(line, var, conditionOp, loops=True)
        return result 
    
    # nostrādās ja nosacījumā ir tikai viena vērtība
    elif len(line) <= 2:

        result = getBoolValue(line[1], var)

        if isinstance(result, bool):
            return result

def ifElseBlock(line: str, var: dict, mathOp: list, conditionOp: list) -> bool:

    """
    pārbauda vai rinda ir saistīta ar ja, citādi ja, citādi un beigas atslēgvārdiem
    un nosaka vai nolasīs konkrēto rindu
    """

    condition = []

    parentActive = False
    conditionResult = False

    ifLine = line

    # izdzēš rindas beigās tad atslēgvārdu 
    if ifLine.endswith("tad"):
        ifLine = ifLine[:-3].strip()

    lineObjects = split(ifLine, posix=False)

    # nostrādās ja sākās ja bloks
    if lineObjects[0] == "ja":

        condition = lineObjects[1:]

        # iegūst informāciju, ka šo bloku atļauts ir lasīt
        if len(ifBlocks) == 0:
            parentActive = True
        else:
            parentActive = ifBlocks[-1]["currentActive"]

        if parentActive == True:

            conditionResult = checkConditions(condition, var, mathOp, conditionOp)
        
        # izveido ierakstu par vienu ja-citadi_ja-citadi bloku
        # parentActive - skatās vai pašu ja-citadi_ja-citadi zaru vajag lasīt un izpildīt 
        # branchExecuted - nosaka vai konkrētais nosacījums atbilst
        # currentActive - nosaka ka konkrēto bloku var izpildīt
        # elseStatement - strādā tikai tad kad citās konkrētajā zara blokos nosacījums neatbilst 
        ifBlocks.append({
            "parentActive": parentActive,
            "branchExecuted": conditionResult,
            "currentActive": parentActive and conditionResult,
            "elseStatement": False
        })

        return True

    # nostrādās ja sākās citadi ja bloks
    elif lineObjects[0] == "citadi" and len(lineObjects) > 1 and lineObjects[1] == "ja":

        condition = lineObjects[2:]

        currentIfBlock = ifBlocks[-1]

        boolStatement = currentIfBlock["parentActive"] == True and currentIfBlock["currentActive"] == False

        # skatās vai iepriekšējais bloks šajā zarā tika izpildīts vai nē 
        if currentIfBlock["parentActive"] == False or currentIfBlock["branchExecuted"] == True:
            currentIfBlock["currentActive"] = False
        
        elif currentIfBlock["branchExecuted"] == False and boolStatement == True:

            conditionResult = checkConditions(condition, var, mathOp, conditionOp)

            if conditionResult == True:

               currentIfBlock["currentActive"] = True
               currentIfBlock["branchExecuted"] = True 

        return True
    
    # nostrādās ja sākās citadi bloks
    elif lineObjects[0] == "citadi":

        currentIfBlock = ifBlocks[-1]

        boolStatement = currentIfBlock["branchExecuted"] == False and currentIfBlock["parentActive"] == True

        # šo bloku izmantos ja citos blokos šajā zarā neizpildijās nosacījumi
        currentIfBlock["currentActive"] = boolStatement

        currentIfBlock["branchExecuted"] = True
        currentIfBlock["elseStatement"] = True

        return True

    # izpildās, kad beidzās ja-citadi_ja-citadi zars
    elif lineObjects[0] == "beigas":

        # izdzēš jaunāko zara informāciju
        ifBlocks.pop()

        return True
    
    return False


def checkBlockStatuss() -> bool:

    """
    skatās vai rindu vai ja-citadi_ja-citadi zaru tiks nolasīts un izpildīts
    """
    # ja nav iekšā ja-citadi_ja-citadi zarā tad var turpināt tālāk skatīties rindu 
    if len(ifBlocks) == 0:
        return True

    return ifBlocks[-1]["currentActive"]
