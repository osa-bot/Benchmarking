# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Översikt

Benchmarking_test ger team möjlighet att upptäcka och åtgärda dolda fel i förutsägande modeller genom att automatiskt skapa realistiska edge‑case tester. Det belyser noggrannhetsluckor, bias och robusthetsproblem, vilket möjliggör snabbare, rättvisare modellförbättring utan manuell märkning.

---

## Innehållsförteckning

- [Översikt](#overview)
- [Kärnfunktioner](#core-features)
- [Installation](#installation)
- [Bidra](#contributing)
- [Citat](#citation)

---

## Kärnfunktioner

1. **Data Preprocessing & Feature Engineering**: Automatiserad rengöring, kodning, skalning och datumdekomposition av råa bostads- och tidsseriedata, borttagning av irrelevanta kolumner och sortering av observationer kronologiskt för att förbereda data för efterföljande modellering.
2. **Regression Model Training Suite**: Träning och utvärdering av flera regressionsalgoritmer (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) på fastighetsprissättningsdata med automatiserad lagring och prestandarapportering (R², MAPE).
3. **Two‑Stage Generative Benchmarking Pipeline**: Kombinerar genetiska algoritmer för att identifiera dåligt förutsagda fall med variational autoencoders som lär sig fördelningen av misslyckade fall, vilket producerar syntetiska testexempel som riktar sig mot modellens svagheter.
4. **Fairness‑Aware Scenario Generation**: Skapar kontrafaktiska syntetiska exempel i underpresterande funktionssubrum för att exponera och mildra bias över demografiska och geografiska segment.
5. **Synthetic Data Generation for Edge Cases**: Genererar högdensitet syntetiska prover i områden av funktionsutrymmet där modeller visar hög fel, vilket underlättar robust testning och kontinuerlig förbättring.

---

## Installation

Installera Benchmarking_test med någon av följande metoder:

**Build from source:**

1. Clone the Benchmarking_test repository:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Navigate to the project directory:
   ```sh
   cd Benchmarking_test
   ```
3. Install the project dependencies:
   ```sh
   pip install -r requirements.txt
   ```

---

## Bidra

- **[Report Issues](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Submit bugs found or log feature requests for the project.
- **[Submit Pull Requests](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: To learn more about making a contribution to Benchmarking_test.

---

## Citat

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
