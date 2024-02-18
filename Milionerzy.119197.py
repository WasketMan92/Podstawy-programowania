import random

class Milionerzy:
    def __init__(self):
        self.imie = None
        self.pytania = []
        self.obecne_pytanie = None
        self.pozostale_kola = {
            'A': self.uzyj_kola_telefon_do_przyjaciela,
            'B': self.uzyj_kola_pol_na_pol,
            'C': self.uzyj_kola_pytanie_do_publicznosci
        }
        self.pomoc_publicznosci_procenty = None
        self.wygrana = 0
        self.kwoty = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
        self.gwarantowane_kwoty = {1000, 40000}
        self.gwarantowana_kwota = 0

    def uzyj_kola_telefon_do_przyjaciela(self):
        self.zapisz_pytanie_przed_kolem()
        self.telefon_do_przyjaciela()
        self.przywroc_pytanie_po_kole()
        self.wyswietl_pytanie()

    def uzyj_kola_pol_na_pol(self):
        self.zapisz_pytanie_przed_kolem()
        self.pol_na_pol()
        self.przywroc_pytanie_po_kole()
        self.wyswietl_pytanie()

    def uzyj_kola_pytanie_do_publicznosci(self):
        self.zapisz_pytanie_przed_kolem()
        self.pytanie_do_publicznosci()
        self.przywroc_pytanie_po_kole()
        self.wyswietl_pytanie()
       
    def wprowadz_imie(self):
        self.imie = input("Wpisz swoje imię: ")

    def generuj_pytania(self):
        ilosc_brakujacych_pytan = 15 - len(self.pytania)
        pytania = [
        {
            'pytanie': 'Jaki jest kolor nieba?',
            'odpowiedzi': ['Czerwony', 'Niebieski', 'Zielony', 'Żółty'],
            'poprawna_nr': 2
        },
        {
            'pytanie': 'Kto napisał "Lalkę"?',
            'odpowiedzi': ['Henryk Sienkiewicz', 'Bolesław Prus', 'Adam Mickiewicz', 'Juliusz Słowacki'],
            'poprawna_nr': 2
        },
        {
            'pytanie': 'Jaką stolicę ma Polska?',
            'odpowiedzi': ['Warszawa', 'Kraków', 'Gdańsk', 'Poznań'],
            'poprawna_nr': 1
        },
        {
            'pytanie': 'Ile wynosi 2 do potęgi 3?',
            'odpowiedzi': ['6', '8', '12', '16'],
            'poprawna_nr': 2
        },
        {
            'pytanie': 'Kto jest autorem "Zbrodni i kary"?',
            'odpowiedzi': ['Fiodor Dostojewski', 'Leo Tolstoj', 'Gabriel Garcia Marquez', 'Ernest Hemingway'],
            'poprawna_nr': 1
        },
        {
            'pytanie': 'Która planeta jest najbliżej Słońca?',
            'odpowiedzi': ['Mars', 'Wenus', 'Jowisz', 'Merkury'],
            'poprawna_nr': 4
        },
        {
            'pytanie': 'Ile kontynentów jest na Ziemi?',
            'odpowiedzi': ['4', '5', '6', '7'],
            'poprawna_nr': 3
        },
        {
            'pytanie': 'Kto jest prezydentem Stanów Zjednoczonych (2022)?',
            'odpowiedzi': ['Joe Biden', 'Donald Trump', 'Angela Merkel', 'Emmanuel Macron'],
            'poprawna_nr': 1
        },
        {
            'pytanie': 'Ile wynosi pierwiastek kwadratowy z 144?',
            'odpowiedzi': ['10', '12', '14', '16'],
            'poprawna_nr': 2
        },
        {
            'pytanie': 'Kto jest autorem obrazu "Mona Lisa"?',
            'odpowiedzi': ['Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Claude Monet'],
            'poprawna_nr': 2
        },
        {
            'pytanie': 'Które zwierzę jest najszybsze na świecie?',
            'odpowiedzi': ['Szympans', 'Gepard', 'Kondor', 'Żyrafa'],
            'poprawna_nr': 2
        },
        {
            'pytanie': 'Która rzeka jest najdłuższa na świecie?',
            'odpowiedzi': ['Nil', 'Amazonka', 'Missisipi', 'Jangcy'],
            'poprawna_nr': 1
        },
        {
            'pytanie': 'Ile wynosi 7 razy 9?',
            'odpowiedzi': ['45', '54', '63', '72'],
            'poprawna_nr': 3
        },
        {
            'pytanie': 'Który instrument jest znany jako "król instrumentów"?',
            'odpowiedzi': ['Gitara', 'Fortepian', 'Skrzypce', 'Organy'],
            'poprawna_nr': 4
        },
        {
            'pytanie': 'Kto jest autorem dramatu "Romeo i Julia"?',
            'odpowiedzi': ['William Shakespeare', 'Jane Austen', 'Fyodor Dostoevsky', 'Charles Dickens'],
            'poprawna_nr': 1
        },
        ]
        if ilosc_brakujacych_pytan > 0 and ilosc_brakujacych_pytan <= len(pytania):
            nowe_pytania = random.sample(pytania, ilosc_brakujacych_pytan)
            nowe_pytania.sort(key=lambda x: self.kwoty[pytania.index(x)])
            self.pytania.extend(nowe_pytania)

    def losuj_pytanie(self):
        self.obecne_pytanie = self.pytania.pop(random.randrange(len(self.pytania)))

    def wyswietl_pytanie(self):
        print(f"\n{self.imie}, oto twoje pytanie (wartość pytania: {self.kwoty[-len(self.pytania) - 1]} PLN):")
        print(self.obecne_pytanie['pytanie'])
        for i, odp in enumerate(self.obecne_pytanie['odpowiedzi'], 1):
            print(f"{i}. {odp}")
        print()

    def telefon_do_przyjaciela(self):
        print("\nPrzyjaciel mówi:")
        print(f"Myślę, że poprawna odpowiedź to: {random.choice(self.obecne_pytanie['odpowiedzi'])}\n")

    def zapisz_pytanie_przed_kolem(self):
        self.pytanie_przed_kolem = self.obecne_pytanie.copy()

    def przywroc_pytanie_po_kole(self):
        self.obecne_pytanie = self.pytanie_przed_kolem.copy()

    def pol_na_pol(self):
        poprawna_nr = self.obecne_pytanie['poprawna_nr']
        poprawna = self.obecne_pytanie['odpowiedzi'][poprawna_nr - 1]
        do_usuniecia = [odp for odp in self.obecne_pytanie['odpowiedzi'] if odp != poprawna]
        do_usuniecia = random.sample(do_usuniecia, 2)
        print(f"\nUsuń dwie błędne odpowiedzi: {do_usuniecia[0]}, {do_usuniecia[1]}\n")
        obecne_pytanie_copy = self.obecne_pytanie.copy()
        obecne_pytanie_copy['odpowiedzi'] = [odp for odp in obecne_pytanie_copy['odpowiedzi'] if
                                             odp == poprawna or odp in do_usuniecia]
        for i, pytanie in enumerate(self.pytania):
            if pytanie['pytanie'] == self.obecne_pytanie['pytanie']:
                self.pytania[i] = obecne_pytanie_copy
        self.obecne_pytanie = obecne_pytanie_copy

    def pytanie_do_publicznosci(self):
        print("\nPubliczność podaje sugestie odpowiedzi:")
        obecne_pytanie_copy = self.obecne_pytanie.copy()
        self.pomoc_publicznosci_procenty = [random.randint(10, 90) for _ in
                                            range(len(obecne_pytanie_copy['odpowiedzi']))]
        indeksy = list(range(len(obecne_pytanie_copy['odpowiedzi'])))
        indeksy.sort(key=lambda x: self.pomoc_publicznosci_procenty[x], reverse=True)
        for i, indeks in enumerate(indeksy, 1):
            odp = obecne_pytanie_copy['odpowiedzi'][indeks]
            print(f"{i}. {odp}: {self.pomoc_publicznosci_procenty[indeks]}%")

    def wyswietl_dostepne_kola(self):
        dostepne_kola = [litera for litera in self.pozostale_kola.keys()]
        print("\nDostępne koła ratunkowe:")
        for litera in dostepne_kola:
            print(f"- {litera} ({self.pozostale_kola[litera].__name__})")
        print()

    def start(self):
        print("Witaj w grze Milionerzy!\n")
        self.wprowadz_imie()
        self.generuj_pytania()

        print(f"{self.imie}, zaczynamy grę! Masz szansę zdobyć milion PLN.\n")

        while self.pytania:
            self.losuj_pytanie()
            self.zapytaj()

        print(f"Dziękujemy za udział w grze, {self.imie}! Zdobyłeś/aś {self.wygrana} PLN!")

    def zapytaj(self):
        if self.obecne_pytanie is None:
            self.losuj_pytanie()

        while True:
            self.wyswietl_pytanie()
            self.wyswietl_dostepne_kola()

            dostepne_kola = [litera for litera in self.pozostale_kola.keys()]
            dostepne_kola += [self.pozostale_kola[litera].__name__ for litera in self.pozostale_kola.keys()]

            if 'kola' in self.pozostale_kola:
                dostepne_kola.append('kola')

            odpowiedz = input(f"Podaj literę odpowiedzi (lub 'koniec' aby zakończyć, 'rezygnuj' aby zakończyć grę, {', '.join(dostepne_kola)} aby skorzystać z koła ratunkowego): ")

            if odpowiedz.lower() == 'koniec':
                return
            elif odpowiedz.lower() == 'rezygnuj':
                print(
                    f"\n{self.imie}, rezygnujesz z gry. Twoja wygrana wynosi: {self.gwarantowana_kwota} PLN. Do zobaczenia!")
                self.pytania.clear()
                exit()  # Zamyka program po zakończeniu gry
            else:
                if odpowiedz in dostepne_kola:
                    if odpowiedz == 'kola':
                        self.pozostale_kola['kola']()
                    else:
                        self.pozostale_kola[odpowiedz]()
                elif odpowiedz.isdigit() and 1 <= int(odpowiedz) <= len(self.obecne_pytanie['odpowiedzi']):
                    kwota = self.kwoty[len(self.kwoty) - len(self.pytania)]
                    if int(odpowiedz) == self.obecne_pytanie['poprawna_nr']:
                        print(f"Poprawna odpowiedź! Gratulacje! Wygrana wynosi: {kwota} PLN\n")
                        self.wygrana += kwota
                        if kwota in self.gwarantowane_kwoty:
                            self.gwarantowana_kwota = kwota
                        self.losuj_pytanie()  # Losujemy nowe pytanie po poprawnej odpowiedzi
                        break  
                    else:
                        print(
                            f"Niestety, błędna odpowiedź. Koniec gry. Twoja wygrana to: {self.gwarantowana_kwota} PLN. Do zobaczenia!")
                        exit()  # Zamyka program po błędnej odpowiedzi
                else:
                    print("Nieprawidłowy wybór. Spróbuj ponownie.")

        if not self.pytania:
            print(f"\nGratulacje, {self.imie}! Zdobywasz milion PLN! Do zobaczenia!")

# Uruchomienie gry
gra = Milionerzy()
gra.start()