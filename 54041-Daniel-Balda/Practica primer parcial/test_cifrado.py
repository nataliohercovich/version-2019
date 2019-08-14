import unittest
from cifrado import encrypt

class TestEncryptText(unittest.TestCase):
    def test_encrypt_text_casa_nueva(self):
        result_encrypt = encrypt('casa nueva','pais')
        self.assertEqual(result_encrypt, 'raas%cumnp')

    def test_encrypt_text_hola_mundo(self):
            result_encrypt = encrypt('holamundo','puerta')
            self.assertEqual(result_encrypt, 'wiprfucxs')

    def test_encrypt_text_murcielago(self):
            result_encrypt = encrypt('murcielago','google')
            self.assertEqual(result_encrypt, 'sifitirouu')

if __name__ == '__main__':
    unittest.main()