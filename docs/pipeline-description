
Repozytorium wykorzystuje narzędzie GitHub Actions do automatyzacji procesów Continuous Integration (CI). Zaimplementowany workflow odpowiada za uruchamianie testów funkcjonalnych, wydajnościowych, statyczną analizę kodu oraz agregację wyników.

## 1. Wyzwalacze (Triggers)

Workflow jest uruchamiany automatycznie lub manualnie w następujących przypadkach:

-   **Push:** Każde przesłanie zmian bezpośrednio do gałęzi `main`.
    
-   **Pull Request:** Utworzenie lub aktualizacja żądania zmian (PR) skierowanego do gałęzi `main`.
    
-   **Workflow Dispatch (Manualny):** Ręczne uruchomienie z poziomu zakładki _Actions_ w interfejsie GitHub.
    

### Parametry uruchomienia manualnego

Podczas ręcznego wyzwalania użytkownik ma możliwość zdefiniowania parametru wejściowego `test_level`:

-   `all` (domyślny): Uruchamia pełen zestaw testów.
    
-   `functional`: Uruchamia wyłącznie etap testów funkcjonalnych.
    
-   `performance`: Uruchamia wyłącznie etap testów wydajnościowych.
    

## 2. Architektura i Zadania (Jobs)

Workflow składa się z trzech odrębnych zadań wykonywanych na środowisku uruchomieniowym `ubuntu-latest`:

### 2.1. Functional Tests (`functional-tests`)

Zadanie odpowiedzialne za weryfikację poprawności oraz jakości kodu.

-   **Warunek uruchomienia:** Zdarzenie `push`, `pull_request` lub manualne wybranie opcji `all` / `functional`.
    
-   **Środowisko:** Python 3.11 z włączonym mechanizmem cache'owania menedżera pakietów `pip`.
    
-   **Przebieb procesu:**
    
    1.  Pobranie kodu źródłowego (`actions/checkout@v4.2.2`).
        
    2.  Instalacja zależności systemowych oraz pakietów `pytest` i `pytest-cov`.
        
    3.  Analiza statyczna kodu (linting) za pomocą narzędzia `Ruff`. Wykrycie błędów formatowania lub składni przerywa działanie pipeline'u.
        
    4.  Wykonanie testów funkcjonalnych zlokalizowanych w katalogu `tests/functional/` wraz z generowaniem raportu pokrycia kodu (`coverage.xml`).
        
    5.  Przesłanie raportów pokrycia do zewnętrznego narzędzia Codecov (`codecov/codecov-action@v5`). Krok ten wykonuje się zawsze, niezależnie od wyniku samych testów.
        

> **Uwaga techniczna:** Ewentualne ostrzeżenia (deprecations) dotyczące wersji środowiska Node.js w logach wynikają ze specyfiki obrazu runnera GitHub i nie mają wpływu na proces testowy. Zastosowane akcje zostały zaktualizowane do wersji wspierających nowsze standardy środowiskowe.  Według changelog'u GitHub, ich runnery nie przełączą się domyślnie na Node 24 aż do 2 czerwca 2026 r. Ponieważ zaktualizowaliśmy już wszystkie nasze workflow actions do najnowszych wersji v4/v5, nasza konfiguracja jest w pełni aktualna, a te ostrzeżenia można bezpiecznie zignorować.

### 2.2. Performance Tests (`performance-tests`)

Zadanie dedykowane testom wydajnościowym i profilowaniu kodu.

-   **Warunek uruchomienia:** Zdarzenie `push`, `pull_request` lub manualne wybranie opcji `all` / `performance`.
    
-   **Środowisko:** Python 3.11 wraz z cache `pip`.
    
-   **Zabezpieczenie przed błędami pustego katalogu:** Wykorzystano mechanizm obsługi kodu wyjścia pytest. Jeśli katalog `tests/performance/` nie zawiera zdefiniowanych testów, komenda zwraca standardowy kod wyjścia `5`. Został on obsłużony wyrażeniem `|| [ $? -eq 5 ]`, co zapobiega awarii całego pipeline'u z powodu braku testów.
    
