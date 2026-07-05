from process.variables import variables
FILE_PATH = "temp/code.txt"
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

        # skatās atslēgvārdus
        match first_word:
            case "mainigais":
                variables(line, variable)