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
