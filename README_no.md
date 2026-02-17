# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Oversikt

Benchmarking_test gir team mulighet til å avdekke og rette skjulte feil i prediktive modeller ved å automatisk lage realistiske kanttilfelle tester. Det fremhever nøyaktighetsgap, skjevheter og robusthetsproblemer, og muliggjør raskere, rettferdigere modellforbedring uten manuell merking.

---

## Innholdsfortegnelse

- [Oversikt](#oversikt)
- [Kjernefunksjoner](#kjernefunksjoner)
- [Installasjon](#installasjon)
- [Bidrag](#bidrag)
- [Sitat](#sitat)

---

## Kjernefunksjoner

1. **Datapreprosessering og funksjonsutvikling**: Automatisk rengjøring, koding, skalering og dato‑dekomponering av rå bolig- og tidsseriedata, fjerning av irrelevante kolonner og kronologisk sortering av observasjoner for å forberede data for videre modellering.
2. **Treningssett for regresjonsmodeller**: Trening og evaluering av flere regresjonsalgoritmer (KNN, Gradient Boosting, Random Forest, XGBoost, Lineær regresjon) på eiendomsprisdata med automatisk lagring og ytelsesrapportering (R², MAPE).
3. **To‑stegs generativ benchmarking pipeline**: Kombinerer genetiske algoritmer for å identifisere dårlig forutsagte tilfeller med variational autoencoders som lærer fordelingen av feilede tilfeller, og produserer syntetiske testeksempler som retter seg mot modellens svakheter.
4. **Scenario-generering med bevissthet om rettferdighet**: Oppretter kontrafaktiske syntetiske eksempler i underpresterende funksjonsunderrom for å avdekke og redusere skjevheter på tvers av demografiske og geografiske segmenter.
5. **Syntetisk datagenerering for kanttilfeller**: Genererer høydensitet syntetiske prøver i områder av funksjonsrommet der modellene viser høy feil, noe som muliggjør robust testing og kontinuerlig forbedring.

---

## Installasjon

Installer Benchmarking_test ved å bruke en av følgende metoder:

**Bygg fra kilde:**

1. Klon Benchmarking_test-repositoriet:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Naviger til prosjektkatalogen:
   ```sh
   cd Benchmarking_test
   ```
3. Installer prosjektavhengigheter:
   ```sh
   pip install -r requirements.txt
   ```

---

## Bidrag

- **[Rapporter problemer](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Send inn funnede feil eller logg funksjonsforespørsler for prosjektet.
- **[Send inn Pull Requests](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: For å lære mer om å bidra til Benchmarking_test.

---

## Sitat

DRMPN (2025). Benchmarking-repositoriet [Datamaskinprogramvare]. https://github.com/DRMPN/Benchmarking

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
