# Benchmarking

---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Overview

Advancing artificial general intelligence requires developing self-reflection mechanisms in multi-agent systems through generative benchmarking. This research addresses the critical challenge of evaluating AI model quality in edge cases where failures are rare but consequential. A two-stage generative benchmarking pipeline synthesizes test examples targeting model weaknesses without human intervention, combining genetic algorithms to augment poorly-predicted instances with variational autoencoders to approximate their probability distribution. The methodology formalizes benchmark generation for regression and classification tasks, enabling multi-agent systems to conduct mutual evaluation through dynamically generated benchmarks and facilitating agent self-improvement through objective performance assessment.

---

## Table of Contents

- [Overview](#overview)
- [Content](#content)
- [Algorithms](#algorithms)
- [Installation](#installation)
- [Citation](#citation)

---

## Content

This benchmarking project develops a generative framework for identifying and correcting machine learning model failures through synthetic data augmentation. The system trains regression models on real estate pricing data, then employs a two-stage pipeline combining genetic algorithms and variational autoencoders to synthesize test cases targeting model weaknesses. Key components include:

- **Data Preprocessing & Feature Engineering**: Modules that prepare Moscow apartment datasets with feature encoding (MinMaxScaler, LabelEncoder, one-hot encoding)
- **Regression Models**: Multiple implementations including KNN, Gradient Boosting, Random Forest, XGBoost, and Linear Regression for price prediction
- **Fairness-Aware Scenario Generation**: Creates synthetic counterfactual examples in underperforming feature subspaces
- **Supporting Utilities**: 
  - Hyperparameter optimization via Optuna
  - Sensitivity analysis through Sobol indices
  - Model distillation into neural networks
  - Train-test splitting and ensemble methods

By augmenting training data with algorithmically-generated examples that expose prediction failures, the framework improves model robustness and fairness across demographic and geographic segments, enabling autonomous systems to conduct self-evaluation and continuous improvement.

---

## Algorithms

The project implements a two-stage generative benchmarking pipeline combining genetic algorithms and variational autoencoders:

1. **Genetic Algorithms**: Identify and augment poorly-predicted instances by evolving feature combinations toward target performance improvements, guided by linear regression coefficients and Sobol sensitivity indices
2. **Variational Autoencoders**: Learn the probability distribution of augmented failure cases, generating synthetic test examples that densely populate model weakness regions
3. **Supporting Techniques**: Feature encoding, train-test splitting, and ensemble regression models (XGBoost, Random Forest, KNN)

These methods collectively enable automated discovery of edge cases where machine learning models fail, creating realistic synthetic benchmarks without manual annotation for continuous model evaluation and improvement.

---

## Installation

Install Benchmarking using one of the following methods:

**Build from source:**

1. Clone the Benchmarking repository:
```bash
git clone https://github.com/DRMPN/Benchmarking
```

2. Navigate to the project directory:
```bash
cd Benchmarking
```

3. Install the project dependencies:
```bash
pip install -r requirements.txt
```

---

## Citation

If you use this software, please cite it as below.

### APA format:

```
DRMPN (2025). Benchmarking repository [Computer software]. https://github.com/DRMPN/Benchmarking
```

### BibTeX format:

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

---