-   **Przebieg procesu:**
    
    1.  Instalacja biblioteki benchmarkowej `pytest-benchmark`.
        
    2.  Uruchomienie testów z flagą `--benchmark-only` oraz zapis wyników do pliku strukturyzowanego `benchmark.json`.
        
    3.  Weryfikacja istnienia oraz zawartości pliku wynikowego za pomocą funkcji `hashFiles`.
        
    4.  Wygenerowanie unikalnego znacznika czasu (timestamp) formatowanego do struktury `YYYY-MM-DD_HH-MM-SS`.
        
    5.  Archiwizacja pliku `benchmark.json` jako artefaktu GitHub Actions pod nazwą `benchmark-results-[timestamp]` z czasem retencji ustawionym na 30 dni.
        

### 2.3. Test Summary (`test-summary`)

Zadanie agregujące, działające po zakończeniu procesów testowych.

-   **Zależności:** `needs: [functional-tests, performance-tests]`
    
-   **Warunek uruchomienia:** Wykonuje się zawsze, pod warunkiem, że przynajmniej jedno z poprzednich zadań nie zostało pominięte (`skipped`).
    
-   **Funkcjonalność:** Ekstrakcja statusów końcowych zadań i wygenerowanie czytelnego podsumowania w formacie tabeli Markdown w sekcji `GitHub Step Summary`.
    
-   **Kontrola statusu wyjścia:** Jeśli którykolwiek z etapów testowych zakończył się niepowodzeniem (`failure`), zadanie celowo zwraca kod wyjścia `1`, co skutkuje oznaczeniem całego przebiegu workflow jako nieudanego w interfejsie GitHub.
    


Oto poprawiona wersja dokumentacji. Sekcja dotycząca pliku `benchmark.json` została zrekonstruowana w taki sposób, aby opisywała wyłącznie generyczną strukturę schematu danych, pomijając konkretne wartości liczbowe, nazwy funkcji czy parametry maszyn z pliku przykładowego.

Poprawiono również formatowanie tabeli w punkcie 4, aby wyświetlała się prawidłowo.

# Dokumentacja Pipeline CI: Test Pipeline

Repozytorium wykorzystuje narzędzie GitHub Actions do automatyzacji procesów Continuous Integration (CI). Zaimplementowany workflow odpowiada za uruchamianie testów funkcjonalnych, wydajnościowych, statyczną analizę kodu oraz agregację wyników.

## 1. Wyzwalacze (Triggers)

Workflow jest uruchamiany automatycznie lub manualnie w następujących przypadkach:

-   **Push:** Każde przesłanie zmian bezpośrednio do gałęzi `main`.
    
-   **Pull Request:** Utworzenie lub aktualizacja żądania zmian (PR) skierowanego do gałęzi `main`.
    
-   **Workflow Dispatch (Manualny):** Ręczne uruchomienie z poziomu zakładki _Actions_ w interfejsie GitHub.
    

### Parametry uruchomienia manualnego

Podczas ręcznego wyzwalania użytkownik ma możliwość zdefiniowania parametru wejściowego `test_level`:

-   `all` (domyślny): Uruchamia pełen zestaw testów.
    
-   `functional`: Uruchamia wyłącznie etap testów funkcjonalnych.
    
-   `performance`: Uruchamia wyłącznie etap testów wydajnościowych.
    

## 2. Architektura i Zadania (Jobs)

Workflow składa się z trzech odrębnych zadań wykonywanych na środowisku uruchomieniowym `ubuntu-latest`:

### 2.1. Functional Tests (`functional-tests`)

Zadanie odpowiedzialne za weryfikację poprawności oraz jakości kodu.

-   **Warunek uruchomienia:** Zdarzenie `push`, `pull_request` lub manualne wybranie opcji `all` / `functional`.
    
-   **Środowisko:** Python 3.11 z włączonym mechanizmem cache'owania menedżera pakietów `pip`.
    
