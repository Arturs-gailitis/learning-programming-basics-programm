from shlex import split
from typing import Any

def compare(line: str, var: dict, operators: list[str], loops = False) -> None | bool:

    """
    apstrādā salīdzinājuma darbības un tos ieliek vecajos vai jaunajos mainīgajos vai arī if, for un while uzbūvēs
    """

    brackets, noBrackets, order, = [], [], [],
    result = None

    line = line.replace("(", " ( ").replace(")", " ) ")

    # līdzīga metode kā parastā .split() tikai šeit nesagriež vērtības ja tās ir pēdiņās
    lineObjects = split(line, posix=False)
    
    # iziet cauri visiem salīdzināšanas operātoriem
    for o in operators:

        isBracket = False

        # iziet cauri konkrētajai rindai
        for position, ob in enumerate(lineObjects):

            # piefiksē vai nav iekavas sākušās vai beigušās
            if ob == "(":
                isBracket = True
            
            if ob == ")":
                isBracket = False
            
            if ob == o:

                # ieliek masīvos visas iespējamās salīdzināšanas darbības, skatoties vai tās atrodās iekavās vai nē
                if isBracket == True:
                    brackets.append((o, position))
                else:
                    noBrackets.append((o, position))

    # sakārto salīdzināšanas darbības pēc to pozīcijas rindā un pēc tam apvieno kopā
    brackets.sort(key= lambda item: item[1])
    noBrackets.sort(key= lambda item: item[1])

    order = brackets + noBrackets

    # iziet cauri visām salīdzināšanas darbībām
    for operator, position in order:

        firstVariable = lineObjects[position - 1]
        secondVariable = lineObjects[position + 1]

        result = None

        # iegūst konkrēti vajadzīgās vērtības no mainīgajiem vai jau atrisinātajiem
        firstValue = getBoolValue(firstVariable, var)
        secondValue = getBoolValue(secondVariable, var)

        # skatās kura salīdzināšanas operātors ir jāizmanto
        match operator:
            case "un":
                result = logicalAnd(firstValue, secondValue)
            case "vai":
                result = logicalOr(firstValue, secondValue)
            case "vienads":
                result = equal(firstValue, secondValue)
            case "nevienads":
                result = notEqual(firstValue, secondValue)
            case "lielaks":
                result = bigger(firstValue, secondValue)
            case "mazaks":
                result = smaller(firstValue, secondValue)
            case "vismaz":
                result = biggerOrEqual(firstValue, secondValue)
            case "neparsniedz":
                result = smallerOrEqual(firstValue, secondValue)

        bracketsRemoved = False

        # skatās vai par kreisi un pa labi ir vēl saraksta robežās
        if position - 2 >= 0 and position + 2 < len(lineObjects):

            # pārbauda vai salīdzināšanas darbība ir iekavās
            if lineObjects[position - 2] == "(" and lineObjects[position + 2] == ")":

                # izdzēs visu iekavās glabātās vērtības
                del lineObjects[position - 2: position + 3]

                # ieliek izdzēstajā vietā jaunu vērtību
                lineObjects.insert(position - 2, result)

                bracketsRemoved = True
        
        # skatās vai salīdzināšana notika iekavās
        if bracketsRemoved == False:

            del lineObjects[position - 1: position + 2]

            lineObjects.insert(position - 1, result)

        # iziet cauri visām saglabātajām operātoriem
        for index in range(len(order)):
            
            nextOperation, nextPosition = order[index]

            # maina visiem pozīciju, atkarībā cik daudz tika izdzēsts 
            if nextPosition > position:

                if bracketsRemoved == True:
                    order[index] = (nextOperation, nextPosition - 4)
                else:
                    order[index] = (nextOperation, nextPosition - 2)
    
    # skatās vai šī funkcija netika izsaukta if/else, for un while ciklos
    if loops == False:

        name = lineObjects[0]

        # skatās vai ievieto vecajam mainīgajam jaunu vērtību vai arī ieliek jaunajam mainīgajam
        if name != "mainigais":

            var[name] = lineObjects[2]
        
        else:

            var[lineObjects[1]] = lineObjects[3]

    else:

        return result


def logicalAnd(first: bool, second: bool) -> bool:

    """
    salīdzina divas vērtības ar and salīdzināšanas operātoru
    """

    return first and second

def logicalOr(first: bool, second: bool) -> bool:

    """
    salīdzina divas vērtības ar or salīdzināšanas operātoru
    """

    return first or second

def equal(first: Any, second: Any) -> bool:

    """
    salīdzina divas vērtības ar == salīdzināšanas operātoru
    """

    return first == second

def notEqual(first: Any, second: Any) -> bool:

    """
    salīdzina divas vērtības ar != salīdzināšanas operātoru
    """

    return first != second

def bigger(first: Any, second: Any) -> bool:

    """
    salīdzina divas vērtības ar > salīdzināšanas operātoru
    """

    return first > second

def smaller(first: Any, second: Any) -> bool:

    """
    salīdzina divas vērtības ar < salīdzināšanas operātoru
    """

    return first < second

def biggerOrEqual(first: Any, second: Any) -> bool:

    """
    salīdzina divas vērtības ar >= salīdzināšanas operātoru
    """

    return first >= second

def smallerOrEqual(first: Any, second: Any) -> bool:

    """
    salīdzina divas vērtības ar <= salīdzināšanas operātoru
    """

    return first <= second

def getBoolValue(value: Any, var: dict) -> bool | int | float:

    """
    iegūst konkrētās vērtības priekš salīdzināšanas
    """

    # pārbauda vai dotais mainīgais nav ievietots kā boolean vai cipars
    if isinstance(value, bool) or isinstance(value, int) or isinstance(value, float):
        return value

    # iegūst vērtību no iepriekš izveidotajiem mainīgajiem
    if value in var:
        return var[value]

    # pārveido kodā uzrakstīto true vai false
    if value == "patiess":
        return True
    elif value == "nepatiess":
        return False
    
    # skatās vai nevar pārveidot no teksta uz veselu ciparu vai daļskaitli
    try:
        return int(value)
    
    except ValueError:
        return float(value)