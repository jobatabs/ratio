import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.varakas_maksukortti = Maksukortti(100000)
        self.varaton_maksukortti = Maksukortti(0)

    def test_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_oikea_maara_lounaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_edullisesti_kateisella(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(1000)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(vaihtorahat, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_maukkaasti_kateisella(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(1000)

        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtorahat, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_ei_tarpeeksi_rahaa_maukkaaseen_kateisella(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(399)

        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtorahat, 399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ei_tarpeeksi_rahaa_edulliseen_kateisella(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(239)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vaihtorahat, 239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.varakas_maksukortti)

        self.assertEqual(str(self.varakas_maksukortti), "Kortilla on rahaa 997.60 euroa")
        self.assertTrue(onnistui)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.varakas_maksukortti)

        self.assertEqual(str(self.varakas_maksukortti), "Kortilla on rahaa 996.00 euroa")
        self.assertTrue(onnistui)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ei_tarpeeksi_rahaa_maukkaaseen_kortilla(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.varaton_maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.varaton_maksukortti), "Kortilla on rahaa 0.00 euroa")
        self.assertFalse(onnistui)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ei_tarpeeksi_rahaa_edulliseen_kortilla(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.varaton_maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(str(self.varaton_maksukortti), "Kortilla on rahaa 0.00 euroa")
        self.assertFalse(onnistui)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_rahan_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.varaton_maksukortti, 1000)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(self.varaton_maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortille_negatiivinen_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.varakas_maksukortti, -100)
        
        self.assertEqual(str(self.varakas_maksukortti), "Kortilla on rahaa 1000.00 euroa")