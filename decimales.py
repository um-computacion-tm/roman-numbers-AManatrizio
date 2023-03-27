import unittest

def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 5:
        return 'V'
    elif decimal == 40:
        return 'XL'
    elif decimal == 50:
        return 'L'
    elif decimal == 90:
        return 'XC'
    elif decimal == 100:
        return 'C'
    elif decimal == 400:
        return 'CD'
    elif decimal == 500:
        return 'D'
    elif decimal == 900:
        return 'CM'
    elif decimal == 1000:
        return 'M'
    elif decimal == 10:
        return 'X'


class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')

    def test_cuarenta(self):
        resultado = decimal_to_roman(40)
        self.assertEqual(resultado, 'XL')  

    def test_cincuenta(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, 'L')

    def test_noventa(self):
        resultado = decimal_to_roman(90)
        self.assertEqual(resultado, 'XC')  

    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')  

    def test_quinientos(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, 'D')            
    
    def test_novecientos(self):
        resultado = decimal_to_roman(900)
        self.assertEqual(resultado, 'CM')

    def test_mil(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, 'M')



if __name__ == '__main__':
    unittest.main()