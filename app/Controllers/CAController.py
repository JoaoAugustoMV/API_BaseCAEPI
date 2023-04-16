from flask import request, make_response
from flask_restx import Namespace, Resource, fields, marshal
from app.Services.CAService import CAService


api = Namespace('CA', description="Consultas e Operações da BaseCAEPI")

modeloInfoCA = api.model('Dados CA',{
    'RegistroCA': fields.String,
    'DataValidade': fields.String,
    'Situacao': fields.String,
    'NRProcesso': fields.String,
    'CNPJ': fields.String,
    'RazaoSocial': fields.String,
    'Natureza': fields.String,
    'NomeEquipamento': fields.String,
    'DescricaoEquipamento': fields.String,
    'MarcaCA': fields.String,
    'Referencia': fields.String,
    'Cor': fields.String,
    'AprovadoParaLaudo': fields.String,
    'RestricaoLaudo': fields.String,
    'ObservacaoAnaliseLaudo': fields.String,
    'CNPJLaboratorio': fields.String,
    'RazaoSocialLaboratorio': fields.String,
    'NRLaudo': fields.String,
    'Norma': fields.String
    })

modeloExportarExcel = api.model('Dados para exportar Excel',{
    'nomeArquivo': fields.String,
    'listaCAs': fields.List(fields.String)
    })
modeloExportarJSON = api.model('Dados para exportar JSON',{
    'listaCAs': fields.List(fields.String)
    })

modeloCAsNaoEncontrados = api.model("CAs não encontrados",{'success': fields.Boolean, 'CAsNaoEncontrados': fields.List(fields.String)})

caService = CAService()

@api.route('/<string:ca>')
@api.param('ca', "Numero do Certifacado de Aprovação do EPI")
@api.response(400, "Numero Ca não encontrado")
@api.response(200, "Informações do EPI", model=modeloInfoCA)
class RetornarInfoCA(Resource):
    # @api.marshal_with(modeloInfoCA)
    def get(self, ca):
        """
        Retorna apenas a ultima ocorrencia(dados atuais)
        """
        dadosEPI = caService.retornarTodasInfoAtuais(ca)
        if dadosEPI != None:            
            return dadosEPI
        api.abort(400, "Numero Ca não encontrado!")

@api.route('/retornarTodasAtualizacoes/<string:ca>')
@api.param('ca', "Numero do Certifacado de Aprovação do EPI")
@api.response(400, "Numero Ca não encontrado")
@api.response(200, "Informações do EPI", model=fields.List(fields.Nested(modeloInfoCA)))
class RetornarTodasAtualizacoes(Resource):
    @api.expect(fields.String, validate=True)
    # @api.marshal_list_with(modeloInfoCA)    
    def get(self, ca):
        """
        Retorna todas as ocorrencias
        """
        dadosEPI = caService.retornarTodasAtualizacoes(ca)
        if dadosEPI != None:            
            return dadosEPI
        api.abort(404, "Numero Ca não encontrado!")
        

@api.route('/exportarExcel')
@api.response(400, "Um ou mais CA não foram encontrados", modeloCAsNaoEncontrados)
@api.response(200, "Todas CA foram encontrados e arquivo foi gerado com sucesso")
class ExportarExcel(Resource):
    @api.expect(modeloExportarExcel)
    def post(self):
        """
        Gera um arquivo em excel com os respectivos CA 
        """
        jsonRequisicao = request.get_json()        
        # Criar uma resposta para o arquivo Excel
        respExportarExcel = caService.exportarExcel(jsonRequisicao['listaCAs'], jsonRequisicao['nomeArquivo'])
        if not respExportarExcel['success']:
            return api.abort(400, respExportarExcel)
        planilha = respExportarExcel['planilha']

        response = make_response(planilha)
        response.headers['Content-Disposition'] = f'attachment; filename={jsonRequisicao["nomeArquivo"]}.xlsx'
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        
        return response

@api.route('/exportarJSON')
@api.response(400, "Um ou mais CA não foram encontrados", modeloCAsNaoEncontrados)
@api.response(200, "Todas CA foram encontrados",  model=fields.List(fields.Nested(modeloInfoCA)))
class ExportarJSON(Resource):
    @api.expect(modeloExportarJSON)
    def post(self):
        """
        Retorna um JSON com os respectivos CA 
        """
        jsonRequisicao = request.get_json()
        respExportarJson = caService.exportarJson(jsonRequisicao['listaCAs'])

        if not respExportarJson['success']:
            return api.abort(400, respExportarJson)
        
        
        return respExportarJson['JSON']