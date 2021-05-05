# CeneoScrapper
## Etap 1
### 1. analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl)
|składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion|obiekt bs4.element.Tag|
|ID opinii["data-entry-id"]|opinion_id|str|
|Autor|span.user-post_author-name|author|str|
|Rekomendacja|span.user-post__author-recomendation > em|recomendation|bool|
|Liczba gwiazdek|span.user-post__score-count|stars|float|
|Treść opinii|div.use-post_text|content|str|
|Lista zalet|div.review-feature_col:has(>div[class*="possitives"])>div.review-feature_item|pros|list|
|Lista wad|div.review-feature_col:has(>div[class*="negatives"])>div.review-feature_item|cons|list|
|Czy potwierdzono zakupem|div.review-pz|purchased|bool|
|Data wystawienia opinii|span.user-post_published > time:nth-child(1)["datetime"]|submit_date|str|
|Data zakupu produktu|span.user-post_published > time:nth-child(2)["datetime"]|purchase_date|str|
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful|int|
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|int|


### 2. pobranie składowych pojedynczych opiii
- pobranie kodu pojedynczej strony z opiniami
- wyodrębnienie z kodu strony pojedynczej opinii
- pobranie do pojedynczych zmiennych poszczególnych składowych na podstawie selektorów
- obsługa błędów
- dobranie typów danych do wartości zmiennych


### Etap 2. Ekstrakcja wszystkich opinii o produkcie z pojedynczej strony
- zapis składowych pojedynczej opinii do słownika
- zdefiniowanie listydo przechowywania wszystkich opinii o danym produkcie
- dodanie pętli, która wykonuje operację ekstracji dla wszystkich opinii pobranych z pojedynczej strony
-
### Etap 3. Ekstrakcja wszystkich opinii o produkcie z wszystkich stron
- dodanie pętli, która pobiera i analizuje kolejne strony z opiniami o produkcie
- dodanie możliwości podania kodu produktu "z klawiatury"
- dodanie zapisu wszystkich opinii o produkcie do pliku .json

### Etap 4. Refactoring
- zdefiniowanie funkcji do ekstrakcji pojedynczego elementu opinii
- przygotowanie słownika opisującego składowe opinii wraz z ich selektorami
- tworzenie słownika reprezentującego pojedyncząopinię przy wykorzstaniu wyrażenia słownikowego (dictionary comprehension)

### Etap 5
- wyświetlenie listy produktów, dla których pobrane zostały opinie
- wczytanie opinii o wskazanym produkcie do obiektu DataFrame
- obliczenie podstawowych statystyk
    * średnia ocena produktu
    * liczba opinii o produkcie
    * liczba opinii dla których podana została liczba zalet
    * liczba opinii dla których podana została liczba wad

### Etap 6 Rysowanie wykresów opartych o dane z pobranych opinii
- wykres słupkowy/kolumnowy obrazujący częstość występowania opinii z poszczególnymi ocenami
- wykres kołowy obrazujący udział poszczególnych rodzajów rekomendacji w zbiorze opinii