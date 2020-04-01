# -*- coding: utf-8 -*-
from sys import exit
import os



# funkcja tekst otwiera pliki tekstowe wskazane jako argument i wyświetla użytkownikowi
def tekst(x):
	f = open(x, 'r')
	txt = f.read()
	print
	print "\n", txt, "\n"

def clear_screen():
	import os
	os.system('clear')

# mechaniki dupa
# fala
def eq():
	print "\nEkwipunek:"
	for i in equipment:
		print " -", i
	print "\n"

def dead(why):
	print why, "\nKoniec gry. Przegrałeś."
	exit(0)

# LOKACJE

def bimbrownik():
	clear_screen()
	tekst("teksty/bimber_polski.txt")
	while True:

		start = raw_input("> ")

		if start == "1":
			clear_screen()
			cela_start()
			break

		elif start == "2":
			clear_screen()
			exit(0)

		else:
			print "Może jednak nie jest to takie proste..."

def cela_start():
	tekst("teksty/wstęp.txt")
	choice = """
1) Podchodzę do drzwi i próbuje je otworzyć
2) Idę do wychodka spuścić z zawora
3) Ubieram swoje rzeczy
4) Nie robie nic czekając na rozwój wydarzeń\n
"""

	kamien = False

	while True:
		print c, choice

		next = raw_input("> ")

		clear_screen()

		if next == "1" and not kamien and not "drut" in equipment:
			print "\nDrzwi są solidne i jak można było się domyślić - zamknięte.\nCzego żeś się psia jego mać spodziewał?"

		elif next == "1" and kamien and not "drut" in equipment:
			print """
Kamień wskazany w wychodku wygląda na obluzowany.
Widać wnętrze zamka. Nie masz jednak czym do niego sięgnąć.
"""

		elif next == "1" and not kamien and "drut" in equipment:
			print """
Stoisz jak młot z drutem w ręku i opadającymi z dupy spodniami.
Od strony celi nie ma jednak żadnego otworu.
"""


		elif next == "1" and kamien and "drut" in equipment:
			print """
Kamień wskazany w wychodku jest obluzowany. Udaje Ci się go wyjąć.
Dzięki drutowi znalezionemu w bacioku udaje ci się dostać do odsłoniętego wnętrza zamka i otworzyć drzwi.
Wygląda na to że nikogo nie ma w pobliżu.
"""
			print "\nCzy chcesz wyjść z celi?\n1) Tak\n2) Nie\n"

			open = raw_input("> ")

			clear_screen()

			if open == "1":
				notatki.append("list do siebie")
				korytarz_cela()
				break

			elif open == "2":
				print "Uznałeś że lepiej poczekać."
			else:
				print "Nie rozumiem."



		elif next == "2" and not kamien:
			print """\nMusisz skorzystać z wychodka.
To zrozumiałe zważywszy na ilość płynów przyjętych zeszłej nocy.
Podczas oddawania moczu zauważyłeś wyryty na ścianie rysunek wskazujący na
jeden z kamieni przy drzwiach celi. Może wypadało by to sprawdzić.
"""
			kamien = True


		elif next == "2" and kamien:
			print "Już się załatwiłeś.\nIle można?"


		elif next == "3" and not "drut" in equipment:
			print """
Podnosisz z ziemi swoje rzeczy.
Nowością to one nie pachną lecz w tej sytuacji nie ma co narzekać.
I tak Cie nikt wąchać nie będzie.
Podczas ubierania swoich starych dobrych, wysłużonych gumofilców coś cię uwarło.
Okazało się że jakimś cudem znalazł się tam kawałek drutu.
To by wyjaśniało ból lewej stopy.
"""
			equipment.append("drut")


		elif next == "3" and "drut" in equipment:
			print "\nJeszcze nie wytrzeźwiałeś?\nPrzecież przed chwilą się ubrałeś."

		elif next == "4":
			print "\nCzekasz 5 minut, 10 minut.\nNic sie nie dzieje.\n"

		else:
			print "\nNie rozumiem.\n"

