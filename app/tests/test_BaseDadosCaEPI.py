from unittest import main, TestCase

from Services.BaseDadosCaEPI import BaseDadosCaEPI

class test_BaseDadosCaEPI(TestCase):
    def test_se_baixou_e_retornou_dataframe(self):
        #Arrange
        baseCAEPI = BaseDadosCaEPI()

        #Act
        df = baseCAEPI.retornarBaseDados()
        
        #Assert
        self.assertTrue(df.size >0)

if __name__ == "__main__":
    main()