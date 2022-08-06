# 1 Entry page

1. W URLS projektu zmieniłem ściezke do URLS aplikacji na /wiki
2. po wpisaniu /wiki/CSS chce sie dostac na te strone. Aby to zrobic musze stworzyc view w aplikacji
   a nastepnie powiazac je z URL. View ma dostac zawartosc danego entry przez wezwanie wlasciwej UTIL funkcji
3. Stworze entry.html, nastepnie view o nazwie entry ktory bedzie zwracal entry.html oraz niezbedne informacje
   z funkcji. Teraz trzeba zajac sie funckjami. Jesli dobrze rozumiem to funkcja save_entry da mi tytul i 
   content ktore bede mogl wstawic do entry.html. Teraz trzeba ten view powiazac z URL. Nie dziala.
4. Uzylem funkcji get_entry ktora zwraca content lub none gdy entry nie istnieje. Jak juz mam content to musze 
   go jakos przetlumaczyc na HTML oraz wpisac title. Title uzyskalem przez przypisanie do klucza
   title z URLS.
5. Aby przetlumaczyc markdown na html, pobralem markdownify przez pip a nastepnie dodalem 
   do aplikacji w settings.py
6. Teraz warunek: jesli entry istnieje to wyswietla sie strona z content, a jestli nie 
   istnieje to wyswietla sie error page. Aby to zrobic stworzylem warunek ktory najpierw
   sprawdza czy title istnieje w liscie(do tego wykorzystalem funkcje ktora zwraca te liste),
   jesli tak to render a jestli nie to HttpResponseNotFound(). Wszystko dziala

# 2 Index page

1. glowna strona, lista ma pozwolic uzytkownikowi na klikniecie i przeniesienie
   na entry page
2. Aby to zrobic, prawdopodobnie to ma byc anchor tag, ktory bedzie przekierowywal na strone
   odpowiadajaca danemy anchorowi.
3. Stworzylem anchor tag i w href nastepuje przekierowanie na /wiki oraz entry, czyli zmienna
   ktora zostaje stworzona podczas loopowania. Ta zmienna odpowiada elementowi w przekazanej liscie
   dlatego dla kazdego zostaje stworzony href prowadzacy do strony odpowiadajacej tej zmiennej

# 3 Search

1. Mam umozliwic uzytkownikowi wpisanie frazy w wyszkuiwarce na pasku bocznym by mogl wyszkukac
   entry. Jesli fraza pasuje do entry to powinien zostac przekierowany na ta strone.
   Jesli nie pasuje to uzytkownik zostaje przekierowany na Search results page ktora wyswietla
   liste dostepnych wejsc ktore zawieraja wyszukiwane slowo i gdy w nie kliknie zostaje przekierowany
2. Do tag form w layout dodalem action do index oraz method post ale wyskakuje CSRF. Aby 
   to ogarnac, dodam do form unikaly CSRF token dla kazdej sesji. Wystarczy dodac {% csrf_token %}
   pod form.
3. Nie dziala, sprobuje stworzyc  django class form. Chodzi o to by uzytkownik wpisal
   a my zbierzemy informacje o wyszukiwaniu w polu tekstowym. Nastepnie dolacze to do contextu
   index view oraz layout.html.
4. A wiec tak, stworzylem klase django form i dodalem ja do view i layout. Potem w index view
   dodalem warunek ktory sprawdza request. Jesli jest POST to do zmiennej form zapisuje 
   zawartosc tego co wpisal uzytkownik. Nastepnie sprawdzamy czy uzytkownik rzeczywiscie wpisal 
   odpowiednia fraze, jesli tak to zapisuje do zmiennej search to co zostalo wpisane i przekierowuje uzytkownkika
   na odpowiednia strone jesli fraza pasuje do entry. Jesli zawartosc tego co wpisal pasuje do
   skladni entries, to zabieram go na Search Result Page na ktorej zostana wyswietlone
   entries posiadajace to co wpisal.
5. Aby wyswietlic mu wyniki wyszukiwania, przed przekierowaniem na search result page, wykonuje
   petle ktora sprawdza czy raza pasuje do jakichs entry, jesli tak to zostaja zapisane w 
   nowej liscie. Nowa lista jest przekazywana na strone razem z uzytkownikim i wyswietlaja sie
   dostepne entries.

# 4 New Page

1. Na bocznym pasku ma znajdowac sie link ktory prowadzi do strony na ktorej uzytkownik moze 
   stworzyc wlasna strone. Znajduje sie tam input dla tytulu i textarea dla contentu w Markdown.
   Znajduje sie rowniez button do zapisania strony. Jesli entry z zapewnionym tytulem juz istnieje
   powinien wyskoczyc error, jesli nie to entry powinno zostac zapisane i przekierowac uzytkownika na
   nowa strone.
