from Services.BaseDadosCaEPI import BaseDadosCaEPI;
import io
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

class CAService:    
    def __init__(self):        
        self.baseDadosDF = BaseDadosCaEPI().retornarBaseDados()
        self._defineHorarioAtualizacao()
        
    def retornarTodasAtualizacoes(self, ca: str) -> list[dict]:
        dadosEPI = self.baseDadosDF.loc[self.baseDadosDF['RegistroCA'] == ca]            
        if dadosEPI.empty:
            return None
        return dadosEPI.to_dict('records')

    def retornarTodasInfoAtuais(self, ca: str) -> dict:
        dadosEPI = self.baseDadosDF.loc[self.baseDadosDF['RegistroCA'] == ca]        
        if dadosEPI.empty:
            return None
        
        return dadosEPI.iloc[-1].to_dict()
        
    def caValido(self, ca) -> bool:
        return self.retornarTodasInfoAtuais(ca)['Situacao'] == 'VÁLIDO'    
        
    def exportarExcel(self, listaCAs: list[str], nomeArquivo: str) -> dict:
        df = self._filtrarPorCAs(listaCAs)        
        
        CAsNaoEncontrados = self._retornaCAsNaoEncontrado(df, listaCAs)
        if CAsNaoEncontrados != []:
            return {'success': False, 'CAsNaoEncontrados': CAsNaoEncontrados}
        
    # Converter o dataframe para um objeto Excel em memória
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=nomeArquivo)
        
        writer.close()
        output.seek(0)

        return {"success": True, 'planilha': output}
    
    def exportarJson(self, listaCAs: list[str]) -> dict:
        df = self._filtrarPorCAs(listaCAs)
        CAsNaoEncontrados = self._retornaCAsNaoEncontrado(df, listaCAs)
        if CAsNaoEncontrados != []:
            return {'success': False, 'CAsNaoEncontrados': CAsNaoEncontrados}
        
        return {"success": True, "JSON": df.to_dict('records')}
            
    def _filtrarPorCAs(self, listaCAs: list[str]) -> pd.DataFrame:        
        df = self.baseDadosDF.loc[self.baseDadosDF['RegistroCA'].isin(listaCAs)]
        return df.drop_duplicates('RegistroCA', keep='last')
    
    def _retornaCAsNaoEncontrado(self, df: pd.DataFrame, listaCAs: list[str]) -> list[str]:       
        return [ca for ca in listaCAs if ca not in df['RegistroCA'].values]
    
    def _atualizarBaseDados(self):
        self.baseDadosDF = BaseDadosCaEPI().retornarBaseDados()
        print("Base de Dados atualizada em", datetime.now())

    def _defineHorarioAtualizacao(self):
        horaAtualizacao = 20
        minutoAtualizacao = 10
        scheduler = BackgroundScheduler()
        scheduler.start()

        # É atualizado as 20h, mas resolvi dar uma margem de erro
        scheduler.add_job(self._atualizarBaseDados, 'cron', hour=horaAtualizacao, minute=minutoAtualizacao, day_of_week='0-6')
    


    