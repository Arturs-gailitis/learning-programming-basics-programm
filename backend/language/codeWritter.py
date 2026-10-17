from language.code_reader import getCodeFilePath

def writeCode(code: str) -> None:
    """
    Ieraksta no frontend saņemto kodu txt failā.
    """

    filePath = getCodeFilePath("realCode.txt")

    with open(filePath, "w", encoding="utf-8") as file:
        file.write(code)

def deleteCode() -> None:
    """
        Izdzēš frontend saņemto kodu.
    """

    filePath = getCodeFilePath("realCode.txt")

    with open(filePath, "w", encoding="utf-8") as file:
        file.write("")