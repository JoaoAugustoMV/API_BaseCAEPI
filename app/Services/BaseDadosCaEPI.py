import ftplib
import io
import zipfile
import pandas as pd
import os


class BaseDadosCaEPI:
    baseDadosDF = None 
    nomeArquivo = 'tgg_export_caepi.txt'      
    def __init__(self):
        self = self

    def _baixarArquivoBaseCaEPI(self):
        if os.path.exists(self.nomeArquivo):
            os.remove(self.nomeArquivo)

        urlBase = 'ftp.mtps.gov.br'
        caminho = 'portal/fiscalizacao/seguranca-e-saude-no-trabalho/caepi/'

        ftp = ftplib.FTP(urlBase)
        ftp.login()
        ftp.cwd(caminho)

        arquivoZip = 'tgg_export_caepi.zip'
        r = io.BytesIO()

        ftp.retrbinary(f'RETR {arquivoZip}', r.write)

        arquivoZip = zipfile.ZipFile(r)

        arquivoZip.extractall()
    
    def _transformarEmDataFrame(self):                  
        self.baseDadosDF = pd.read_csv(self.nomeArquivo, sep=r"(?<! )\|(?<! )",engine='python', encoding='unicode_escape', quoting=3, quotechar='"', dtype="string")
        if('RegistroCA' not in self.baseDadosDF.columns):
            self.baseDadosDF = self.baseDadosDF.rename(columns = {'#NRRegistroCA':'RegistroCA'})

    def retornarBaseDados(self):        
        print("Aguarde o download...")        
        self._baixarArquivoBaseCaEPI()
        print(f"Download concluido!")

        self._transformarEmDataFrame()
        return self.baseDadosDF

    


   