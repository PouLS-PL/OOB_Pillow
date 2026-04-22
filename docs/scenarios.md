# Wstępne Scenariusze Testowe Projektu

### Lista Scenariuszy Testowych

| ID | Nazwa testu | Opis | Warunki wstępne | Czynności testowe | Spodziewane rezultaty |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PT-01** | **Walidacja konwersji JPEG->PNG** | Weryfikacja poprawności konwersji z formatu JPEG do formatu PNG. Sprawdzenie zachowania wymiarów. | Obraz testowy w formacie `.jpeg` | 1. Załaduj plik wejściowy <br> 2. Wywołaj funkcję `convert_format` <br> 3. Zweryfikuj typ MIME pliku <br> 4. Porównaj wymiary | Plik wyjściowy ma format PNG i zachowuje wymiary oryginału. |
| **PT-02** | **Skalowanie obrazu (resize)** | Weryfikacja przeliczania pikseli podczas zmiany rozmiaru pliku. | Obraz testowy 1000x1000px | 1. Załaduj plik wejściowy <br> 2. Wykonaj `resize((500,500))` <br> 3. Sprawdź wartość `.size` | Wartość `.size` zwraca dokładnie (500, 500). Obraz nie jest uszkodzony. |
| **PT-03** | **Konwersja barw (RGB->L)** | Weryfikacja zmiany trybu koloru na czarno-biały (Grayscale). | Obraz kolorowy w formacie RGB | 1. Załaduj plik wejściowy <br> 2. Użyj metody `.convert('L')` <br> 3. Sprawdź atrybut `.mode` | Obraz jest czarno-biały - atrybut `.mode` ma wartość 'L'. |
| **PT-04** | **Generowanie miniatury** | Test metody `thumbnail()`, która modyfikuje obiekt w miejscu. | Obraz prostokątny (np. 1200x800 px) | 1. Załaduj plik <br> 2. Wywołaj `img.thumbnail((400, 400))` <br> 3. Sprawdź wymiary | Dłuższy bok ma 400 px, krótszy bok przeskalowany proporcjonalnie. |
| **PT-05** | **Nakładanie filtrów** | Weryfikacja poprawności modyfikacji macierzy przy użyciu filtrów. | Obraz testowy `input.jpg` | 1. Załaduj plik wejściowy <br> 2. Wywołaj `filter(GaussianBlur)` | Plik ma inną sumę kontrolną niż oryginał. Widoczne rozmycie. |
| **PT-06** | **Kadrowanie (Crop)** | Weryfikacja wycinania fragmentu obrazu na podstawie współrzędnych. | Obraz o znanych wymiarach | 1. Wywołaj `crop((x0, y0, x1, y1))` <br> 2. Sprawdź wymiary wycinka | Wymiary wycinka zgadzają się z zadanymi współrzędnymi. |

---

### Uwagi Techniczne
* **Środowisko:** Testy powinny być przeprowadzane przy użyciu biblioteki Pillow (PIL).
* **Zestaw danych:** Wszystkie obrazy testowe powinny znajdować się w folderze `/tests/assets/`.
* **Kryteria akceptacji:** Wszystkie testy muszą zakończyć się statusem PASS przed przejściem do fazy wdrożenia.
