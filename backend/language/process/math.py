def math(line: str, var: dict, operations: list):

    """
    apstrādā matemātiskas darbības un ieliek tos vecajos vai jaunajos mainīgajos
    """

    first_priority, second_priority, bracket_first, bracket_second = [], [], [], []

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

    # iziet cauri visiem matemātiskajiem operātoriem
    for o in operations:

        in_brackets = False

        # iziet cauri konkrētajai rindai
        for position, ch in enumerate(characters):

            # piefiksē vai nav iekavas sākušās vai beigušās
            if ch == "(":
                in_brackets = True

            elif ch == ")":
                in_brackets = False

            elif ch == o:
                
                # ieliek masīvā visas iespējamās matemātiskās darbības, skatoties vai tās atrodās iekavās
                if in_brackets == True:

                    # tā kā reizināšana un dalīšana ir pirmā tad tās tiek ieliktas atsevišķā masīvā
                    if ch == "*" or ch == "/":
                        bracket_first.append((o, position))
                    else:
                        bracket_second.append((o, position))

                else:

                    if ch == "*" or ch == "/":
                        first_priority.append((o, position))
                    else:
                        second_priority.append((o, position))

    # sakārto matemātiskas darbības pēc to pozīcijas rindā un pēc tam apvieno kopā
    bracket_first.sort(key= lambda item: item[1])
    bracket_second.sort(key= lambda item: item[1])
    first_priority.sort(key= lambda item: item[1])
    second_priority.sort(key= lambda item: item[1])

    order = bracket_first + bracket_second + first_priority + second_priority

    # iziet cauri visām matemātikas darbībām
    for operation, position in order:

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

        for index in range(len(order)):
            next_operation, next_position = order[index]

            # maina visiem pozīciju, atkarībā cik daudz tika izdzēsts 
            if next_position > position:

                if brackets_removed == True:
                    order[index] = (next_operation, next_position - 4)
                else:
                    order[index] = (next_operation, next_position - 2)

    name = characters[0]
    
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