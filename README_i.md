# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Panoramica

Benchmarking_test consente ai team di scoprire e correggere difetti nascosti nei modelli predittivi creando automaticamente test realistici di casi limite. Evidenzia lacune di accuratezza, bias e problemi di robustezza, permettendo un miglioramento più rapido e equo del modello senza etichettatura manuale.

---

## Sommario

- [Panoramica](#panoramica)
- [Funzionalità principali](#funzionalità-principali)
- [Installazione](#installazione)
- [Contributi](#contributi)
- [Citazione](#citazione)

---

## Funzionalità principali

1. **Preprocessing dei dati e ingegneria delle feature**: Pulizia automatica, codifica, scaling e decomposizione delle date di dataset grezzi di appartamenti e serie temporali, rimozione di colonne irrilevanti e ordinamento cronologico delle osservazioni per preparare i dati al modello successivo.
2. **Suite di addestramento di modelli di regressione**: Addestramento e valutazione di più algoritmi di regressione (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) su dati di pricing immobiliare con persistenza automatica e report di performance (R², MAPE).
3. **Pipeline di benchmarking generativo a due fasi**: Combina algoritmi genetici per identificare istanze mal previste con variational autoencoders che apprendono la distribuzione dei casi di fallimento, producendo esempi di test sintetici mirati alle debolezze del modello.
4. **Generazione di scenari consapevoli di equità**: Crea esempi sintetici counterfactual in sotto-spazi di feature con prestazioni inferiori per esporre e mitigare bias tra segmenti demografici e geografici.
5. **Generazione di dati sintetici per casi limite**: Produce campioni sintetici ad alta densità nelle regioni dello spazio delle feature dove i modelli mostrano errori elevati, facilitando test robusti e miglioramento continuo.

---

## Installazione

Installa Benchmarking_test usando uno dei seguenti metodi:

**Costruisci dal sorgente**:

1. Clona il repository Benchmarking_test:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Naviga nella directory del progetto:
   ```sh
   cd Benchmarking_test
   ```
3. Installa le dipendenze del progetto:
   ```sh
   pip install -r requirements.txt
   ```

---

## Contributi

- **[Segnala problemi](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Invia bug trovati o richiedi nuove funzionalità per il progetto.
- **[Invia pull request](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: Per saperne di più su come contribuire a Benchmarking_test.

---

## Citazione

DRMPN (2025). Repository di benchmarking [Software informatico]. https://github.com/DRMPN/Benchmarking

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
