#  Sistema CAEPI

- Base de dados do Sistema CAEPI: Contem todas informações sobre os CA e os respectivos EPI 
  - Esta base é atualizada diariamente as 20h, localizada no endereço ftp://ftp.mtps.gov.br/portal/fiscalizacao/seguranca-e-saude-notrabalho/caepi
- CA: O Certificado de Aprovação é um documento expedido pelo Ministério do Trabalho e Emprego que atesta referente a funcionalidade daquele Equipamento de Proteção Individual (EPI).

# API
- Esta API tem como objetivo entregar uma forma facil e rapida de consulta de informações de CAs
- Com ela é possivel:
  - Retorna as informações atualizadas do EPI 
  - Retorna todas as informações já ocorridas no EPI
  - Dado uma lista de CA: gerar um arquivo em exel ou retornar um JSON contendo todas informações de cada CA

# Funcionamento

- Automaticamente é baixado o arquivo da baseCAEPI do servidor do sistema CAEPI, ele é transformado em uma tabela(pandas.Dataframe) e atraves dos endpoints acontecem as consultas nessa tabela
- Tambem de forma automatica, as 20h10 é atualizada a tabela 
  - A base do servidor é atualizadas as 20h, apenas como margem de erro a tabela é atualizada as 20h10
## Stack

- Python
  - Flask: Aplicação Web
  - Flask_restx: Documentação no Swagger
  - Pandas: Controlar a tabela
- Docker: Controlar container
 
# Consumir 
 
- API está conteinerizada disponivel no DockerHub
  - Docker Hub: https://hub.docker.com/r/joaoaugustomv/api_certificado_aprovacao

## Iniciar container

- docker pull {tag}: Baixa a imagem do docker hub
- docker run -d -p {portaMaquina):5000 --name {nomeContainer} {tag}: Executa a imagem do container
    - d: Não trava o terminal
    - p: Mapea as portas da maquina com as portas do container respectivamente. Ex: 5200:5000
    - t: Nomear container
- Seguindo o exemplo a URL base será: http://localhost:5200
  - Documentação Swagger em: http://localhost:5200/swagger
  ![Documentação Swagger](https://github.com/JoaoAugustoMV/API_BaseCAEPI/blob/main/imgs/swagger.png?raw=true "Documentacao Swagger")
## Retorno JSON 
- URL/ca/:NumeroCAPretendido
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



