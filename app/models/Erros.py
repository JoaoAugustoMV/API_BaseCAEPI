from pydantic import BaseModel

class Erros(BaseModel):
    sucess: bool
    erros: list[str]