# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Ümumi Baxış

Benchmarking_test komandaların gizli səhvlərini aşkar etməsinə və həll etməsinə imkan verir, real həyat sərhəd halları üçün testlər avtomatik yaradır. Bu, dəqiqlik boşluqlarını, tərəqqi və dayanıqlıq problemlərini işıqlandırır, modelin sürətli, ədalətli təkmilləşdirilməsini təmin edir və əl ilə etiketləmə tələb etmir.

---

## Məzmunun Siyahısı

- [Ümumi Baxış](#overview)
- [Əsas Xüsusiyyətlər](#core-features)
- [Qurulum](#installation)
- [Hissə alma](#contributing)
- [Sitat](#citation)

---

## Əsas Xüsusiyyətlər

1. **Məlumatların əvvəlcədən işlənməsi və Xüsusiyyətlərin hazırlanması**: Qeyri-əlaqəli sütunları silir, müşahidələri kronoloji şəkildə sıralayır və ev və zaman seriyası məlumatlarını təmizləyir, kodlaşdırır, ölçüləndirir və tarixi parçalayır, aşağıdakı modelləşdirmə üçün hazırlıq.
2. **Regressiya Modeli Təlim Paketi**: KNN, Gradient Boosting, Random Forest, XGBoost, Linear Regression kimi bir neçə regresiya alqoritmini real daşınmaz əmlak qiymətləndirmə məlumatları üzərində təlim və qiymətləndirmə edir, avtomatik saxlanma və performans hesabatı (R², MAPE) təqdim edir.
3. **İki mərhələli Generativ Benchmarking Pipeline**: Genetik alqoritmlərlə zəif təxmin edilən nümunələri tapır və variational autoencoders ilə uğursuzluq halları paylanmasını öyrənir, model zəifliklərini hədəf alan süni test nümunələri yaradır.
4. **Ədalətli Ssenari Yaradılması**: Əsas performans göstərməyən xüsusiyyət alt sahələrində qarşılıqlı süni nümunələr yaradır, demoqrafik və coğrafi bölmələr arasında tərəqqi azaldır.
5. **Süni Məlumat Yaradılması Sınır Halları üçün**: Modelin yüksək səhv göstərdiyi xüsusiyyət sahələrində sıx süni nümunələr yaradır, davamlı test və təkmilləşdirməni təmin edir.

---

## Qurulum

Benchmarking_test-i aşağıdakı üsullardan biri ilə quraşdırın:

**Mənbədən qurun**:

1. Benchmarking_test deposunu klonlayın:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Layihə qovluğuna keçin:
   ```sh
   cd Benchmarking_test
   ```
3. Layihə asılılıqlarını quraşdırın:
   ```sh
   pip install -r requirements.txt
   ```

---

## Hissə alma

- **[Problem Bildirin](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Tapılan səhvləri və ya xüsusiyyət tələblərini layihəyə göndərin.
- **[Pull Request Göndərin](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: Benchmarking_test-ə töhfə verməyi öyrənmək üçün.

---

## Sitat

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
