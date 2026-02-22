# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Überblick

Benchmarking_test ermöglicht es Teams, versteckte Fehler in Vorhersagemodellen aufzudecken und zu beheben, indem automatisch realistische Grenzfalltests erstellt werden. Es hebt Genauigkeitslücken, Bias und Robustheitsprobleme hervor und ermöglicht eine schnellere, gerechtere Modellverbesserung ohne manuelles Labeling.

---

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Kernfunktionen](#kernfunktionen)
- [Installation](#installation)
- [Mitwirken](#mitwirken)
- [Zitation](#zitation)

---

## Kernfunktionen

1. **Datenvorverarbeitung & Feature Engineering**: Automatisierte Bereinigung, Kodierung, Skalierung und Datumszerlegung von Rohdaten zu Wohnungen und Zeitreihen, Entfernen irrelevanter Spalten und chronologische Ordnung der Beobachtungen zur Vorbereitung der Daten für nachgelagerte Modellierung.
2. **Regression Model Training Suite**: Training und Bewertung mehrerer Regressionsalgorithmen (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) auf Immobilienpreis-Daten mit automatischer Persistenz und Leistungsberichterstattung (R², MAPE).
3. **Zwei‑Stufen Generative Benchmarking Pipeline**: Kombiniert genetische Algorithmen zur Identifizierung schlecht vorhergesagter Instanzen mit variationalen Autoencodern, die die Verteilung von Fehlermustern lernen, und erzeugt synthetische Testbeispiele, die gezielt Schwachstellen des Modells ansprechen.
4. **Fairness‑Aware Scenario Generation**: Erstellt kontrafaktische synthetische Beispiele in unterdurchschnittlichen Feature‑Subspaces, um Bias über demografische und geografische Segmente hinweg aufzudecken und zu mildern.
5. **Synthetische Datengenerierung für Grenzfälle**: Erzeugt hochdichte synthetische Stichproben in Bereichen des Feature‑Raums, in denen Modelle hohe Fehler aufweisen, um robuste Tests und kontinuierliche Verbesserungen zu ermöglichen.

---

## Installation

Installieren Sie Benchmarking_test mit einer der folgenden Methoden:

**Aus dem Quellcode bauen**:

1. Klonen Sie das Benchmarking_test Repository:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Navigieren Sie zum Projektverzeichnis:
   ```sh
   cd Benchmarking_test
   ```
3. Installieren Sie die Projektabhängigkeiten:
   ```sh
   pip install -r requirements.txt
   ```

---

## Mitwirken

- **[Probleme melden](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Melden Sie gefundene Fehler oder loggen Sie Funktionsanfragen für das Projekt.
- **[Pull Requests einreichen](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: Um mehr darüber zu erfahren, wie Sie zu Benchmarking_test beitragen können.

---

## Zitation

DRMPN (2025). Benchmarking repository [Computer software]. https://github.com/DRMPN/Benchmarking

```bibtex
@misc{Benchmarking,
    author = {DRMPN},
    title = {Benchmarking repository},
    year = {2025},
    publisher = {github.com},
    journal = {github.com repository},
    howpublished = {\url{https://github.com/DRMPN/Benchmarking.git}},
    url = {https://github.com/DRMPN/Benchmarking.git}
}
```
