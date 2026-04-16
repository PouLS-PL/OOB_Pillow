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
