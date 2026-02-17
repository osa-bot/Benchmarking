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
- [Bidrag](#contributing)
- [Citat](#citation)

---

## Kärnfunktioner

1. **Dataförbehandling & Funktionsutveckling**: Automatisk rengöring, kodning, skalning och datumdekomposition av råa bostads- och tidsseriedata, borttagning av irrelevanta kolumner och sortering av observationer kronologiskt för att förbereda data för efterföljande modellering.
2. **Regressionmodellträning**: Träning och utvärdering av flera regressionsalgoritmer (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) på fastighetsprisdatan med automatiserad lagring och prestandarapportering (R², MAPE).
3. **Tvåstegs generativ benchmarkpipeline**: Kombinerar genetiska algoritmer för att identifiera dåligt förutsagda fall med variational autoencoders som lär sig fördelningen av misslyckade fall, vilket producerar syntetiska testexempel som riktar sig mot modellens svagheter.
4. **Rättvisebewakande scenariegenerering**: Skapar kontrafaktiska syntetiska exempel i underpresterande funktionsdelområden för att exponera och mildra bias över demografiska och geografiska segment.
5. **Syntetisk datagenerering för edge‑cases**: Genererar högdensitetssyntetiska prover i områden av funktionsutrymmet där modeller visar hög fel, vilket underlättar robust testning och kontinuerlig förbättring.

---

## Installation

Installera Benchmarking_test med någon av följande metoder:

**Bygg från källkod:**

1. Klona Benchmarking_test-repositoriet:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Navigera till projektkatalogen:
   ```sh
   cd Benchmarking_test
   ```
3. Installera projektets beroenden:
   ```sh
   pip install -r requirements.txt
   ```

---

## Bidrag

- **[Rapportera problem](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Skicka in bug eller logga funktionsförfrågningar för projektet.
- **[Skicka Pull Requests](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: För att lära dig mer om hur du gör ett bidrag till Benchmarking_test.

---

## Citat

DRMPN (2025). Benchmarking-repository [Computer software]. https://github.com/DRMPN/Benchmarking

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
