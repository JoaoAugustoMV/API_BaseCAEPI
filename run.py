from flask import Flask
from flask_restx import Api
import os
from app.Services.CAService import CAService;
from app.Controllers.CAController import api as caController

app = Flask(__name__)
app.config['ERROR_404_HELP'] = False # Não exibir mensagem de erro padrões da lib
app.config.SWAGGER_UI_DOC_EXPANSION = 'list' # Exibir os endpoints por padrão

api = Api(app,
        version='1.0',
        title="API BaseCAEPI",
        doc='/swagger/',
        description="""Pesquisar e recuperar informações(por json ou arquivo de excel) sobre os certificados de aprovação emitidos para EPIs.
        Codigo fonte: https://github.com/JoaoAugustoMV/API_BaseCAEPI
        """,
        
        )

api.add_namespace(caController)

if __name__ == "__main__":    
    app.run(debug=True, host="0.0.0.0")
    