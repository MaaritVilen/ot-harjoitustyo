import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
    
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate,None)
    
    def test_myydyt_edulliset_lounaat_nolla(self):
        self.assertEqual(self.kassapaate.edulliset,0)
    
    def test_myydyt_maukkaat_lounaat_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat,0)
