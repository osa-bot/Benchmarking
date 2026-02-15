# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Собрано с помощью:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)
---

## Обзор

Benchmarking_test предоставляет фреймворк для автоматического обнаружения и тестирования слабых мест модели путём генерации реалистичных сценариев крайних случаев, помогая командам улучшать точность, справедливость и устойчивость предиктивных моделей без ручной разметки.
---

## Содержание

- [Обзор](#overview)
- [Основные функции](#core-features)
- [Установка](#installation)
- [Внесение вклада](#contributing)
- [Цитирование](#citation)
---

## Основные функции

1. **Data Preprocessing & Feature Engineering**: Автоматизированная очистка, кодирование и масштабирование сырых наборов данных о квартирах и временных рядах, включая извлечение дат, one‑hot кодирование, масштабирование MinMax и удаление нерелевантных колонок для подготовки данных к последующему моделированию.
2. **Regression Model Training Suite**: Обучение и оценка нескольких регрессионных алгоритмов (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) на данных о ценах недвижимости, с автоматической сохранением модели и отчётом о производительности (R², MAPE).
3. **Two‑Stage Generative Benchmarking Pipeline**: Комбинирует генетические алгоритмы для выявления и усиления плохо предсказанных экземпляров с вариационными автоэнкодерами, которые изучают распределение случаев неудач, создавая синтетические тестовые примеры, направленные на слабые места модели.
4. **Fairness‑Aware Scenario Generation**: Создаёт контрфактические синтетические примеры в подпространствах с низкой производительностью, чтобы выявить и смягчить предвзятость по демографическим и географическим сегментам.
5. **Hyperparameter Optimization with Optuna**: Автоматическая настройка гиперпараметров модели и генерации с использованием байесовской оптимизации, позволяющая эффективно исследовать пространство параметров для улучшения производительности.
6. **Sobol Sensitivity Analysis**: Квантитативно оценивает влияние каждого входного признака на предсказания модели, информируя о важности признаков и направляя стратегии мутации и кроссовера генетического алгоритма.
7. **Synthetic Data Generation for Edge Cases**: Генерирует высоко плотные синтетические образцы в регионах пространства признаков, где модели показывают высокую ошибку, облегчая надёжное тестирование и непрерывное улучшение.
8. **Multi‑Agent Self‑Evaluation Framework**: Позволяет автономным агентам оценивать друг друга на динамически генерируемых бенчмарках, способствуя саморефлексии и итеративному улучшению модели.
---

## Установка

Установите Benchmarking_test, используя один из следующих методов:

**Сборка из исходного кода:**

1. Клонируйте репозиторий Benchmarking_test:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Перейдите в каталог проекта:
   ```sh
   cd Benchmarking_test
   ```
3. Установите зависимости проекта:
   ```sh
   pip install -r requirements.txt
   ```
---

## Внесение вклада

- **[Report Issues](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Отправьте найденные ошибки или запросы на новые функции для проекта.
- **[Submit Pull Requests](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: Чтобы узнать больше о том, как внести вклад в Benchmarking_test.
---

## Цитирование

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
