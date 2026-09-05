from shlex import split

from process.ifBlock import checkConditions
from process.functions import getListSize

def checkWhileCondition(codeLine: list, startIndex: int, var: dict, mathOp: list, conditionOp: list) -> bool:

    """
        iegūst kamer bloka nosacījuma atbildi 
    """

    # iegūst nosacījuma rindu 
    # ja tajā ir iebūvētā masīva garuma funkcija tad sākumā iegūst to  
    whileConditionLine = getListSize(str(codeLine[startIndex]).strip(), var)

    lineObjects = split(whileConditionLine, posix=False)

    # notīra no saraksta kamer un tad atslēgvārdus
    cleanLineObjects = lineObjects[1:-1]

    return checkConditions(cleanLineObjects, var, mathOp, conditionOp)
