from shlex import split

from process.variables import variables
from process.math import math
from process.comparison import compare

FILE_PATH = "temp/code.txt"
MATH_OPERATORS = ["*", "/", "+", "-"]
COMPARISON_OPERATORS = ["un", "vai", "vienads", "nevienads", "lielaks", "mazaks", "vismaz", "neparsniedz"]

variable = {}

# atver latviskoto koda failu lasīšanas režīmā
with open(FILE_PATH, "r", encoding="utf-8") as file:
    
    # skatās katru rindu
    for line in file:

        # noskaidro vai rinda ir tukša vai nē
        if line.strip() == "":
            continue
        else:
            line = line.strip()

        # sagriež rindu pa gabaliem
        lineObjects = split(line, posix=False)

        hasMathSimbols = False
        hasComparisonSimbols = False

        # skatās vai konkrētajā līnijā ir iekļauti matemātikas vai salīdzināšanas operātori
        for l in lineObjects:

            if l in MATH_OPERATORS:
                hasMathSimbols = True

            if l in COMPARISON_OPERATORS:
                hasComparisonSimbols = True

            if hasComparisonSimbols == True and hasMathSimbols == True:
                break
        
        # ja abi ir iekļauti, tad sākumā izpilda matemātiku un samaina līniju un tad notiek salīdzināšana
        if hasMathSimbols == True and hasComparisonSimbols == True:

            changedLine = math(line, variable, MATH_OPERATORS, returnLine=True)
            compare(changedLine, variable, COMPARISON_OPERATORS)
            continue
        
        # ja ir tikai bijusi matemātikas operātori tad tikai izpilda matemātiku
        elif hasMathSimbols == True and hasComparisonSimbols == False:

            math(line, variable, MATH_OPERATORS)
            continue
        
        # ja ir tikai bijusi salīdzināšanas operātori tad tikai izpilda salīdzināšanu
        elif hasMathSimbols == False and hasComparisonSimbols == True:
            
            compare(line, variable, COMPARISON_OPERATORS)
            continue

        # iegūst visu saglabāto mainīgo nosaukumus
        varNames = variable.keys()

        # iegūst pirmo atslēgvārdu, ko analizēt
        first_word = lineObjects[0]
        
        # skatās vai būs jāmaina vecajiem mainīgajiem vērtības
        for v in varNames:

            if first_word == v and first_word != "mainigais":
                variables(line, variable)
                continue

        # skatās atslēgvārdus
        match first_word:
            case "mainigais":
                variables(line, variable)

print(variable)