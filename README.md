# Benchmarking_test

---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Overview

Benchmarking_test helps teams quickly identify and fix hidden weaknesses in predictive models by generating realistic edge‑case tests. It highlights accuracy gaps, bias, and robustness problems, enabling faster, fairer model improvement without manual labeling.

---

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)

---

## Core features

1. **Data Preprocessing & Feature Engineering**: Automated cleaning, encoding, scaling, and date decomposition of raw apartment and time‑series datasets, removing irrelevant columns and ordering observations chronologically to prepare data for downstream modeling.
2. **Regression Model Training Suite**: Training and evaluation of multiple regression algorithms (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) on real‑estate pricing data with automated persistence and performance reporting (R², MAPE).
3. **Two‑Stage Generative Benchmarking Pipeline**: Combines genetic algorithms to identify poorly‑predicted instances with variational autoencoders that learn the distribution of failure cases, producing synthetic test examples that target model weaknesses.
4. **Fairness‑Aware Scenario Generation**: Creates counterfactual synthetic examples in under‑performing feature subspaces to expose and mitigate bias across demographic and geographic segments.
5. **Hyperparameter Optimization with Optuna**: Automated Bayesian tuning of model and generation hyperparameters, enabling efficient exploration of parameter space for improved performance.
6. **Sobol Sensitivity Analysis**: Quantifies the influence of each input feature on model predictions, informing feature importance and guiding the genetic algorithm’s mutation and crossover strategies.
7. **Synthetic Data Generation for Edge Cases**: Generates high‑density synthetic samples in regions of the feature space where models exhibit high error, facilitating robust testing and continuous improvement.

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
