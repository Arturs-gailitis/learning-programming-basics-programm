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

        foundOperator = False

        # skatās vai rindā neatrodās matemātisks operātors
        for o in MATH_OPERATORS:
            for ob in lineObjects:

                if ob == o:
                    math(line, variable, MATH_OPERATORS)
                    foundOperator = True
                    break
            
            if foundOperator == False:
                continue

        if foundOperator == True:
            continue
        
        # skatās vai rindā neatrodās salīdzināšanas operātors
        for co in COMPARISON_OPERATORS:
            for ob in lineObjects:

                if ob == co:
                    compare(line, variable, COMPARISON_OPERATORS)
                    foundOperator = True
                    break
            
            if foundOperator == False:
                continue
        
        if foundOperator == True:
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