def math(line: str, var: dict, operations: list, returnLine = False) -> None | str:

    """
    apstrādā matemātiskas darbības un ieliek tos vecajos vai jaunajos mainīgajos
    """

    mathOrder = []

    depth = 0
    priority = 0

    characters = line.replace("(", " ( ").replace(")", " ) ").split()

    # skatās vai tās nav matemātiskas darbības bet teksta savienošana
    if "+" in line:

        # iegūst darbības aiz = zīmes un pirms tā 
        action = line.split("=", 1)[1].split("+")
        firstPart = line.split("=", 1)[0].split()

        notConcatinationSimbols = False

        for a in action:
            
            # pārbauda vai ir atsevišķi simboli, kuri neatiecās uz teksta savienošanu
            if a == "-" or a == "*" or a == "/":

                notConcatinationSimbols = True
            
            if notConcatinationSimbols == False:

                # Pārbauda vai šajā darbībā ir vienkārš string teksts, vai arī mainīgais kuram vērtība ir string
                if '"' in line or (a in var and isinstance(var[a], str)):
                    
                    concatination(firstPart, action, var)
                    return

    for position, c in enumerate(characters):

        # ja atrod iekavas vaļā tad palielina iekavu dziļumu
        if c == "(":
            depth = depth + 1
            continue

        # ja atrod iekavas ciet tad samazina iekavu dziļumu
        if c == ")":
            depth = depth - 1
            continue

        # ja atrod reizināšanas vai dalīšanas simbolus, tad ieliek iekšā secību sarakstā informāciju par šo darbību
        # papildus arī norādot ka pirmie izteiksmē būs jādara
        if c == "*" or c == "/":
            priority = 1

            mathOrder.append([depth, priority, position, c])
            continue

        # ja atrod saskaitīšanas vai atņemšanas simbolus, tad ieliek iekšā secību sarakstā informāciju par šo darbību
        # papildus arī norādot ka pēdējie izteiksmē būs jādara
        if c == "+" or c == "-":
            priority = 0

            mathOrder.append([depth, priority, position, c])
            continue
    
    # sakārto matemātisko secību šādā secībā - iekavas, matemātisko darbību prioritāte un atrašanās vieta
    mathOrder.sort(key=lambda item: (-item[0], -item[1], item[2]))

    # iziet cauri visām matemātikas darbībām
    for depth, priority, position, operation in mathOrder:

        first_variable = characters[position - 1]
        second_variable = characters[position + 1]

        # skatās kura matemātiskā darbība ir jādara
        match operation:
            case "*":
                multiplication(first_variable, second_variable, var, position, characters)
            case "/":
                division(first_variable, second_variable, var, position, characters)
            case "+":
                addition(first_variable, second_variable, var, position, characters)
            case "-":
                subtraction(first_variable, second_variable, var, position, characters)

        brackets_removed = False

        # skatās vai par kreisi vēl atrodās elementi un vai pozīcija ir vēl saraksta robežās
        if position - 2 >= 0 and position < len(characters):

            # pārbauda vai rezultāts neatrodas starp iekavām
            if characters[position - 2] == "(" and characters[position] == ")":

                # izdzēs iekavas
                del characters[position]
                del characters[position - 2]

                brackets_removed = True

        for index in range(len(mathOrder)):

            nextDepth, nextPriority, nextPosition, nextOperation = mathOrder[index]

            # maina visiem pozīciju, atkarībā cik daudz tika izdzēsts 
            if nextPosition > position:

                if brackets_removed == True:
                    mathOrder[index] = (nextDepth, nextPriority, nextPosition - 4, nextOperation)
                else:
                    mathOrder[index] = (nextDepth, nextPriority, nextPosition - 2, nextOperation)

    name = characters[0]

    # skatās vai vajag izdot izmainītu rindu
    if returnLine == True:
        changedLineList = []
        changedLine = ""

        for c in characters:
            changedLineList.append(str(c))

        # notiek visu elementu savienošana vienā string vērtībā, kas attēlo izmainīto rindu
        changedLine = " ".join(changedLineList)
        
        return changedLine
    
    # skatās vai ievieto vecajam mainīgajam jaunu vērtību vai arī jaunajam mainīgajam
    if name != "mainigais":

        var[name] = characters[2]
    
    else:

        var[characters[1]] = characters[3]


def multiplication(first: str, second: str, var: dict, position: int, characters: list):

    """
    izreiķina konkrētos skaitļus izmantojot reizināšanu
    """

    first_value = get_value(first, var)
    second_value = get_value(second, var)

    result = first_value * second_value

    del characters[position - 1: position + 2]

    characters.insert(position - 1, result)

def division(first: str, second: str, var: dict, position: int, characters: list):

    """
    izreiķina konkrētos skaitļus izmantojot dalīšanu
    """

    first_value = get_value(first, var)
    second_value = get_value(second, var)

    result = first_value / second_value

    del characters[position - 1: position + 2]

    characters.insert(position - 1, result)

def addition(first: str, second: str, var: dict, position: int, characters: list):

    """
    izreiķina konkrētos skaitļus izmantojot saskaitīšanu
    """
  
    first_value = get_value(first, var)
    second_value = get_value(second, var)

    result = first_value + second_value

    del characters[position - 1: position + 2]

    characters.insert(position - 1, result)

def subtraction(first: str, second: str, var: dict, position: int, characters: list):

    """
    izreiķina konkrētos skaitļus izmantojot atņemšanu
    """
  
    first_value = get_value(first, var)
    second_value = get_value(second, var)

    result = first_value - second_value

    del characters[position - 1: position + 2]

    characters.insert(position - 1, result)   
    

def get_value(variable: str, var: dict) -> int | float:

    """
    noskaidro vai dotā vērtība nav cipars, jau saglabātais mainīgais vai tekstā uzrakstīts cipars
    """

    # pārbauda vai dotais mainīgais nav ievietots kā cipars
    if isinstance(variable, int) or isinstance(variable, float):
        return variable

    # iegūst saglabāto mainīgā vērtību
    if variable in var:
        return var[variable]

    # skatās vai nevar pārveidot no teksta uz veselu ciparu vai daļskaitli
    try:

        return int(variable)
        
    except ValueError:
        return float(variable)

def concatination(firstPart: list, action: list[str], var: dict):

    """
    savieno string vērtības vienā vērtībā, jeb notiek string concatination
    """

    result = ""

    for a in action:

        a = a.strip()

        # pārbauda vai fragments ir vērtības nosaukums
        if a in var:
            result = result + var[a]
        
        # pārbauda vai fragments ir teksts
        if '"' in a:
            result = result + a.replace('"', "")
        
    first = firstPart[0]
    
    # skatās vai ievieto vecajam mainīgajam jaunu vērtību vai arī ieliek jaunajam mainīgajam
    if first != "mainigais":

        var[first] = result
    
    else:

        var[firstPart[1]] = result