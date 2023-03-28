import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
    
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate,None)
    
    def test_myydyt_edulliset_lounaat_nolla(self):
        self.assertEqual(self.kassapaate.edulliset,0)
    
    def test_myydyt_maukkaat_lounaat_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    #Edulliset lounaat
    def test_kateisosto_edullinen_maksu_riittava_kassa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.kassapaate.syo_edullisesti_kateisella(1000)==(1000-240)

    def test_kateisosto_edullinen_maksu_riittava_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_edullinen_maksu_ei_riittava_kassa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)
    
    def test_kateisosto_edullinen_maksu_ei_riittava_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset,0)
    
    #Maukkaat lounaat
    def test_kateisosto_maukas_maksu_riittava_kassa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.kassapaate.syo_maukkaasti_kateisella(1000)==(1000-400)

    def test_kateisosto_maukas_maksu_riittava_maara_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_maukas_maksu_ei_riittava_kassa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200),200)
    
    def test_kateisosto_maukas_maksu_ei_riittava_maara_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat,0)
    
    #Korttiostot
    
    def test_edullinen_kortilla_rahaa_ja_veloitus_oikein(self):
        self.maksukortti=Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-240)
        self.maksukortti.ota_rahaa(240)==True
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_maukas_kortilla_rahaa_ja_veloitus_oikein(self):
        self.maksukortti=Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-400)
        self.maksukortti.ota_rahaa(400)==True
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_edullinen_kortilla_ei_rahaa(self):
        self.maksukortti=Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.maksukortti.ota_rahaa(240)==False
    
    def test_maukas_kortilla_ei_rahaa(self):
        self.maksukortti=Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.maksukortti.ota_rahaa(400)==False

#Kortin lataus oikein
    def test_kortin_lataus_oikein(self):
        self.maksukortti=Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,101000)
        self.assertEqual(self.maksukortti.saldo,1000)
    
    def test_ladataan_nolla(self):
        self.maksukortti=Maksukortti(0)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100), None)