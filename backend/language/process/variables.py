from typing import Any

def variables(line: str, var: dict):

    """
    piefiksē kurš mainīgajam ir datu tips un to ieliek mainīgo dictionary
    """

    name = ''
    value = None

    characters = line.split()

    # pārbauda vai pirmais vārds atbilst mainīgajam
    if characters[0] == 'mainigais':
        name = characters[1]
        value = characters[3]

        # skatās kurš datu tips mainīgajam ir un ieliek to mainīgo sarakstā
        if isInt(value):
            var[name] = int(value)
        elif isFloat(value):
            var[name] = float(value)
        elif isList(line.split("=", 1)[1].strip()):
            var[name] = createList(line, var)
        elif isString(line):
            text_List = line.split("=", 1)
            text = ""

            # savieno visus string mainīgā vārdus 
            if (len(text_List) == 1):
                text = text_List[0]
            else:
                for word in text_List:
                    text = word + " "

            var[name] = text.strip('" ').strip('"')

        elif isBool(value):
            if value == "patiess":
                var[name] = True
            else:
                var[name] = False

        # pārbauda vai jaunā mainīgā vērtība tiek ņemta no masīva
        elif isListElement(value, var):
            var[name] = getListElement(value, var)

        # pārbauda vai jaunā mainīgā vērtība nav cits mainīgais
        elif isVariable(value, var):
            variableValue = getVariable(value, var)
            var[name] = variableValue
    
    else:

        name = characters[0]
        newValue = characters[2]
        oldValue = None
        variableNames = var.keys()

        # iegūst vecās vērtību no konkrētā mainīgā
        for v in variableNames:
            if name == v:
                oldValue = var[name]
                break

        # skatās vai tam kuram ieliks jauno vērtību, nav eksistējošs masīvs
        if isListElement(name, var):
            setListElement(name, newValue, var)
            return

        # skatās vai jaunā vērtība nebūs nākusi no eksistējoša masīva
        if isListElement(newValue, var):
            var[name] = getListElement(newValue, var)
            return
        
        # skatās vai jaunais mainīgais ir jau eksistējošā mainīgā nosaukums
        if isVariable(newValue, var):
            variableValue = getVariable(newValue, var)
            var[name] = variableValue
            return
        
        # skatās kurš datu tips ir vecajam mainīgajam un tad pārveido jauno vērtību lai būtu tāds pats datu tips
        if isinstance(oldValue, bool):

            if newValue == "patiess":
                var[name] = True
            elif newValue == "nepatiess":
                var[name] = False 
        
        elif isinstance(oldValue, int):
            var[name] = int(newValue)
        elif isinstance(oldValue, float):
            var[name] = float(newValue)
        elif isinstance(oldValue, str):

            text = line.split("=", 1)[1].strip()

            var[name] = text.strip('"')  

def isInt(variable: str) -> bool:

    """
    pārbauda vai mainīgais ir vesels skaitlis
    """

    try:

        dot = variable.find(".") == -1
        instance = isinstance(int(variable), int)
        quatation = variable.find('"') == -1

        if dot and instance and quatation:
            return True
        else:
            return False 
    
    except ValueError:
        return False
    
def isFloat(variable: str) -> bool:
    
    """
    pārbauda vai mainīgais ir daļskaitlis
    """

    try:

        dot = variable.find(".") != -1
        instance = isinstance(float(variable), float)
        quatation = variable.find('"') == -1

        if dot and instance and quatation:
            return True
        else:
            return False 
        
    except ValueError:
        return False

def isString(line: str) -> bool:

    """
    pārbauda vai mainīgais ir teksts
    """
        
    quatation = line.find('"') != -1

    if quatation:
        return True
    else:
        return False

def isBool(variable: str) -> bool:

    """
    pārbauda vai mainīgais ir true vai false
    """

    isTrue = variable == "patiess"
    isFalse = variable == "nepatiess"

    if isTrue or isFalse:
        return True
    else:
        return False

