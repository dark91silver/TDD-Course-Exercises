import unittest

import booking
import errors

#test ricerca
class TestSearch(unittest.TestCase):
    #ricerca ok
    def ok(self):
        arrivo = "2025-02-24"
        partenza = "2025-02-25"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), ["101"])
    #ricerca fallisce per prenotazione che copre i primi giorni
    def arrivo_bloccato(self):
        arrivo = "2025-02-19"
        partenza = "2025-02-21"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])
    #ricerca fallisce per prenotazione che copre gli ultimi giorni
    def part_bloccata(self):
        arrivo = "2025-02-22"
        partenza = "2025-02-25"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])
    #ricerca fallisce per prenotazione che copre gli stessi giorni
    def giorni_bloccati(self):
        arrivo = "2025-02-20"
        partenza = "2025-02-24"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])
    #ricerca fallisce per prenotazione che copre + giorni
    def intervallo_maggiore(self):
        arrivo = "2025-02-19"
        partenza = "2025-02-26"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])
    #ricerca fallisce per prenotazione che copre - giorni
    def intervallo_minore(self):
        arrivo = "2025-02-22"
        partenza = "2025-02-23"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])
    #ricerca fallisce perché data nulla
    def data_vuota(self):
        arrivo = ""
        partenza = ""
        self.assertRaises(booking.search(arrivo, partenza, "test.json"), errors.WrongFormatDate)
    #richiesta fallisce perché data formato errato
    def formato_sbagliato(self):
        arrivo = "ventiquattro febbraio 2025"
        partenza = "02 24th 2025"
        self.assertRaises(booking.search(arrivo, partenza, "test.json"), errors.WrongFormatDate)
    #richiesta fallisce perché data antecedente a oggi
    def ieri(self):
        arrivo = "2025-02-17"
        partenza = "2025-02-18"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), errors.WrongIntervalDate)
    #richiesta fallisce perché arrivo dopo partenza
    def invertiti(self):
        arrivo = "2025-02-23"
        partenza = "2025-02-22"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), errors.WrongIntervalDate)

#test prenotazione
class TestBook(unittest.TestCase):
    #prenotazione ok
    def ok(self):
        pren = {
            "arrivo": "2025-02-24",
            "partenza": "2025-02-25",
            "nome": "luigi",
            "cognome": "bianchi",
            "cf": "cde234"
        }
        self.assertTrue(booking.book(pren, "101", "test.json"))
    #prenotazione fallisce perché qualcuno ha già prenotato quella camera
    def bloccata(self):
        pren = {
            "arrivo": "2025-02-22",
            "partenza": "2025-02-23",
            "nome": "luigi",
            "cognome": "bianchi",
            "cf": "cde234"
        }
        self.assertFalse(booking.book(pren, "101", "test.json"))
    #prenotazione fallisce perché campi nulli
    def formato_errato(self):
        pren = {
            "arrivo": "2025-02-22",
            "partenza": "2025-02-23",
            "nome": None,
            "cognome": "bianchi",
            "cf": "cde234"
        }
        self.assertRaises(booking.book(pren, "101", "test.json"), errors.WrongFormatInput)
    #prenotazione fallisce perché campi vuoti
    def formato_errato(self):
        pren = {
            "arrivo": "2025-02-22",
            "partenza": "2025-02-23",
            "nome": "",
            "cognome": "",
            "cf": "cde234"
        }
        self.assertRaises(booking.book(pren, "101", "test.json"), errors.WrongFormatInput)
    #prenotazione fallisce perché campi formato errato
    def formato_errato(self):
        pren = {
            "arrivo": "2025-02-22",
            "partenza": "2025-02-23",
            "nome": "luigi",
            "cognome": "bianchi",
            "cf": 12345
        }
        self.assertRaises(booking.book(pren, "101", "test.json"), errors.WrongFormatInput)
    #prenotazione fallisce perché date formato errato
    def date_errate(self):
        pren = {
            "arrivo": "duemilaventicinque trattino zerodue trattino diciotto",
            "partenza": "",
            "nome": "luigi",
            "cognome": "bianchi",
            "cf": "cde234"
        }
        self.assertRaises(booking.book(pren, "101", "test.json"), errors.WrongFormatDate)
    #prenotazione fallisce perché date invertite
    def date_errate(self):
        pren = {
            "arrivo": "2025-02-25",
            "partenza": "2025-02-24",
            "nome": "luigi",
            "cognome": "bianchi",
            "cf": "cde234"
        }
        self.assertRaises(booking.book(pren, "101", "test.json"), errors.WrongIntervalDate)
    #prenotazione fallisce perché ieri
    def date_errate(self):
        pren = {
            "arrivo": "2025-02-17",
            "partenza": "2025-02-18",
            "nome": "luigi",
            "cognome": "bianchi",
            "cf": "cde234"
        }
        self.assertRaises(booking.book(pren, "101", "test.json"), errors.WrongIntervalDate)
    #prenotazione fallisce perché stesso utente ha prenotato stessa camera per stessi giorni
    def bloccata(self):
        pren = {
            "arrivo": "2025-02-20",
            "partenza": "2025-02-24",
            "nome": "mario",
            "cognome": "rossi",
            "cf": "abc123"
        }
        self.assertFalse(booking.book(pren, "101", "test.json"))

class IntegrationTest(unittest.TestCase):
    def ok(self):
        #utente fa ricerca
        #ricerca dà esito positivo
        #utente prenota
        #prenotazione dà esito positivo
        pass
    def no_disponibilità(self):
        #utente fa ricerca
        #ricerca dà esito negativo
        pass
    def prenotazione_concorrente(self):
        #utente1 fa ricerca
        #utente2 fa ricerca
        #entrambi esito positivo
        #utente1 prenota
        #utente1 ha esito positivo
        #utente2 prenota
        #utente2 ha esito negativo
        pass

if __name__ == '__main__':
    unittest.main()
