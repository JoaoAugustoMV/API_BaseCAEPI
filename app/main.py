from fastapi import Depends, FastAPI
import uvicorn
from routers import certificadoApovacao

tag_ca = [
    {
        "name": "Certificado de Aprovação",
        "description": "Consultas e Operações da BaseCAEPI"        
    }
]
app = FastAPI( 
    title="API BaseCAEPI",
    description="""Pesquisar e recuperar informações(por json ou arquivo de excel) sobre os certificados de aprovação emitidos para EPIs.\n
    Codigo fonte: https://github.com/JoaoAugustoMV/API_BaseCAEPI
        """,
        openapi_tags=tag_ca
    )



app.include_router(certificadoApovacao.router)

@app.get("/", tags=["HOME"])
async def index():
    return "HOME"

if __name__ == "__main__":
    uvicorn.run(app)