# CeneoScrapper
## Etap 1
### 1. analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl)
|składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.user-post user-post__card js_product-review|opinion||
|ID opinii["data-entry-id"]|opinion_id||
|Autor|span.user-post_author-name|author||
|Rekomendacja|span.user-post__author-recomendation > em|recomendation||
|Liczba gwiazdek|span.user-post__score-count|stars||
|Treść opinii|div.use-post_text|content||
|Lista zalet|div.review-feature_col:has(>div[class*="possitives"])>div.review-feature_item|pros||
|Lista wad|div.review-feature_col:has(>div[class*="negatives"])>div.review-feature_item|cons||
|Czy potwierdzono zakupem|div.review-pz|purchased||
|Data wystawienia opinii|span.user-post_published > time:nth-child(1)["datetime"]|submit_date||
|Data zakupu produktu|span.user-post_published > time:nth-child(2)["datetime"]|purchase_date||
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful||
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless||


### 2. pobranie składowych pojedynczych opiii
- pobranie kodu pojedynczej strony z opiniami
- wyodrębnienie z kodu strony pojedynczej opinii
- pobranie do pojedynczych zmiennych poszczególnych składowych na podstawie selektorów