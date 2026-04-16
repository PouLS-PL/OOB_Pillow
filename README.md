# OOB_Pillow
## Opis projektu
Celem projektu jest stworzenie uproszczonego systemu testowania OOB dla modlułu python Pillow z PyPI.
## Testowany moduł
- Modułu: Pillow
- Źródło: PyPI
- Testowana wersja: 12.1.1
## Strategia testowania
### Testy biblioteki
Gotowe testy biblioteki są uruchamiane w pipeline. Ich celem jest sprawdzenie, czy biblioteka działa poprawnie w środowisku przygotowanym przez pipeline.
### Testy funkcjonalne
Testy, które sprawdzają realne i kluczowe funkcjonalności biblioteki.
Mogą obejmować:
- sprawdzenie działania podstwawowych funkcji biblioteki
- weryfikację poprawności wyników dla przykładowych danych
- testowanie typowych scenariuszy użycia
### Testy wydajnościowe
Mierzą czas wykonania oberacji.
## Podział ról
| Członek zespołu | Zadania                                                               | 
| --------------- | --------------------------------------------------------------------- | 
| @PouLS-PL       | Testy funkcjonalne, testy wydajnościowe, harmonogram i organizacja.   | 
| @maupaaa        | Zarządzanie GitHubem, struktura katalogów, code review, pipeline.     | 
| @Tymqqq         | Dokumentacja, scenariusze akceptacyjne, końcowa prezentacja projektu. | 
# Wstępne Scenariusze Testowe Projektu

### Lista Scenariuszy Testowych

| ID | Nazwa testu | Opis | Warunki wstępne | Czynności testowe | Spodziewane rezultaty | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PT-01** | **Walidacja konwersji JPEG->PNG** | Weryfikacja poprawności konwersji z formatu JPEG do formatu PNG. Sprawdzenie zachowania wymiarów. | Obraz testowy w formacie `.jpeg` | 1. Załaduj plik wejściowy <br> 2. Wywołaj funkcję `convert_format` <br> 3. Zweryfikuj typ MIME pliku <br> 4. Porównaj wymiary | Plik wyjściowy ma format PNG i zachowuje wymiary oryginału. | ⏳ TO-DO |
| **PT-02** | **Skalowanie obrazu (resize)** | Weryfikacja przeliczania pikseli podczas zmiany rozmiaru pliku. | Obraz testowy 1000x1000px | 1. Załaduj plik wejściowy <br> 2. Wykonaj `resize((500,500))` <br> 3. Sprawdź wartość `.size` | Wartość `.size` zwraca dokładnie (500, 500). Obraz nie jest uszkodzony. | ⏳ TO-DO |
| **PT-03** | **Konwersja barw (RGB->L)** | Weryfikacja zmiany trybu koloru na czarno-biały (Grayscale). | Obraz kolorowy w formacie RGB | 1. Załaduj plik wejściowy <br> 2. Użyj metody `.convert('L')` <br> 3. Sprawdź atrybut `.mode` | Obraz jest czarno-biały - atrybut `.mode` ma wartość 'L'. | ⏳ TO-DO |
| **PT-04** | **Generowanie miniatury** | Test metody `thumbnail()`, która modyfikuje obiekt w miejscu. | Obraz prostokątny (np. 1200x800 px) | 1. Załaduj plik <br> 2. Wywołaj `img.thumbnail((400, 400))` <br> 3. Sprawdź wymiary | Dłuższy bok ma 400 px, krótszy bok przeskalowany proporcjonalnie. | ⏳ TO-DO |
| **PT-05** | **Nakładanie filtrów** | Weryfikacja poprawności modyfikacji macierzy przy użyciu filtrów. | Obraz testowy `input.jpg` | 1. Załaduj plik wejściowy <br> 2. Wywołaj `filter(GaussianBlur)` | Plik ma inną sumę kontrolną niż oryginał. Widoczne rozmycie. | ⏳ TO-DO |
| **PT-06** | **Kadrowanie (Crop)** | Weryfikacja wycinania fragmentu obrazu na podstawie współrzędnych. | Obraz o znanych wymiarach | 1. Wywołaj `crop((x0, y0, x1, y1))` <br> 2. Sprawdź wymiary wycinka | Wymiary wycinka zgadzają się z zadanymi współrzędnymi. | ⏳ TO-DO |

---

### Uwagi Techniczne
* **Środowisko:** Testy powinny być przeprowadzane przy użyciu biblioteki Pillow (PIL).
* **Zestaw danych:** Wszystkie obrazy testowe powinny znajdować się w folderze `/tests/assets/`.
* **Kryteria akceptacji:** Wszystkie testy muszą zakończyć się statusem PASS przed przejściem do fazy wdrożenia.

---

## Komunikacja
- Grupa na Facebook Messenger
- Omówienie postępów i kolejnych etapów projektu co tydzień w piątki na zajęciach
## Harmonogram projektu
Projekt jest realizowany w czterech etapach. Zgodnie z zasadą „cut-off”, wszystkie zmiany podlegające ocenie muszą być zmergowane do gałęzi main najpóźniej 2 dni przed lekcją oceniającą.

| Etap projektu | Termin | Cut-off (Merge do main) | Zakres prac i Kryteria Ukończenia | Odpowiedzialni |
| :--- | :--- | :--- | :--- | :--- |
| **START: Organizacja** | 17.04.2026 | 15.04.2026 | Założenie repozytorium, pełne README, harmonogram, podział ról, kanały komunikacji i wstępne scenariusze testowe. | @PouLS-PL, @Tymqqq, @maupaaa |
| **Pierwsza Iteracja: Zarządzanie** | 24.04.2026 | 22.04.2026 | Przygotowanie struktury katalogów, aktywne korzystanie z Issues i Pull Requestów, przeprowadzenie Code Review, opracowanie dokumentu ze scenariuszami akceptacyjnymi. | @maupaaa, @Tymqqq |
| **Druga Iteracja: Testowanie** | 08.05.2026 | 06.05.2026 | Działająca pipeline GitHub Actions, implementacja testów funkcjonalnych i wydajnościowych oraz raportowanie wyników. | @PouLS-PL, @maupaaa |
| **RELEASE: Finalizacja** | 22.05.2026 | 20.05.2026 | Kompletna dokumentacja końcowa, prezentacja projektu, samoocena oraz uzasadniony podział punktów w zespole. | @PouLS-PL, @Tymqqq, @maupaaa |
