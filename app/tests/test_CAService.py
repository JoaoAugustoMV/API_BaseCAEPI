from unittest import TestCase
from Services.CAService import CAService

class test_CAService(TestCase):
    # def __init__(self):
    caService = CAService()

    def test_retorna_true_se_ca_for_encontrado_info_atuais(self):
        # Arrange        
        ca = '45545'

        # Act
        infoCa = self.caService.retornarTodasInfoAtuais(ca)        

        # Assert
        self.assertIsNotNone(infoCa)

    def test_retorna_true_se_ca_com_erro__linha_for_encontrado_info_atuais01(self):
        # Arrange        
        ca = '42037'

        # Act
        infoCa = self.caService.retornarTodasInfoAtuais(ca)        

        # Assert
        self.assertIsNotNone(infoCa)

    def test_retorna_true_se_ca_com_erro__linha_for_encontrado_info_atuais02(self):
        # Arrange        
        ca = '34535'

        # Act
        infoCa = self.caService.retornarTodasInfoAtuais(ca)        

        # Assert
        self.assertIsNotNone(infoCa)

    def test_retorna_false_se_ca_nao_for_encontrado_info_atuais(self):
        # Arrange        
        ca = '20'

        # Act
        infoCa = self.caService.retornarTodasInfoAtuais(ca)

        # Assert
        self.assertIsNone(infoCa)

    def test_retorna_true_se_retornar_lista_preenchida_para_todas_atualizacoes(self):
        # Arrange        
        ca = '32023'

        # Act
        listAtualizacoes = self.caService.retornarTodasAtualizacoes(ca)

        # Assert
        self.assertGreater(len(listAtualizacoes), 0)

    def test_retorna_false_se_retornar_lista_vazia_para_todas_atualizacoes(self):
        # Arrange        
        ca = '20'

        # Act
        listAtualizacoes = self.caService.retornarTodasAtualizacoes(ca)

        # Assert
        self.assertIsNone(listAtualizacoes)

    
    def test_retorna_true_se_retornar_encontrar_todos_ca_para_exportar_excel_ou_json(self):
        # Arrange        
        listaCAs = ["45545","32091","29202","15203","30215" ]

        # Act
        jsonCAs = self.caService.exportarJson(listaCAs)
        success = jsonCAs['success']
        # Assert
        self.assertTrue(success)

    def test_retorna_CAs_NAO_encontrados_ao_exportar_excel_ou_json(self):
        # Arrange        
        listaCAs = ["45545","32091","2","15203","09001018018" ]

        # Act
        jsonCAs = self.caService.exportarJson(listaCAs)
        CAsNaoEncontrados = jsonCAs['CAsNaoEncontrados']
        
        # Assert
        self.assertGreater(len(CAsNaoEncontrados), 0)

