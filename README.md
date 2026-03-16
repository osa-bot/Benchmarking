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

Benchmarking_test empowers teams to uncover and address hidden flaws in predictive models by automatically creating realistic edge‑case tests. It reveals accuracy gaps, bias, and robustness issues, enabling quicker, fairer model improvement without manual labeling.
---

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Examples](#examples)
- [Contributing](#contributing)
- [Citation](#citation)
---

## Core features

1. **Data Preprocessing & Feature Engineering**: Automated cleaning, encoding, scaling, and date decomposition of raw apartment and time‑series datasets, removing irrelevant columns, handling missing values, and ordering observations chronologically to produce a tidy DataFrame ready for modeling.
2. **Regression Model Training Suite**: A plug‑in pipeline that trains multiple regression algorithms (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) on real‑estate pricing data, evaluates them with R² and MAPE, and persists the best models for inference.
3. **Two‑Stage Generative Benchmarking Pipeline**: Combines a genetic algorithm to locate poorly‑predicted instances with a variational auto‑encoder that learns the distribution of those failure cases, producing synthetic test examples that specifically target model weaknesses.
4. **Fairness‑Aware Scenario Generation**: Creates counterfactual synthetic examples in under‑performing feature subspaces (e.g., demographic or geographic groups) to expose and mitigate bias in predictive models.
5. **Synthetic Edge‑Case Data Generation**: Generates high‑density synthetic samples in regions of the feature space where models exhibit high error, enabling robust testing and continuous improvement of model robustness.
---

## Installation

Build from source:

```sh
# 1. Clone the Benchmarking_test repository
git clone https://github.com/fl1pcoin/Benchmarking_test

# 2. Navigate to the project directory
cd Benchmarking_test

# 3. Install the project dependencies
pip install -r requirements.txt
```
---

## Getting Started

The project ships with a Jupyter notebook that demonstrates a toy end‑to‑end workflow:

1. **Generate a synthetic dataset**
2. **Train a baseline model** (e.g., `LinearRegression` or `XGBRegressor`)
3. **Identify poorly predicted points**
4. **Generate synthetic edge‑case examples** using a genetic algorithm and a VAE
5. **Evaluate the models on the synthetic data**

You can run the notebook directly:

```bash
jupyter notebook examples/Model_toy_example.ipynb
```

If you prefer a quick script, the following minimal example reproduces the core steps from the notebook:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error, r2_score
from sklearn.linear_model import LinearRegression

# Synthetic data
X = np.random.rand(1000, 2)
y = X @ np.array([2.0, 3.0]) + 7
X, y = pd.DataFrame(X), pd.DataFrame(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Baseline model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions and metrics
pred = model.predict(X_test).flatten()
print('MAPE:', mean_absolute_percentage_error(y_test, pred))
print('R²:', r2_score(y_test, pred))
```

This snippet gives you a quick feel for how the library works. For a full demonstration, open the notebook and follow the visualizations and code cells.
---

## Examples

Examples of how this should work and how it should be used are available [here](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/examples).
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