def korytarz_cela():

	clear_screen()

	choice_1 = """
1) Wchodzę do sali tortur.
2) Próbujesz otworzyć celę obok.
3) Zakradam się bliżej wyjścia.
"""

	shit_1 = "wiadro z gownem"

	if "korytarz_cela" not in virtual:
		tekst("teksty/korytarz_cela.txt")
		virtual.append("korytarz_cela")

	elif "korytarz_cela" in virtual:
		print "Wróciłeś pod swoją cele."


	while True:

		print c
		print choice_1

		next = raw_input("> ")

		clear_screen()

		if next == "1":
			sala_tortur()
			break


		elif next == "2" and not "klucze straznika" in equipment:
			print "\nPróbujesz pociągnąć za kalmkę lecz drzwi są zamknięte.\nCzuć tylko potworny smród."

		elif next == "2" and "klucze straznika" in equipment:

			print """
Udaje Ci się otworzyć drzwi.
W środku ku twojemu zaskoczeniu znajduje się jedynie wiadro z gównem.
- Co do chuja!? - zamruczałeś pod nosem
"""
			print "Czy chcesz zabrać je ze sobą?\n1) Tak\n2) Nie"

			wiadro = raw_input("> ")

			clear_screen()

			if wiadro == "1":
				equipment.append(shit_1)
				print """
- Może się przyda - pomyślałeś.
Zabrałeś je więc ze sobą i wróciłeś na korytarz
"""

			elif wiadro == "2":
				print """A na cholere mi wiadro z gównem psia jego mać - zamruczałeś pod nosem i wróciłeś na korytarz."""

			else:
				print "Nie rozumiem."


		elif next == "3":
			print "\nPodchodzisz bliżej wyjścia."
			korytarz_cela_2()
			break

		else:
			print "\nNie rozumiem"

def korytarz_cela_2():

	clear_screen()

	choice_1 = """
1) Zakradam się do celi Gwizdacza
2) Zakradam się do spiżarni
3) Cofam się pod swoją celę
4) Atakuje strażnika
"""
	choice_2 = """
1) Idę do celi Gwizdacza
2) Idę do spiżarni
3) Cofam się pod swoją celę
4) Wychodzę z piwnicy
"""

	if "korytarz_cela_2" not in virtual:
		virtual.append("korytarz_cela_2")
		print """
Udało ci się podkraść bliżej wyjścia.
Po lewej stronie widzisz kolejną cele,
w której ktoś wygwizduje dźwięki znanej ci dobrze międzynarodówki.
Z prawej natomiast prawdopodobnie znajduje się spiżarnia.
Przed tobą natomiast schody wychodzące z piwnicy.
"""
	elif "korytarz_cela_2" in virtual:
		print "Jesteś na środku korytarza."

	else:
		print "\n"

	guard_keys_1 = "klucze straznika"

	gwizdacz = False

	while True:


		if guard_keys_1 not in equipment:
			print c, choice_1

		elif guard_keys_1 in equipment:
			print c, choice_2

		next = raw_input("> ")

		clear_screen()

		if next == "1":
			cela_gwizdacza()

		elif next == "2":
			print "Wchodzisz do spiżarni."
			spizarnia_1()
			break

		elif next == "3":
			korytarz_cela()
			break

		elif next == "4" and guard_keys_1 not in equipment and "palka" not in equipment:
			print "strażnik cię zabija"
			dead("Zaatakowałeś strażnika bez broni. Pokonuje cię ")

		elif next == "4" and guard_keys_1 not in equipment and "palka" in equipment:
			print "Walczysz z strażnikiem, ogłuszasz go pałką i zabierasz klucze"
			equipment.append(guard_keys_1)

		elif next == "4" and guard_keys_1 in equipment:
			print """
Wychodząc spoglądasz na stanowisko strażnika.
Widzisz świerszczyki
- to pewnie dlatego tak sapał
CZy chcesz zabrać plakat z gołą babą?
1) Tak
2) Nie
"""
			plakat = raw_input("> ")

			clear_screen()
			if plakat == "1":
				print "wyrywasz gołą babę ze środka i uciekasz z więzienia"
				schody_cela_1()
				break

			elif plakat == "2":
				print "Na cholere mi goła baba. odwracesz się i uciekasz z piwnicy."
				schody_cela_1()
				break

			else:
				"Nie rozumiem"

		else:
			"Nie rozumiem."

