from models.requestParaExportarArquivo import RequestParaExportarArquivo
from models.requestParaExportarJson import RequestParaExportarJson


class ExemplosRequest():
    listaExemplos = [
                    "45545",
                    "32091",
                    "29202",
                    "15203",
                    "30215"
                    ]

    exportarArquivo = RequestParaExportarArquivo(nomeArquivo="ExemploArquivo", listaCAs=listaExemplos)
    exportarJSON = RequestParaExportarJson(listaCAs=listaExemplos)