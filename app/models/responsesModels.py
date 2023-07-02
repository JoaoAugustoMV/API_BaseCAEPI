from models.Erros import Erros
from models.CAsNaoEncontrados import CAsNaoEncontrados

from fastapi.responses import JSONResponse

class ResponsesModels():
    responsesInfoCA:dict = {
                200:{
                    "description": "Informações do CA"
                    },
                404:{
                    "model": Erros,
                    "description": "Erros na requisição",  
                    },
                }
    responsesExportar: dict = {
                200:{
                    "description": "Todos CA foram localizados",
                    "content": {"'application/vnd.      openxmlformats-officedocument.spreadsheetml.sheet": {}}
                    },
                400:{
                    "model": Erros,
                    "description": "listaCAs não pode ser vazia",  
                    },
                404:{
                    "model": CAsNaoEncontrados,
                    "description": "Um ou mais CA não foi localizados",  
                    },
                }
    
    responsesCANaoEncontrado = JSONResponse(status_code=404, content={
        "sucess": False,
        "erros": ["Numero Ca não encontrado!"]
        })
    
    responsesListaVazia = JSONResponse(status_code=404, content={
        "sucess": False,
        "erros": ["listaCAs não pode estar vazia"]
        })

    def responsesExportarCAsNaoEncontrado(self, listCAsNaoEncontrados):
        return JSONResponse(status_code=404, content={
        "sucess": False,
        "erros": {
            'CAsNaoEncontrados': listCAsNaoEncontrados
            }        
        })
