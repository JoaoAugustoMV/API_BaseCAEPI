from models.Erros import Erros
from models.CAsNaoEncontrados import CAsNaoEncontrados


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
