from process.variables import variables
from process.math import math

FILE_PATH = "temp/code.txt"
MATH_OPERATORS = ["*", "/", "+", "-"]

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

        # iegūst pirmo atslēgvārdu, ko analizēt
        first_word = line.split()[0]

        if "+" in line or "-" in line or "*" in line or "/" in line:
            math(line, variable, MATH_OPERATORS)
            continue

        # iegūst visu saglabāto mainīgo nosaukumus
        varNames = variable.keys()
        
        # skatās vai būs jāmaina vecajiem mainīgajiem vērtības
        for v in varNames:
            char = line.split()
            if first_word == v and first_word != "mainigais":
                variables(line, variable)
                continue

        # skatās atslēgvārdus
        match first_word:
            case "mainigais":
                variables(line, variable)

print(variable)