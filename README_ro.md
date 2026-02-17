# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Prezentare generală

Benchmarking_test permite echipelor să descopere și să remedieze defecte ascunse în modelele predictive prin crearea automată de teste realiste pentru cazuri extreme. Evidențiază diferențele de acuratețe, părtinirea și problemele de robustețe, permițând îmbunătățirea modelelor mai rapidă și mai echitabilă fără etichetare manuală.

---

## Indice

- [Prezentare generală](#prezentare-generală)
- [Caracteristici principale](#caracteristici-principale)
- [Instalare](#instalare)
- [Contribuții](#contribuții)
- [Citare](#citare)

---

## Caracteristici principale

1. **Preprocesare a datelor și inginerie de caracteristici**: Curățare, codificare, scalare și decompoziție a datelor de timp și a seturilor de date despre apartamente, eliminând coloane irelevante și ordonând observațiile cronologic pentru a pregăti datele pentru modelarea ulterioară.
2. **Suite de antrenament a modelelor de regresie**: Antrenarea și evaluarea mai multor algoritmi de regresie (KNN, Gradient Boosting, Random Forest, XGBoost, Regresie liniară) pe date de prețuri imobiliare, cu raportare automată a performanței (R², MAPE).
3. **Pipeline de benchmarking generativ în două etape**: Combină algoritmi genetici pentru identificarea instanțelor slab prezise cu autoencodere variationale care învață distribuția cazurilor de eșec, producând exemple de test sintetic care vizează slăbiciunile modelului.
4. **Generare de scenarii conștiente de echitate**: Creează exemple sintetice contrafactuale în subspații de caracteristici subperformante pentru a expune și a atenua părtinirea în segmentul demografic și geografic.
5. **Generare de date sintetice pentru cazuri extreme**: Produce mostre sintetice de înaltă densitate în regiunile spațiului de caracteristici unde modelele prezintă erori mari, facilitând testarea robustă și îmbunătățirea continuă.

---

## Instalare

Instalați Benchmarking_test utilizând una dintre următoarele metode:

**Construiește din sursă:**

1. Clonați depozitul Benchmarking_test:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Navigați la directorul proiectului:
   ```sh
   cd Benchmarking_test
   ```
3. Instalați dependențele proiectului:
   ```sh
   pip install -r requirements.txt
   ```

---

## Contribuții

- **[Raportați probleme](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Trimiteți erori găsite sau solicitați caracteristici pentru proiect.
- **[Trimiteți Pull Requests](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: Pentru a afla mai multe despre cum să contribuiți la Benchmarking_test.

---

## Citare

DRMPN (2025). Depozit Benchmarking [Software de calculator]. https://github.com/DRMPN/Benchmarking

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
