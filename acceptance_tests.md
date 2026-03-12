# Scenariusze testów akceptacyjnych -- Projekt testowania OOB modułu Pillow

## Scenariusz 1 -- Otwarcie obrazu

**Cel testu**
Sprawdzenie, czy biblioteka Pillow umożliwia poprawne otwarcie pliku
graficznego po instalacji z PyPI.

**Opis scenariusza**
Użytkownik uruchamia program wykorzystujący bibliotekę Pillow i próbuje
otworzyć istniejący plik graficzny w formacie PNG znajdujący się w
katalogu projektu.

**Oczekiwany rezultat**
- obraz zostaje poprawnie wczytany przez bibliotekę
- program nie zgłasza błędów podczas otwierania pliku
- możliwe jest odczytanie podstawowych właściwości obrazu (np. rozmiaru)

**Kryterium zaliczenia**
- plik zostaje otwarty bez błędów
- biblioteka zwraca poprawne informacje o wymiarach obrazu

------------------------------------------------------------------------

## Scenariusz 2 -- Konwersja formatu obrazu

**Cel testu**
Sprawdzenie, czy biblioteka Pillow pozwala zapisać obraz w innym
formacie.

**Opis scenariusza**
Użytkownik otwiera obraz w formacie PNG, a następnie zapisuje go w
formacie JPEG przy użyciu funkcji biblioteki.

**Oczekiwany rezultat**
- obraz zostaje zapisany w nowym formacie
- nowy plik pojawia się w katalogu projektu
- plik można ponownie otworzyć przy użyciu biblioteki

**Kryterium zaliczenia**
- plik JPEG istnieje w katalogu projektu
- plik można otworzyć bez błędów

------------------------------------------------------------------------

## Scenariusz 3 -- Zmiana rozmiaru obrazu

**Cel testu**
Sprawdzenie, czy biblioteka Pillow poprawnie zmienia rozmiar obrazu.

**Opis scenariusza**
Użytkownik wczytuje obraz, a następnie zmienia jego rozmiar na mniejszy
(np. połowa szerokości i wysokości).

**Oczekiwany rezultat**
- obraz zostaje przeskalowany
- nowy obraz ma określone wymiary
- operacja przebiega bez błędów

**Kryterium zaliczenia**
- wynikowy obraz ma dokładnie oczekiwane wymiary
- plik wynikowy zostaje poprawnie zapisany
