from pydantic import BaseModel

class RequestParaExportarJson(BaseModel):    
    listaCAs: list[str]