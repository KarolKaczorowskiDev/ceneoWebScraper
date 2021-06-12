# CeneoScraperN11
## Etap 1 - Pobranie składowych pojedynczej opinii o konkretnym produkcie z serwisu [Ceneo.pl](https://www.ceneo.pl/)
1. Pobranie kodu pojedynczej strony z opiniami o produkcie
2. Analiza struktury kodu pojedynczej opinii

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|:-------|:-----------|:-------------|:---------|
|Opinia|`div.js_product-review`|review|dict|
|Identyfikator opinii|`["data-entry-id"]`|review_id|str|
|Autor opinii|`span.user-post__author-name`|author|str|
|Rekomendacja|`span.user-post__author-recomendation`|recommendation|bool|
|Liczba gwiazdek|`span.user-post__score-count`|stars|float|
|Treść opinii|`div.user-post__text`|content|str|
|Lista zalet|`div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item`<br>`div.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item`<br>`div.review-feature__title--positives ~ div.review-feature__item`|pros|\[str\]|
|Lista wad|`div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item`<br>`div.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item`<br>`div.review-feature__title--negatives ~ div.review-feature__item`|cons|\[str\]|
|Dla ilu osób przydatna|`span[id^="votes-yes"]`<br>`button.vote-yes["data-total-vote"]`<br>`button.vote-yes > span`|useful|int|
|Dla ilu osób nieprzydatna|`span[id^="votes-no"]`<br>`button.vote-no["data-total-vote"]`<br>`button.vote-no > span`|useless|int|
|Czy potwierdzona zakupem|`div.review-pz`|purchased|bool|
|Data wystawienia opinii|`span.user-post__published > time:nth-child(1)["datetime"]`|review_date|str|
|Data zakupu produktu|`span.user-post__published > time:nth-child(2)["datetime"]`|purchase_date|str|

3. Pobranie składowych opinii do pojedynczych zmiennych

## Etap 2 - Pobranie wszystkich opinii z pojedynczej strony
1. Zdefiniowanie słownika do przechowywania składowych pojedynczej opinii
2. Zdefiniowanie listy do przechowywania słowników z opiniami
3. Dodanie pętli wykonującej operację ekstrakcji na wszystkich opiniach z pojedynczej strony

## Etap 3 - Pobrania wszystkich opinii o produkcie
1. Dodanie pętli wykonującej operację ekstrakcji opinii z wszystich stron z opiniami dla danego produtu
2. Wczytywanie kodu produktu z standardowego wejścia
3. Parametryzacja adresy strony z opiniami
4. Eksport opinii o produkcie do pliku .json

## Etap 4 - Analiza pobranych opinii
