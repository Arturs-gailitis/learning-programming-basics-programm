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