from shlex import split
from typing import Any

def compare(line: str, var: dict, operators: list[str], loops = False) -> None | bool:

    """
    apstrādā salīdzinājuma darbības un tos ieliek vecajos vai jaunajos mainīgajos vai arī if, for un while uzbūvēs
    """

    order = []

    result = None
    depth = 0

    line = line.replace("(", " ( ").replace(")", " ) ")

    # līdzīga metode kā parastā .split() tikai šeit nesagriež vērtības ja tās ir pēdiņās
    lineObjects = split(line, posix=False)
    
    # iziet cauri visiem salīdzināšanas operātoriem
    for o in operators:

        # iziet cauri konkrētajai rindai
        for position, ob in enumerate(lineObjects):

            # nosaka cik dziļi iekavās salīdzināšanas darbība būs
            if ob == "(":
                depth = depth + 1
                continue
            
            if ob == ")":
                depth = depth - 1
                continue
            
            if ob == o:

                # nosaka katras salīdzināšanas darbību prioritātes un ieliek kopējā sarakstā
                if ob == "vai":
                    priority = 0
                    order.append((depth, priority, position, o))
                    continue
                elif ob == "un":
                    priority = 1
                    order.append((depth, priority, position, o))
                    continue
                else:
                    priority = 2
                    order.append((depth, priority, position, o))
                    continue

    # sakārto salīdzināšanas darbības šādā secībā - iekavas, darbību prioritāte un atrašanās vieta
    order.sort(key=lambda item: (-item[0], -item[1], item[2]))

    # iziet cauri visām salīdzināšanas darbībām
    for depth, priority, position, operation in order:

        firstVariable = lineObjects[position - 1]
        secondVariable = lineObjects[position + 1]

        result = None

        # iegūst konkrēti vajadzīgās vērtības no mainīgajiem vai jau atrisinātajiem
        firstValue = getBoolValue(firstVariable, var)
        secondValue = getBoolValue(secondVariable, var)

        # skatās kura salīdzināšanas operātors ir jāizmanto
        match operation:
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
            
            nextDepth, nextPriority, nextPosition, nextOperation = order[index]

            # maina visiem pozīciju, atkarībā cik daudz tika izdzēsts 
            if nextPosition > position:

                if bracketsRemoved == True:
                    order[index] = (nextDepth, nextPriority, nextPosition - 4, nextOperation)
                else:
                    order[index] = (nextDepth, nextPriority, nextPosition - 2, nextOperation)
    
    # skatās vai šī funkcija netika izsaukta if/else, for un while ciklos
    if loops == False:

        name = lineObjects[0]

        # skatās vai ievieto vecajam mainīgajam jaunu vērtību vai arī ieliek jaunajam mainīgajam
        if name != "mainigais":

            var[name] = result
        
        else:

            var[lineObjects[1]] = result

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
    
    # pārbauda vai dotais mainīgais nav ievietots kā cipars
    if value.startswith('"') and value.endswith('"'):
        return value.strip('"')
    
    # skatās vai nevar pārveidot no teksta uz veselu ciparu vai daļskaitli
    try:
        return int(value)
    
    except ValueError:
        return float(value)