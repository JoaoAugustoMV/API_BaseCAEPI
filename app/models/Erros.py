from pydantic import BaseModel

class Erros(BaseModel):
    sucess: bool = False
    erros: list[str]