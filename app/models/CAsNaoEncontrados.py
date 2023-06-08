from pydantic import BaseModel

class CAsNaoEncontrados(BaseModel):
    sucess = False
    CAsNaoEncontrados: list[str]