def isList(variable: str) -> bool:

    """
    pārbauda vai mainīgais ir masīvs
    """

    if variable.startswith("[") and variable.endswith("]"):
        return True
    else:
        return False
    
def isVariable(variable: str, var: dict) -> bool:

    """
    pārbauda vai ievietotā vērtība ir jau izveidotā mainīgā nosaukums
    """

    varNames = var.keys()

    for v in varNames:
        if variable == v:
            return True
    
    return False

def isListElement(variable: str, var: dict) -> bool:

    """
    pārbauda vai teksts norāda uz eksistējoša masīva elementu
    """

    if "[" not in variable and "]" not in variable:
        return False

    name = variable.split("[")[0]

    if name in var and isinstance(var[name], list):
        return True
    else:
        return False

       
def getVariable(variable: str, var: dict) -> Any:

    """
    iegūst cita mainīgā vērtību
    """

    return var[variable]

def createList(line: str, var: dict) -> list:

    """
    izveido jauno masīvu un ieliek tajā norādītās vērtības priekš šī masīva nodefinēšanas variables dictionary
    """

    listSection = line.split("=", 1)[1].strip()

    # atgriež tukšu masīvu, ja tajā nav nodefinētas vērtības
    if listSection == "[]":
        return []

    # dabū katru vērtību izlaižot cietās iekavas - []
    listElements = listSection[1:-1].split(",")

    results = []

    # iterē cauri katra masīva elementiem lai tos ieliktu jaunajā masīvā
    for elem in listElements:

        elem = elem.strip()

        if isListElement(elem, var):
        
            results.append(getListElement(elem, var))

        elif isVariable(elem, var):

            results.append(getVariable(elem, var))

        elif isBool(elem):

            if elem == "patiess":
                results.append(True)
            else:
                results.append(False)

        elif isString(elem):

            results.append(elem.strip('"'))

        elif isInt(elem):

            results.append(int(elem))

        elif isFloat(elem):

            results.append(float(elem))

    return results

def getListElement(variable: str, var: dict) -> Any:

    """
    paņem no iepriekš nodefinētā masīva konkrētu elementu, pēc tās indeksa
    """

    indexInText = ""
    index = 0

    listName = variable.split("[")[0]

    # iegūst iterēšanas sākuma un beigu robežas, lai atrastu indeksu
    findStartIndex = variable.find("[") + 1
    findEndIndex = variable.rfind("]")

    # iterē tik tālu lai varētu iegūt vajadzīgo indeksu
    for i in range(findStartIndex, findEndIndex):
        indexInText = indexInText + variable[i]

    # iegūst indeksa vērtību kā ciparu vai arī ņemot jau eksistējošu mainīgo
    try:
        index = int(indexInText)
    except ValueError:
        index = getVariable(indexInText, var)

    elements = getVariable(listName, var)

    return elements[index]

def setListElement(variable: str, value: str, var: dict) -> None:

    """
    ieliek iepriekš nodefinētajā masīvā konkrētā pozīcijā jaunu vērtību 
    """

    indexInText = ""
    index = 0

    listName = variable.split("[")[0]
    existingList = getVariable(listName, var)

    findStartIndex = variable.find("[") + 1
    findEndIndex = variable.rfind("]")
    
    for i in range(findStartIndex, findEndIndex):
        indexInText = indexInText + variable[i]
    
    try:
        index = int(indexInText)
    except ValueError:
        index = getVariable(indexInText, var)

    if isListElement(value, var):

        existingList[index] = getListElement(value, var)

    elif isVariable(value, var):

        existingList[index] = getVariable(value, var)

    elif isBool(value):

        if value == "patiess":
            existingList[index] = True
        else:
            existingList[index] = False

    elif isString(value):
        existingList[index] = value.strip('"')

    elif isInt(value):
        existingList[index] = int(value)

    elif isFloat(value):
        existingList[index] = float(value)
    