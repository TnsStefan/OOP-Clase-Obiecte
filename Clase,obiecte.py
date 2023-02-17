# EX 1: Clasa Cerc
#
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
        self.PI = 3.14

    def descrie_cerc(self):
        print(f'Raza cercului este: {self.raza}')
        print(f'Culoarea cercului este: {self.culoare}')

    def aria(self):
        self.aria = self.PI * self.raza ** 2
        return self.aria

    def diametru(self):
        self.diam = self.raza * 2
        return self.diam

    def circumferinta(self):
        return self.diam * self.PI


# EX 2: Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi():

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Lungimea este {self.lungime}!')
        print(f'Latimea este {self.latime}!')
        print(f'Culoarea este {self.culoare}!')

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


# EX 3: Clasa Angajat
#
# Atribute: nume, prenume, salariu
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele anagajatului este {self.nume}')
        print(f'Prenumele anagajatului este {self.prenume}')
        print(f'Salariul anagajatului este {self.salariu}')

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return 12 * self.salariu

    def marire_salariu(self, marire):
        self.salariu = self.salariu + (marire / 100 * self.salariu)


# EX 4: Clasa Cont
#
# Atribute: iban, titular_cont, sold
#
# Constructor pentru toate
#
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)


class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def descriere(self):
        print(f'IBAN-ul dumneavoastra este: {self.iban}')
        print(f'Titularul de cont este: {self.titular_cont}')
        print(f'Aveti urmatorul sold: {self.sold}')

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} !')

    def debitare_cont(self, suma):
        if self.sold >= suma:
            self.sold -= suma
        else:
            print('Fonduri insuficiente')

    def creditare_cont(self, suma):
        self.sold += suma


# EX 5: Clasa Factura
#
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

# pip install tabulate
from datetime import date
from tabulate import tabulate


class Factura:
    SERIA = 123456

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def calc_total(self):
        return self.pret_buc * self.cantitate

    def genereaza_factura(self):
        print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, self.calc_total(), date.today()]],
                       headers=['Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data']))


# EX 6: Clasa Masina
#
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
#
# Constructor: model, viteza_maxima
#
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0

class Masina:
    marca = 'Dacia'
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'rosu', 'verde', 'alb', 'albastru', 'portocaliu', 'negru', 'galben'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Marca masinii este: {self.marca}')
        print(f'Modelul masinii este: {self.model}')
        print(f'Viteza maxima a masinii este: {self.viteza_maxima}')
        print(f'Viteza actuala a masinii este: {self.viteza_actuala}')
        print(f'Culoarea masinii este: {self.culoare}')
        print(f'Masina este inamtriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste_masina(self, noua_culoare):
        if noua_culoare.lower() in self.culori_disponibile:
            self.culoare = noua_culoare.lower()
            print(f'Noua culoare a masinii este: {self.culoare}')
        else:
            print('Culoarea aleasa de dvs nu este in paletarul nostru.')

    def accelereaza(self, viteza_dorita):
        if viteza_dorita < 0:
            print('EROARE!')
        elif viteza_dorita >= self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza_dorita
        print(f'Viteza actuala este: {self.viteza_actuala}')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Viteza actuala este: {self.viteza_actuala}. Am oprit masina.')


# 7
class ToDoList:
    dict = {}

    def adauga_task(self, nume_task, descriere_task):
        self.dict[nume_task] = descriere_task
        print('Am adaugat taskul cu succes')

    def finalizeaza_task(self, nume_task):
        del self.dict[nume_task]

    def afiseaza_todo_list(self):
        print(f'Task-urile din TODO sunt: {self.dict.keys()}')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.dict:
            print(f'Detalii pt taskul {nume_task}: {self.dict[nume_task]}')
        else:
            print('Nu am gasit taskul dorit')
            raspuns = input('Vrei sa adaugi task ul in lista?')
            if raspuns.lower() == 'da':
                descriere_task = input('Introdu descrierea pentru noul task: ')
                self.dict[nume_task] = descriere_task
                print('Am adaugat taskul cu succes')
            elif raspuns.lower() == 'nu':
                print('La revedere!')
