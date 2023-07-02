from typing import Annotated

from fastapi import Body, APIRouter
from fastapi.responses import JSONResponse, StreamingResponse

from Services.CAService import CAService

from models.exemplosRequest import ExemplosRequest
from models.requestParaExportarArquivo import RequestParaExportarArquivo
from models.requestParaExportarJson import RequestParaExportarJson
from models.infoCADto import InfoCADto
from models.responsesModels import ResponsesModels

router = APIRouter(tags=["Certificado de Aprovação"])
caService  = CAService()


@router.get('/CA/{ca}',
            status_code=200, 
            summary= "Retorna as informações atuais do CA",
            description="Retorna apenas a ultima ocorrencia(dados atuais)",
            responses=ResponsesModels.responsesInfoCA
            )
async def retornarInfoCA(ca: str) -> InfoCADto:
    dadosEPI = caService.retornarTodasInfoAtuais(ca)
    if dadosEPI == None:            
        return ResponsesModels.responsesCANaoEncontrado           

    return dadosEPI

@router.get('/retornarTodasAtualizacoes/{ca}',
            status_code=200, 
            summary= "Retorna as todas as atualizações  CA",
            description="Retorna as todas as atualizações  CA",
            responses=ResponsesModels.responsesInfoCA)
async def retornarTodasAtualizacoes(ca: str) -> list[InfoCADto]:
    dadosEPI = caService.retornarTodasAtualizacoes(ca)
    if dadosEPI == None:            
        return ResponsesModels.responsesCANaoEncontrado           
    
    return dadosEPI
        
@router.get('/validarSituacao/{ca}',
            status_code=200, 
            summary= "Retorna se o CA está válido",
            description="Retorna se o CA está válido",)
async def validarCA(ca: str):
    dadosEPI = caService.caValido(ca)
    if dadosEPI == None:            
        return ResponsesModels.responsesCANaoEncontrado
    
    return dadosEPI

@router.post('/exportarExcel', 
            summary= "Gera um arquivo excel com os CAs informados",
            description="Gera um arquivo excel com os CAs informados, caso algum CA não seja encontrado ocorrerá um erro",
            responses=ResponsesModels.responsesExportar)
def exportarExcel(
    request: Annotated[RequestParaExportarArquivo, Body(
    example=ExemplosRequest.exportarArquivo)] ) -> StreamingResponse:
    # Criar uma resposta para o arquivo Excel
    if len(request.listaCAs) == 0:
        return ResponsesModels.responsesListaVazia
    respExportarExcel = caService.exportarExcel(request.listaCAs, request.nomeArquivo)

    if not respExportarExcel['success']:
        return ResponsesModels().responsesExportarCAsNaoEncontrado(respExportarExcel['CAsNaoEncontrados'])
    
    planilha = respExportarExcel['planilha']

    response = StreamingResponse(planilha,
                                media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                headers={'Content-Disposition': f'attachment; filename={request.nomeArquivo}.xlsx'}
                                )    

    return response

@router.post('/exportarJSON', 
            summary= "Retorna um JSON com as informações dos CAs informados",                        
            responses=ResponsesModels.responsesExportar)
def exportarJSON(request: Annotated[RequestParaExportarJson, Body(
        example=ExemplosRequest.exportarJSON)
    ]) -> list[InfoCADto]:
    if len(request.listaCAs) == 0:
        return ResponsesModels.responsesListaVazia

    respExportarJson = caService.exportarJson(request.listaCAs)
    if not respExportarJson['success']:        
        return ResponsesModels().responsesExportarCAsNaoEncontrado(respExportarJson['CAsNaoEncontrados'])
    
    return respExportarJson['JSON']