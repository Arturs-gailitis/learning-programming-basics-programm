from language.code_reader import readFile, getPrintedResult

from fastapi import FastAPI

def main() -> FastAPI:

    """
        programmas backend API avots
    """

    # izveido FastAPI objektu
    mainAPI = FastAPI()

    # ieliek /code pseudokoda printējamo rezultātu
    @mainAPI.post("/code")
    def postingSimpleCode() -> dict[str, list]:

        """
        ieliek FastAPI parasta koda printējamo rezultātu
        """

        readFile()
        result = getPrintedResult()

        return {
            "result": result
        }

    return mainAPI


mainAPI = main()