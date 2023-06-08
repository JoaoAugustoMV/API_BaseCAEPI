from pydantic import BaseModel

class InfoCADto(BaseModel):
    RegistroCA: str | None
    DataValidade: str 
    Situacao: str | None
    NRProcesso: str | None
    CNPJ: str | None
    RazaoSocial: str | None
    Natureza: str | None
    NomeEquipamento: str | None
    DescricaoEquipamento: str | None
    MarcaCA: str | None
    Referencia: str | None
    Cor: str | None
    AprovadoParaLaudo: str | None
    RestricaoLaudo: str | None
    ObservacaoAnaliseLaudo: str | None
    CNPJLaboratorio: str | None
    RazaoSocialLaboratorio: str | None
    NRLaudo: str | None
    Norma: str | None