-   **Przebieg procesu:**
    
    1.  Pobranie kodu źródłowego (`actions/checkout@v4.2.2`).
        
    2.  Instalacja zależności systemowych oraz pakietów `pytest` i `pytest-cov`.
        
    3.  Analiza statyczna kodu (linting) za pomocą narzędzia `Ruff`. Wykrycie błędów formatowania lub składni przerywa działanie pipeline'u.
        
    4.  Wykonanie testów funkcjonalnych zlokalizowanych w katalogu `tests/functional/` wraz z generowaniem raportu pokrycia kodu (`coverage.xml`).
        
    5.  Przesłanie raportów pokrycia do zewnętrznego narzędzia Codecov (`codecov/codecov-action@v5`). Krok ten wykonuje się zawsze, niezależnie od wyniku samych testów.
        

> **Uwaga techniczna:** Ewentualne ostrzeżenia (deprecations) dotyczące wersji środowiska Node.js w logach wynikają ze specyfiki obrazu runnera GitHub i nie mają wpływu na proces testowy. Zastosowane akcje zostały zaktualizowane do wersji wspierających nowsze standardy środowiskowe. Według changelog'u GitHub, ich runnery nie przełączą się domyślnie na Node 24 aż do 2 czerwca 2026 r. Ponieważ zaktualizowaliśmy już wszystkie nasze workflow actions do najnowszych wersji v4/v5, nasza konfiguracja jest w pełni aktualna, a te ostrzeżenia można bezpiecznie zignorować.

### 2.2. Performance Tests (`performance-tests`)

Zadanie dedykowane testom wydajnościowym i profilowaniu kodu.

-   **Warunek uruchomienia:** Zdarzenie `push`, `pull_request` lub manualne wybranie opcji `all` / `performance`.
    
-   **Środowisko:** Python 3.11 wraz z cache `pip`.
    
-   **Zabezpieczenie przed błędami pustego katalogu:** Wykorzystano mechanizm obsługi kodu wyjścia pytest. Jeśli katalog `tests/performance/` nie zawiera zdefiniowanych testów, komenda zwraca standardowy kod wyjścia `5`. Został on obsłużony wyrażeniem `|| [ $? -eq 5 ]`, co zapobiega awarii całego pipeline'u z powodu braku testów.
    
-   **Przebieg procesu:**
    
    1.  Instalacja biblioteki benchmarkowej `pytest-benchmark`.
        
    2.  Uruchomienie testów z flagą `--benchmark-only` oraz zapis wyników do pliku strukturyzowanego `benchmark.json`.
        
    3.  Weryfikacja istnienia oraz zawartości pliku wynikowego za pomocą funkcji `hashFiles`.
        
    4.  Wygenerowanie unikalnego znacznika czasu (timestamp) formatowanego do struktury `YYYY-MM-DD_HH-MM-SS`.
        
    5.  Archiwizacja pliku `benchmark.json` jako artefaktu GitHub Actions pod nazwą `benchmark-results-[timestamp]` z czasem retencji ustawionym na 30 dni.
        

### 2.3. Test Summary (`test-summary`)

Zadanie agregujące, działające po zakończeniu procesów testowych.

-   **Zależności:** `needs: [functional-tests, performance-tests]`
    
-   **Warunek uruchomienia:** Wykonuje się zawsze, pod warunkiem, że przynajmniej jedno z poprzednich zadań nie zostało pominięte (`skipped`).
    
-   **Funkcjonalność:** Ekstrakcja statusów końcowych zadań i wygenerowanie czytelnego podsumowania w formacie tabeli Markdown w sekcji `GitHub Step Summary`.
    
-   **Kontrola statusu wyjścia:** Jeśli którykolwiek z etapów testowych zakończył się niepowodzeniem (`failure`), zadanie celowo zwraca kod wyjścia `1`, co skutkuje oznaczeniem całego przebiegu workflow jako nieudanego w interfejsie GitHub.
    

## 3. Struktura raportu wydajnościowego (Benchmark Data)

Generowany plik `benchmark.json` stanowi ustrukturyzowany dokument JSON dostarczany przez bibliotekę `pytest-benchmark`. Zawiera on metadane środowiskowe oraz surowe i zagregowane wyniki pomiarów wydajnościowych.

Schemat pliku składa się z następujących sekcji głównych:

### 3.1. Informacje o maszynie (`machine_info`)