2. Czyli tak, prawdopodobnie trzeba stworzyc nowa klase ktora bedzie form. Dziki temu bedziemy
   mogli zapisac to co wpisal uzytkownik w tytule i przeloopowac liste istniejacych entries by 
   sprawdzic czy juz taka istnieje. Jesli istnieje to error message. Jesli nie, to strona zostaje
   zapisana a uzytkownik przekierowany na nowa strone. 
3. Mam funckje ktora zapisuje entry gdy dostanie jej tytul i content dlatego ja wykorzystam.
   Najpierw stworze klase z dwoma inputami. Stworzylem klase, gdy uzytkownik wpisze tytul ktory istnieje
   to wyskoczy mu tekst. Teraz druga czesc. Problem jest taki ze gdy uzytkownik doda poprawnie 
   to stworzy mi to dodatkowe entry ale w folderze a chce zeby dla kazdego tworzylo sie osobno
   dlatego nalezy ogarnac sessions. Moglbym zrobic tak ze tworze pusta liste dla session ktora przechowa 
   title, a nastepnie doda ten title do istniejacej juz listy entries.
4. W zadaniu pisze ze ma sie zapisywac ale na dysku wiec nwm czy session. 

# 5 Edit Page

1. Na kazdej entry stronie uzytkownik ma miec mozliwosc klikniecia linku ktory zabierze go 
   na strone do edytowania danego entry contentu w textarea. Textarea ma byc wypelniona zawartoscia
   Uzytkownik powinien moc zapisac zmiany ktore popelnil. Gdy uzytkownik kliknie zapisz, ma byc
   zabrany z powrotem na zapisana strone.
2. Do kazdej strony entries dodalem link. Teraz trzeba stworzy view i urls. Strona bedzie wygladala tak
   ze tytul bedzie edit page oraz bedzie miala textarea z przyciskiem. Ta textarea bedzie klasa.
3. Problem jest taki ze nie mam jak wziac tytulu bo gdy bede mial tytul to zdobede content.
   Mysle nad stworzeniem sciezki dla kazdego entry
4. Zrobilem tak ze dodalem sciezke /<title>/edit_page co pozwolilo mi na uzyskanie tytulu oraz dostanie
   sie na strone edytowania. Musialem dodac dodatkowy argument do anchor tag na kazdej stronie entry
   tak aby zawieral title+edit_page(tego brakowalo dlatego nie dzialalo).
5. Wszystko dziala, teraz stworze klase z form ktora bedzie miala zawartosc danego title.
   Sprobuje bez klasy tylko textarea. Dodalem textarea i value dalem jako content ale nie wyswietla sie nic.
   Wyswietla sie jedynie markdownify. Wpisywalem to do value a wystarczylo miedzy >< jako zawartosc.
   Teraz gdy uzytkownik dokona zmian i kliknie button by zapisac zmiany, powinien zostac przekierowany z powrotem
   na strone ze zmienionym entry.
6. Wiem jak przekazac initial value do textarea ale nie wiem jak to zrobic z class.
7. Poki co zajalem sie tym aby moc edytowac entry. Uzylem funkcji ktora bierze title i content
   i podmienia wartosci. Dziala, uzytkownik wchodzi w entry, klika edit page i zostaje przekierowany
   na strone do edytowania ale brakuje tutaj zawartosci.
8. DZIALA! Jak to zrobilem aby ustawic initial value danej form? Najpierw stworzylem zmienna(initial_data) wewnatrz
   view(w tym przypadku new_page) ktora zawiera dictionary. Kluczem jest nazwa pola do wypelnienia form
   (w tym przypadku new_content) a value to funkcja get_entry(title) ktora zwraca zawartosc entry.
   Nastepnie do renderowanej formy w nawias wrzucilem initial=initial_data. Po zapisaniu forma renderuje
   zawartosc. Uzytkownik edytuje w Markdown language i gdy zapisze, przenosi sie na strone z danym entry
   wraz z edytowana zawartoscia wyswietlana w HTML

# 6 Random page

1. Gdy uzytkownik kliknie link Random Page, zostaje zabrany na losowe entry. 
2. Mozna stworzyc funkcje ktora wykorzysta HttpResponseRedirect z losowym entry. Nalezaloby
   stworzyc zmienna ktora przyjmie losowa wartosc z listy entries.
3. Najpierw dodalem link ktory zabiera do sciezki url random_page. URL rando_page wywoluje funkcje view
   random_page ktora tworzy zmienna zawierajaca tytuly entries, Potem tworzy zmienna title
   i przypisuje do niej losowy element z listy, nastepnie zwracana jest HttpResponseRedirect
   zawierajaca /wiki/title, czyli losowa zmienna z listy.
4. Uzytkownik klika przycisk i dziala.