def cela_gwizdacza():

	global gwizdacz



	if "cela_gwizdacza" not in virtual and "klucze straznika" not in equipment and "gwizdacz_negative" not in virtual:

		print """
Podchodzisz bliżej drzwi i wsuwasz swój zapity, purpurowy nos między kraty w okienku.
W środku panuje mrok, ale udaje ci się dostrzec zarys jakiejś postaci.
Wygląda na to, że ona również cię zauważa, bo przerywa swoje gwizdania i zwraca się do ciebie.
- Ключ. Идиот имеет ключ. - szepnął do ciebie niezrozumiale po kacapsku.
Twoje zrozumienie rosyjskiego wraz z edukacją skończyło się jednak trzeciej klasie podstawówki,
ale chyba chce żeby go wypuścić.
"""
		virtual.append("cela_gwizdacza")

	elif "cela_gwizdacza" not in virtual and "klucze straznika" in equipment and "gwizdacz_negative" not in virtual:

		print """
Podchodzisz bliżej drzwi i wsuwasz swój zapity, purpurowy nos między kraty w okienku.
W środku panuje mrok, ale udaje ci się dostrzec zarys jakiejś postaci.
Wygląda na to, że ona również cię zauważa, bo przerywa swoje gwizdania i zwraca się do ciebie.
- Ключ. Идиот имеет ключ. - szepnął do ciebie niezrozumiale po kacapsku.
Twoje zrozumienie rosyjskiego wraz z edukacją skończyło się jednak trzeciej klasie podstawówki,
ale chyba chce żeby go wypuścić."""

		virtual.append("cela_gwizdacza")

		print "\nMasz klucze do celi czy chcesz wypuścić Gwizdacza?\n1) Tak\n2) Nie\n"
		open = raw_input("> ")

		clear_screen()

		if open == "1":
			print "спасибо товарищ"

			NPC.append("Gwizdacz")

		elif open == "2":
			print "Poczekaj, jeszcze cię dopadnę!!"

			virtual.append("gwizdacz_negative")

		else:
			"Nie rozumiem."



	elif "cela_gwizdacza" in virtual and "klucze straznika" not in equipment and "gwizdacz_negative" not in virtual:
		print "ключ дай мне ключ - fuknął zdenerwowany więzień"

	elif "klucze straznika" in equipment and "Gwizdacz" not in NPC and "gwizdacz_negative" not in virtual:

		print "Masz klucze do celi czy chcesz wypuścić Gwizdacza?\n1) Tak\n2) Nie"
		open_1 = raw_input("> ")

		clear_screen()

		if open_1 == "1":
			print """
спасибо товарищ - rzucił w twoją stronę więzień.
Po czym wyskoczył z celi jak poparzony i zniknął w ciemnym korytarzu prowadzącym do wyjścia.
"""

			NPC.append("Gwizdacz")

		elif open_1 == "2":
			print "Poczekaj, jeszcze cię dopadnę!!"

			virtual.append("gwizdacz_negative")

		else:
			"Nie rozumiem."

	elif "klucze straznika" in equipment and "Gwizdacz" not in NPC and "gwizdacz_negative" in virtual:
		print "однако вы передумали? - wybełkotał więzieź"
		print "1) Tak - otwórz więźnia\n2) Nie - odejdź"

		open_2 = raw_input("> ")

		clear_screen()

		if open_2 == "1":
			print "спасибо товарищ"

			NPC.append("Gwizdacz")

		elif open_2 == "2":
			print "Poczekaj, jeszcze cię dopadnę!! - krzyknął więzień"

		else:
			"Nie rozumiem."

	elif "Gwizdacz" in NPC:
		print "Cela jest pusta Wypuściłeś zakapiora"

