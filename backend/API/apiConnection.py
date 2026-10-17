from language.code_reader import readFile, getPrintedResult
from language.codeWritter import writeCode, deleteCode

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# klase kas nosaka kādu atbildi ir jāsaņem no frontend
class RequestedCode(BaseModel):
    text: str


def main() -> FastAPI:

    """
        programmas backend API avots
    """

    # izveido FastAPI objektu
    mainAPI = FastAPI()

    # lai sazinātos ar frontend ir nepieciešama atļauja
    mainAPI.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

    # saņem no frontend parastā redaktora kodu un aizsūta atpakaļ pseudokoda printējamo rezultātu
    @mainAPI.post("/code")
    def gettingSimpleCode(request: RequestedCode) -> dict[str, list]:

        """
            izpilda, kad frontend veic post HTTP vaicājumu no /code adresses
        """

        # iegūst saņemto codu un ieraksta pagaidu txt failā
        code = request.text
        writeCode(code)

        readFile()

        result = getPrintedResult()

        deleteCode()

        return {
            "result": result
        }

    return mainAPI


mainAPI = main()