Obiekt przechowujący pełną specyfikację techniczną środowiska wykonawczego (runnera) w celu umożliwienia rzetelnej analizy porównawczej wyników:

-   **System i architektura:** Informacje o systemie operacyjnym, wersji jądra (release) oraz architekturze procesora.
    
-   **Procesor (CPU):** Szczegółowe metadane procesora, w tym nazwa handlowa modelu, częstotliwość taktowania (nominalna oraz rzeczywista) oraz liczba przypisanych rdzeni logicznych.
    
-   **Środowisko uruchomieniowe Pythona:** Identyfikacja implementacji interpretera (np. CPython), jego dokładna wersja oraz informacje o kompilatorze użytym do jego zbudowania.
    

### 3.2. Metadane kodu źródłowego (`commit_info`)

Identyfikuje dokładny stan i kontekst repozytorium w momencie uruchomienia pomiarów:

-   **id:** Unikalny identyfikator (hash SHA-1) commitu.
    
-   **branch:** Nazwa gałęzi, na której wykonano testy.
    
-   **project:** Nazwa identyfikacyjna projektu.
    
-   **dirty:** Flaga logiczna (boolean) określająca, czy w środowisku roboczym znajdowały się niezatwierdzone (uncommitted) zmiany.
    

### 3.3. Wyniki pomiarów (`benchmarks`)

Tablica obiektów, w której każdy element odpowiada jednemu wykonanemu testowi wydajnościowemu. Każdy obiekt testu zawiera:

-   **name:** Pełna nazwa funkcji testowej wraz z jej ścieżką lub parametrami.
    
-   **options:** Parametry konfiguracyjne profilowania, określające m.in. status mechanizmu odśmiecania pamięci (Garbage Collector), typ licznika czasu użytego do pomiarów oraz narzucone limity iteracji.
    
-   **stats (Statystyki zagregowane):** Obiekt zawierający matematyczną analizę zebranych próbek czasu:
    
    -   Metryki centralne: wartości minimalne (`min`), maksymalne (`max`), średnie (`mean`) oraz mediana (`median`) czasu wykonania operacji.
        
    -   Metryki wydajnościowe: przepustowość wyrażona jako liczba operacji na sekundę (`ops`).
        
    -   Metryki stabilności: odchylenie standardowe (`stddev`) oraz licznik wartości skrajnych/anomalii (`outliers`).
        
    -   Liczba prób: całkowita liczba wykonanych powtórzeń pętli testowej (`rounds`).
        
-   **data (Dane surowe):** Tablica wartości zmiennoprzecinkowych przechowująca dokładny czas trwania każdej indywidualnej rundy testowej, co umożliwia późniejszą weryfikację rozkładu statystycznego.
    

### 3.4. Metadane sesji

-   **datetime:** Dokładna data i godzina zakończenia sesji pomiarowej zapisana w formacie ISO 8601 (UTC).
    
-   **version:** Wersja narzędzia `pytest-benchmark` użytego do wygenerowania struktury pliku.

## 4. Matryca Wyników Podsumowania (Step Summary)

Zadanie `test-summary` generuje raport w oparciu o poniższą logikę stanów:
| Stan zadania bazowego | Status w raporcie | Wpływ na końcowy status workflow  |
|-----------------------|-------------------|-----------------------------------|
| `success`               | PASSED            | Neutralny / Sukces                |
| `failure`               | FAILED            | Wymuszenie statusu błędu (exit 1) |
| `skipped`               | SKIPPED           | Neutralny                         |



## 5. Utrzymanie i Modyfikacje

W przypadku konieczności aktualizacji wersji narzędzi:

1.  **Wersja Pythona:** Zmiana wartości w kluczu `python-version` w zadaniach `functional-tests` oraz `performance-tests`.
    
2.  **Retencja artefaktów:** Modyfikacja parametru `retention-days` (maksymalna dopuszczalna wartość dla GitHub Actions wynosi 90 dni).
    
3.  **Wersje Akcji:** Monitorowanie repozytoriów `actions/checkout`, `actions/setup-python` oraz `codecov/codecov-action` pod kątem wydań wyższych wersji major.
