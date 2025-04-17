import ftplib
import io
import zipfile
import pandas as pd
import os
import re

class BaseDadosCaEPI:
    baseDadosDF = None 
    nomeArquivoBase = 'tgg_export_caepi.txt'
    nomeArquivoConfigNomesColunas = 'config_nomes_colunas.csv'
    nomeArquivoErros = 'CAs_com_erros.txt'    
    urlBase = 'ftp.mtps.gov.br'
    caminho = 'portal/fiscalizacao/seguranca-e-saude-no-trabalho/caepi/'
    nColunas = 19


    nomeColunas = [
        "RegistroCA",
        "DataValidade",
        "Situacao",
        "NRProcesso",
        "CNPJ",
        "RazaoSocial",
        "Natureza",
        "NomeEquipamento",
        "DescricaoEquipamento",
        "MarcaCA",
        "Referencia",
        "Cor",
        "AprovadoParaLaudo",
        "RestricaoLaudo",
        "ObservacaoAnaliseLaudo",
        "CNPJLaboratorio",
        "RazaoSocialLaboratorio",
        "NRLaudo",
        "Norma"        
    ]

    def __init__(self):
        self = self

    def _baixarArquivoBaseCaEPI(self):
        if os.path.exists(self.nomeArquivoBase):
            os.remove(self.nomeArquivoBase)

        ftp = ftplib.FTP(self.urlBase)
        ftp.login()
        ftp.cwd(self.caminho)

        nomeArquivoZip = 'tgg_export_caepi.zip'
        r = io.BytesIO()

        ftp.retrbinary(f'RETR {nomeArquivoZip}', r.write)

        arquivoZip = zipfile.ZipFile(r)

        arquivoZip.extractall()
    
    def _transformarEmDataFrame(self):          
        listaCas = self._retornarCAsSemErros()
        cols = listaCas[0]
        self.baseDadosDF = pd.DataFrame(listaCas, columns=cols)        

        self.baseDadosDF.columns = self.__retornaNomesColunas()

    def __retornaNomesColunas(self):
        arquivo = open(self.nomeArquivoConfigNomesColunas, encoding='UTF-8')

        return arquivo.readline().split(',')

    def _retornarCAsSemErros(self) -> list:
        listaCAsValidos = []
        listaCAsInvalidos = []

        arquivo = open(self.nomeArquivoBase, encoding='UTF-8')
        
        for linha in arquivo.readlines():
            linhaDf = linha.split('|')
            if len(linhaDf) > self.nColunas:
                resul_tratamento = self._tratarCasComErros(linha)
                if resul_tratamento['sucess']:
                    linhaDf = resul_tratamento['linha']
                else:
                    listaCAsInvalidos.append(linha)
                    continue
    
            listaCAsValidos.append(linhaDf)
        
        if listaCAsInvalidos:
            self._criarArquivoComErros(listaCAsInvalidos)
            
        return listaCAsValidos
    
    def _tratarCasComErros(self, linha) -> dict:
        linhaDf = re.split(r'(?<! )\|', linha)
        if len(linhaDf) > self.nColunas: # Erro
            return {
                'sucess': False,
                'linha': linha
            }

        return    {
            'sucess': True,
            'linha': linhaDf
        }

    def _criarArquivoComErros(self, listaCAsInvalidos:list) -> None:
        with open(self.nomeArquivoErros, 'w') as f:
            f.writelines(listaCAsInvalidos)
    
    def retornarBaseDados(self) -> pd.DataFrame:
        if not os.path.exists(self.nomeArquivoBase):
            print("Aguarde o download...")        
            self._baixarArquivoBaseCaEPI()
            print(f"Download concluido!")

        self._transformarEmDataFrame()
        return self.baseDadosDF

    


   