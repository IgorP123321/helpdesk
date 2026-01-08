# HelpDesk System & QA Automation Suite 🚀

## 📖 O projekcie
System HelpDesk to techniczna aplikacja zbudowana w języku Python, służąca do ewidencji i zarządzania zgłoszeniami serwisowymi. Projekt demonstruje praktyczne zastosowanie **programowania obiektowego (OOP)** oraz nowoczesnych metod **zapewnienia jakości (QA)**. Jako osoba z wykształceniem mechatronicznym, skupiam się na budowaniu rozwiązań, które są odporne na błędy i łatwe w weryfikacji.

## 🚀 Kluczowe Funkcjonalności
* **Modelowanie Obiektowe:** Wykorzystanie klasy `Ticket` do precyzyjnej reprezentacji zgłoszeń (imię klienta, opis, priorytet).
* **Automatyzacja Statusów:** Logika biznesowa zarządzająca cyklem życia zgłoszenia od otwarcia (`Open`) do rozwiązania (`Resolved`).
* **Walidacja Danych:** System dba o to, aby zgłoszenia posiadały kompletnie zdefiniowane parametry przed ich przetworzeniem.
* **Logowanie Zdarzeń:** Mechanizm zapisu zgłoszeń do zewnętrznego pliku tekstowego (`tickets.txt`), co imituje działanie bazy danych.

## 🧪 Automatyzacja Testów (Framework Pytest)
Głównym sercem projektu jest rozbudowany zestaw testów automatycznych, który pozwala na błyskawiczną weryfikację poprawności działania systemu. Zastosowane podejście testowe obejmuje:

* **Testy Jednostkowe (Unit Tests):** Weryfikacja, czy obiekty klasy `Ticket` są poprawnie inicjalizowane.
* **Testy Wartości Brzegowych (Boundary Testing):** Sprawdzenie, jak system zachowuje się przy ekstremalnie długich nazwach (stress test) oraz pustych opisach.
* **Testy Negatywne:** Upewnienie się, że system nie pozwala na nieprawidłowe stany (np. sprawdzenie, czy nowy bilet domyślnie nie jest ustawiony jako rozwiązany).
* **Testy Przejść Stanów (State Transition):** Automatyczna weryfikacja, czy metoda `.resolve()` poprawnie zmienia status zgłoszenia.

## 🛠 Technologie i Narzędzia
* **Język:** Python 3.x
* **Framework Testowy:** Pytest
* **Kontrola Wersji:** Git / GitHub
* **Środowisko:** VS Code

## 📂 Struktura Projektu
* `appy.py" – Rdzeń aplikacji: logika biznesowa i definicja klasy `Ticket`.
* `test_logic.py` – Skrypty testowe zawierające zautomatyzowane scenariusze QA.
* `tickets.txt` – Plik wynikowy z zapisanymi danymi zgłoszeń.

## ⚙️ Jak uruchomić i testować
1. **Sklonuj repozytorium:**
   ```bash
   git clone [https://github.com/IgorP123321/helpdesk.git](https://github.com/IgorP123321/helpdesk.git)