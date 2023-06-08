from models.requestParaExportarArquivo import RequestParaExportarArquivo
from models.requestParaExportarJson import RequestParaExportarJson


class ExemplosRequest():
    exportarArquivo = RequestParaExportarArquivo(nomeArquivo="ExemploArquivo", listaCAs=[
        "45545",
        "32091",
        "29202",
        "15203",
        "30215"
        ])
    exportarArquivo = RequestParaExportarJson(
        listaCAs=[
            "45545",
            "32091",
            "29202",
            "15203",
            "30215"
        ])