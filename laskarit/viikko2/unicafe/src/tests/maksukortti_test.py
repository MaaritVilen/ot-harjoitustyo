import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
	def setUp(self):
        	self.maksukortti = Maksukortti(1000)

	def test_luotu_kortti_on_olemassa(self):
		self.assertNotEqual(self.maksukortti, None)

	def test_kortin_saldo_alussa_oikein(self):
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

	def test_rahan_lataus_oikein(self):
		self.maksukortti.lataa_rahaa(1000)

		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
	
	def test_saldo_vahenee_oikein_jos_rahaa(self):
		self.maksukortti.ota_rahaa(500)

		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
	
	def test_saldo_ei_vahene_jos_ei_rahaa(self):
		self.maksukortti.ota_rahaa(1500)

		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
	
	def test_palauttaa_true(self):
		self.maksukortti.ota_rahaa(500)==True
	
	def test_palauttaa_false(self):
		self.maksukortti.ota_rahaa(1500)==False
		