def sala_tortur():

	clear_screen()

	virtual.append("sala_tortur")
	print "\nOstrożnie odchyliłeś drzwi i wszedłeś do sali tortur."
	print """Wszystko tutaj cuchnie juchą"""
	choice = """
1) Zabieram pałkę
2) Wychodzę
"""

	while True:

		print c, choice

		next = raw_input("> ")

		clear_screen()

		if next == "1" and "palka" not in equipment:
			equipment.append("palka")
			print "Całkiem niezła pała"

		elif next == "1" and "palka" in equipment:
			print "Już zabrałeś"

		elif next == "2":
			korytarz_cela()
			break

		else:
			print "Nie rozumiem."

def spizarnia_1():

	clear_screen()
	if "spizarnia_1" not in virtual:
		tekst("teksty/spizarnia_1.txt")
		virtual.append("spizarnia_1")
	else:
		print "Jesteś w spiżarni."

	choice_1 = """
1) Wracam na korytarz
2) Próbuje dobrać się do beczki.
3) Urządzam sobie uczte z przetworów
"""

 	choice_2 = """
1) Wracam na korytarz
2) Próbuję dobrać się do beczki
3) Urządzam sobie ucztę z przetworów
4) Rozlej zawartość wiadra na zapasy
5) Wlej zawartość wiadra do beczki z winem
"""


	while True:

		if "wiadro z gownem" in equipment:
			print c, choice_2

		else:
			print c, choice_1


		next = raw_input("> ")

		clear_screen()

		if next == "1":
			korytarz_cela_2()
			break

		elif next == "2" and "klucze straznika" not in equipment:
			dead("Strażnik usłyszał twoje zapasy z beczką po czym zastrzelił cię bez ostrzeżenia.")

		elif next == "2" and "klucze straznika" in equipment and not "wypite_cela" in virtual :
			print """
Szarpanina z beczką potrwała chwilę nim udało Ci się dostać do jej zawartości
Z racji na to że kac po wczorajszym jeszcze nie minął bla bla bla """
			virtual.append("wypite_cela")

		elif next == "2" and "klucze straznika" in equipment and "wypite_cela" in virtual:
			print "Przypomniało Ci się dlaczego za winem nie przepadasz.\nJeszcze człowiek nic we łbie nie poczół a żołądek pełen"

		elif next == "3" and "klucze straznika" not in equipment:
			dead("zostajesz złapany")
		elif next == "3" and "klucze straznika" in equipment and not "jedzenie_cela" in virtual and not "wiadro_zapasy" in virtual:
			print "Głodny jak wilk rzucasz się na słoiki pochłaniając wszystko."
			virtual.append("jedzenie_cela")

		elif next == "3" and "klucze straznika" in equipment and "jedzenie_cela" in virtual and not "wiadro_zapasy" in virtual:
			print "Obrzarłeś się jak świnia. Nie zmieścisz już więcej."

		elif next == "3" and "wiadro_zapasy" in virtual:
			print "Właśnie rozlałeś gówno na zapasy.\nJesteś pewien że chcesz to jeść?"
			print "1) Tak\n2) Za żadne skarby."
			shit_meal = raw_input(">")

			clear_screen()

			if shit_meal == "1":
				dead("Zjadłeś czyjeś gówno ty chory pojebie. Nie żyjesz. Gratulacje!!")

			elif shit_meal == "2":
				print "Tak myślałem. To był strasznie głupi pomysł."

		elif next == "4" and "wiadro z gownem" not in equipment:
			print "Nie rozumiem."

		elif next == "4" and "wiadro z gownem" in equipment:
			print "Niszczysz zapasy rozlewając na nie gówno"
			equipment.remove("wiadro z gownem")
			virtual.append("wiadro_zapasy")

		elif next == "5" and "wiadro z gownem" not in equipment:
			print "Nie rozumiem."

		elif next == "5" and "wiadro z gownem" in equipment:
			print """
Czyś ty się z chujem na głowy pozamieniał?
Dżentelmenowi tkiemu jak ty nie wypada niszczyć dobrego trunku.
Niby to wino, ale jakby nadal alkohol.
"""
		else:
			print "Nie rozumiem."

def schody_cela_1():
	clear_screen()
	print virtual
	del virtual[:]
	print equipment, NPC, notatki
	print "wychodzisz z piwnicy."




c = "\nCo robisz?"

# listy

equipment = []

nafta = []

notatki = []

bimber =[]

NPC =[]

virtual = []


bimbrownik()
