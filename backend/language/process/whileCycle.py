from shlex import split

from process.ifBlock import checkConditions

def checkWhileCondition(codeLine: list, startIndex: int, var: dict, mathOp: list, conditionOp: list) -> bool:

    """
        iegūst kamer bloka nosacījuma atbildi 
    """

    whileConditionLine = codeLine[startIndex]
    lineObjects = split(whileConditionLine, posix=False)

    # notīra no saraksta kamer un tad atslēgvārdus
    cleanLineObjects = lineObjects[1:-1]

    return checkConditions(cleanLineObjects, var, mathOp, conditionOp)
