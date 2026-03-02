# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black)
---

## Overview

Benchmarking_test helps teams identify and fix hidden weaknesses in predictive models by automatically generating realistic edge‑case tests. It highlights accuracy gaps, bias, and robustness problems, enabling faster, fairer model improvement without manual labeling.
---

## Table of Contents

- [Overview](#overview)
- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)
---

## Core features

1. **Data Preprocessing & Feature Engineering**: Automated cleaning, encoding, scaling, and date decomposition of raw apartment and time‑series datasets. It removes irrelevant columns, handles missing values, and orders observations chronologically to produce a tidy DataFrame ready for modeling.
2. **Regression Model Training Suite**: A plug‑in training pipeline that fits multiple regression algorithms (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) on real‑estate pricing data, evaluates them with R² and MAPE, and persists the best models for later inference.
3. **Two‑Stage Generative Benchmarking Pipeline**: Combines a genetic algorithm to locate poorly‑predicted instances with a variational auto‑encoder that learns the distribution of those failure cases, producing synthetic test examples that specifically target model weaknesses.
4. **Fairness‑Aware Scenario Generation**: Creates counterfactual synthetic examples in under‑performing feature subspaces (e.g., demographic or geographic groups) to expose and mitigate bias in predictive models.
5. **Synthetic Edge‑Case Data Generation**: Generates high‑density synthetic samples in regions of the feature space where models exhibit high error, enabling robust testing and continuous improvement of model robustness.
---

## Installation

Install Benchmarking_test using one of the following methods:

**Build from source**:

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

## Contributing

- **[Report Issues](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Submit bugs found or log feature requests for the project.
- **[Submit Pull Requests](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: To learn more about making a contribution to Benchmarking_test.
---

## Citation

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
