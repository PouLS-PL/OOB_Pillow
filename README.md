
# OOB_Pillow
![Python Version](https://img.shields.io/badge/python-3.x-blue)
![Pillow Version](https://img.shields.io/badge/Pillow-12.1.1-green)
[![Test Pipeline](https://github.com/PouLS-PL/OOB_Pillow/actions/workflows/test-pipeline.yml/badge.svg?branch=ci%2Fadd-test-pipeline)](https://github.com/PouLS-PL/OOB_Pillow/actions/workflows/test-pipeline.yml)

## Opis projektu
Celem projektu jest stworzenie uproszczonego systemu testowania OOB dla modlułu python Pillow z PyPI.
## Testowany moduł
* **Moduł:** [Pillow](https://pypi.org/project/Pillow/) (PIL Fork) – biblioteka do przetwarzania obrazów.
* **Źródło:** PyPI.
* **Wersja:** 12.1.1.

## Automatyzacja i CI (GitHub Actions)

W projekcie wdrożony został system ciągłej integracji (Continuous Integration) oparty o GitHub Actions. Jego głównym celem jest dbanie o to, aby każda zmiana w kodzie była stabilna, bezpieczna i nie psuła dotychczasowego działania aplikacji. Dzięki temu osoba z zewnątrz (oraz nasz zespół) ma pewność, co do jakości kodu bez konieczności jego ręcznego sprawdzania.

### Co uruchamia proces (Workflow Triggers)?
Pipeline uruchamia się automatycznie w dwóch przypadkach:
1. **Każdy Pull Request** skierowany do gałęzi `main` – sprawdzamy kod zanim zostanie scalony.
2. **Każdy bezpośredni Push** do gałęzi `main` – weryfikujemy ostateczny stan głównej wersji projektu.

### Jakie kontrole są wykonywane (Weryfikacja)?
Podczas działania workflow, GitHub Actions uruchamia odizolowane środowisko testowe i wykonuje następujące kroki:
* **Instalacja zależności:** Automatyczne pobranie Pythona oraz biblioteki Pillow w testowanej wersji (12.1.1) z pliku `requirements.txt`.
* **Testy funkcjonalne:** Uruchomienie 6 scenariuszy sprawdzających, czy kluczowe operacje graficzne (np. skalowanie, konwersja formatów) działają poprawnie.
* **Testy wydajnościowe:** Pomiar czasu przetwarzania operacji, aby upewnić się, że nowo dodany kod nie spowalnia działania biblioteki.

---

### Co oznaczają statusy workflow?

#### 🟢 Sukces (Build Passing)
Oznacza, że kod pomyślnie przeszedł wszystkie etapy weryfikacji. Wszystkie testy funkcjonalne zakończyły się wynikiem pozytywnym, wydajność mieści się w normie, a aplikacja jest stabilna i gotowa do bezpiecznego wdrożenia lub dalszego rozwoju.

#### 🔴 Porażka (Build Failing)
Oznacza wykrycie błędu. Najczęstsze przyczyny to:
* Co najmniej jeden test funkcjonalny zakończył się niepowodzeniem (np. funkcja Pillow wygenerowała uszkodzony plik).
* Błąd składniowy w kodzie lub problem z instalacją wymaganych bibliotek.
* Drastyczny spadek wydajności operacji graficznych.

*W przypadku porażki, kod nie powinien być scalany z główną gałęzią (`main`) do momentu naprawienia problemu przez zespół.*
## Struktura projektu

* `docs/` – Dokumentacja projektowa oraz scenariusze testów akceptacyjnych.
* `tests/functional/` – Testy funkcjonalne sprawdzające realne użycie modułu.
* `tests/performance/` – Testy wydajnościowe mierzące czas operacji.
* `tests/assets/` – Zbiór obrazów testowych wykorzystywanych w procesie walidacji.
* `requirements.txt` – Lista zależności niezbędnych do automatycznej instalacji modułu przez pipeline.

## Podział ról
| Członek zespołu | Zadania                                                               | 
| --------------- | --------------------------------------------------------------------- | 
|**@PouLS-PL**     | Testy funkcjonalne, testy wydajnościowe, harmonogram i organizacja.   | 
| **@maupaaa**        | Zarządzanie GitHubem, struktura katalogów, code review, pipeline.     | 
| **@Tymqqq**         | Dokumentacja, scenariusze akceptacyjne, końcowa prezentacja projektu. | 


## Komunikacja
 - **Kanały komunikacji**: Grupa na Facebook Messenger.
 - **Spotkania**: Cotygodniowe podsumowanie postępów w piątki na zajęciach.
## Zasady code review
- Wszystkie zmiany do brancha `main` muszą być dodane przez Pull Requesty.
- Aby Pull Request został zatwierdzony, musi uzyskać pozytywną opinię przynajmniej jednego członka zespołu i wszystkie uwagi powinny być rozwiązane.
- Code review może zrobić każdy członek zespołu, który nie jest autorem Pull Requesta.
- Po stworzeniu Pull Requesta autor informuje na grupie Facebook Messenger, że wymagany jest code review.
## Strategia testowania
Projekt realizuje trzy poziomy weryfikacji:
 - **Testy biblioteki:** Uruchamianie testów jednostkowych dostarczanych przez autorów Pillow (jeśli są dostępne).
 - **Testy funkcjonalne:** 6 scenariuszy sprawdzających kluczowe funkcje (np. konwersja, skalowanie).
 - **Testy wydajnościowe:** Pomiary czasu przetwarzania operacji graficznych i zapis wyników do logów.


> Szczegółowy dokument zawierający scenariusze testów akceptacyjnych wraz z kryteriami zaliczenia znajduje się w pliku: **[scenarios.md](docs/scenarios.md)**.
## Harmonogram projektu
Projekt jest realizowany w czterech etapach. Zgodnie z zasadą „cut-off”, wszystkie zmiany podlegające ocenie muszą być zmergowane do gałęzi main najpóźniej 2 dni przed lekcją oceniającą.

| Etap projektu | Termin | Cut-off (Merge do main) | Zakres prac i Kryteria Ukończenia | Odpowiedzialni |
| :--- | :--- | :--- | :--- | :--- |
| **START: Organizacja** | 17.04.2026 | 15.04.2026 | Założenie repozytorium, pełne README, harmonogram, podział ról, kanały komunikacji i wstępne scenariusze testowe. | @PouLS-PL, @Tymqqq, @maupaaa |
| **Pierwsza Iteracja: Zarządzanie** | 24.04.2026 | 22.04.2026 | Przygotowanie struktury katalogów, aktywne korzystanie z Issues i Pull Requestów, przeprowadzenie Code Review, opracowanie dokumentu ze scenariuszami akceptacyjnymi. | @maupaaa, @Tymqqq |
| **Druga Iteracja: Testowanie** | 08.05.2026 | 06.05.2026 | Działająca pipeline GitHub Actions, implementacja testów funkcjonalnych i wydajnościowych oraz raportowanie wyników. | @PouLS-PL, @maupaaa |
| **RELEASE: Finalizacja** | 22.05.2026 | 20.05.2026 | Kompletna dokumentacja końcowa, prezentacja projektu, samoocena oraz uzasadniony podział punktów w zespole. | @PouLS-PL, @Tymqqq, @maupaaa |

Pełna lista scenariuszy akceptacyjnych znajduje się w pliku [scenarios.md](docs/scenarios.md).

## Instalacja i przygotowanie
Zgodnie z zasadą "działającego minimum", projekt można przygotować do pracy w następujący sposób:

1. Sklonuj repozytorium:

       git clone [https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/OOB_Pillow.git](https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/OOB_Pillow.git)

2. Zainstaluj wymagane biblioteki (Pillow 12.1.1):
    
    pip install -r requirements.txt

