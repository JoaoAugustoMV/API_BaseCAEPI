#  Sistema CAEPI

- Base de dados do Sistema CAEPI: Contém todas informações sobre os CA e os respectivos EPI 
  - Esta base é atualizada diariamente as 20h, localizada no endereço ftp://ftp.mtps.gov.br/portal/fiscalizacao/seguranca-e-saude-notrabalho/caepi
- CA: O Certificado de Aprovação é um documento expedido pelo Ministério do Trabalho e Emprego que atesta referente a funcionalidade daquele Equipamento de Proteção Individual (EPI).
- O site oficial do governo para consulta de CA é http://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx, mas é extremamente lento e sem nenhum tipo de integração com outros sistemas

# API
- Esta API tem como objetivo entregar uma forma fácil e rápida de consulta de informações de CAs
- Com ela é possivel:
  - Retorna as informações atualizadas do EPI 
  - Retorna todas as informações já ocorridas no EPI
  - Dado uma lista de CA: gerar um arquivo em exel ou retornar um JSON contendo todas informações de cada CA

# Funcionamento

- Automaticamente é baixado o arquivo da baseCAEPI do servidor do sistema CAEPI, ele é transformado em uma tabela(pandas.Dataframe) e através dos endpoints acontecem as consultas nessa tabela
- Tambem de forma automatica, as 20h10 é atualizada a tabela 
  - A base do servidor é atualizadas as 20h, apenas como margem de erro a tabela interna é atualizada as 20h10
  
## Stack

- Python
  - FastAPI: Aplicação Web  
  - Pandas: Controlar a tabela
- Docker: Implantar container
 
# Consumir 
 
- API está conteinerizada disponivel no DockerHub
  - Docker Hub: https://hub.docker.com/r/joaoaugustomv/api_base_ca_epi

## Iniciar container

- docker pull joaoaugustomv/api_base_ca_epi
- docker run -d -p {portaMaquina):80 --name {nomeContainer} {tag}: Executa a imagem do container
  - Ex: docker run -d -p 5200:80 --name container-api-base-ca joaoaugustomv/api_base_ca_epi:2.0
    - d: Não trava o terminal
    - p: Mapea as portas da maquina com as portas do container respectivamente. Ex: 5200:80
    - name: Nomear container
- Seguindo o exemplo a URL base será: http://localhost:5200
  - Documentação Swagger em: http://localhost:5200/swagger
  ![Documentação Swagger](https://github.com/JoaoAugustoMV/API_BaseCAEPI/blob/main/imgs/swagger.png?raw=true "Documentacao Swagger")
## Retorno JSON 
- URL/ca/:NumeroCAPretendido
docker tag api_basecaepi_fastapi-slim joaoaugustomv/api_base_ca_epi:2.0
```
{
  "RegistroCA": "string",
  "DataValidade": "string",
  "Situacao": "string",
  "NRProcesso": "string",
  "CNPJ": "string",
  "RazaoSocial": "string",
  "Natureza": "string",
  "NomeEquipamento": "string",
  "DescricaoEquipamento": "string",
  "MarcaCA": "string",
  "Referencia": "string",
  "Cor": "string",
  "AprovadoParaLaudo": "string",
  "RestricaoLaudo": "string",
  "ObservacaoAnaliseLaudo": "string",
  "CNPJLaboratorio": "string",
  "RazaoSocialLaboratorio": "string",
  "NRLaudo": "string",
  "Norma": "string"
}
```
  - OBS: Alguns EPI podem ter campos nulos

# Aviso sobre possiveis erros

- Como já falado, a base de dados é um arquivo de texto em formato csv, mas com o separador '|'
  - Exemplo: 
    ```
    #NRRegistroCA|DataValidade|Situacao|NRProcesso...\n
    20737|23/09/2013|VENCIDO|46000022149200814...\n
    ```
- Infelizmente há inconsistencias na base:
  - Há o caracter '|' em algumas linhas mas que não são para separação de colunas.O que dificulta a separação correta. Como os CA: 34535 e 42037
  
  - Como foram achados poucos registros com erro, este são tratados individualmente

- Caso ocorra de registros que não conseguiram ser tratados, estes serão adicionados em um arquivo "CAs_com_erros.txt"
- Por enquanto, não foi achado nenhum registro que tenha um erro que não pode ser tratado. Caso encontre, por favor me avise!


