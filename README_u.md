# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Огляд

Benchmarking_test дозволяє командам виявляти та усувати приховані недоліки в прогнозних моделях, автоматично створюючи реалістичні тестові випадки крайніх сценаріїв. Він підкреслює розриви точності, упередження та проблеми стійкості, забезпечуючи швидше та справедливіше вдосконалення моделі без ручного маркування.

---

## Таблиця змісту

- [Огляд](#огляд)
- [Основні функції](#основні-функції)
- [Встановлення](#встановлення)
- [Участь](#участь)
- [Цитування](#цитування)

---

## Основні функції

1. **Обробка даних та інженерія ознак**: Автоматичне очищення, кодування, масштабування та розкладання дат у сирих наборах даних про квартири та часових рядів, видалення нерелевантних колонок і впорядкування спостережень за часом для підготовки даних до подальшого моделювання.
2. **Набір для навчання регресійних моделей**: Навчання та оцінка кількох регресійних алгоритмів (KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression) на даних про цінність нерухомості з автоматичною збереженням та звітністю про продуктивність (R², MAPE).
3. **Двоступеневий генеративний пайплайн тестування**: Поєднує генетичні алгоритми для виявлення погано передбачуваних випадків з варіаційними автоенкодерами, які вивчають розподіл випадків невдач, створюючи синтетичні тестові приклади, що спрямовані на слабкості моделі.
4. **Генерація сценаріїв з урахуванням справедливості**: Створює контрафактивні синтетичні приклади в підвищених підпросторах ознак, щоб виявити та пом'якшити упередження в демографічних та географічних сегментах.
5. **Генерація синтетичних даних для крайніх випадків**: Створює високоденсійні синтетичні зразки в регіонах простору ознак, де моделі демонструють високі помилки, сприяючи надійному тестуванню та безперервному вдосконаленню.

---

## Встановлення

Встановіть Benchmarking_test, використовуючи один із наступних методів:

**Збірка з джерела**:

1. Клонувати репозиторій Benchmarking_test:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Перейдіть до каталогу проекту:
   ```sh
   cd Benchmarking_test
   ```
3. Встановіть залежності проекту:
   ```sh
   pip install -r requirements.txt
   ```

---

## Участь

- **[Report Issues](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Надішліть помилки або запити на нові функції для проекту.
- **[Submit Pull Requests](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: Дізнайтеся більше про внесення вкладень у Benchmarking_test.

---

## Цитування

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
