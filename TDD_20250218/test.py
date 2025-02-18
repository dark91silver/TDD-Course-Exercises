import unittest

import booking

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
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])
    #richiesta fallisce perché data formato errato
    def formato_sbagliato(self):
        arrivo = "ventiquattro febbraio 2025"
        partenza = "02 24th 2025"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])
    #richiesta fallisce perché data antecedente a oggi
    def ieri(self):
        arrivo = "2025-02-17"
        partenza = "2025-02-18"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])
    #richiesta fallisce perché arrivo dopo partenza
    def invertiti(self):
        arrivo = "2025-02-23"
        partenza = "2025-02-22"
        self.assertEqual(booking.search(arrivo, partenza, "test.json"), [])

#test prenotazione
class TestBook(unittest.TestCase):
    #prenotazione ok
    def ok(self):
        pass
    #prenotazione fallisce perché qualcuno ha già prenotato quella camera
    #prenotazione fallisce perché campi nulli o formato errato
    #prenotazione fallisce perché date formato errato
    #prenotazione fallisce perché date invertite
    #prenotazione fallisce perché utente ha prenotato stessa camera per stessi giorni

if __name__ == '__main__':
    unittest.main()
