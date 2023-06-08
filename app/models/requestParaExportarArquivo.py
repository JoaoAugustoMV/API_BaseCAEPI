from pydantic import BaseModel

class RequestParaExportarArquivo(BaseModel):
    nomeArquivo: str
    listaCAs: list[str]
    