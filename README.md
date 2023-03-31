# Preprocessing Service

<img width="1792" alt="Ekran Resmi 2023-03-31 23 06 11" src="https://user-images.githubusercontent.com/83168207/229219539-dcd35a99-6146-4f9e-bbd6-830ec132bb23.png">

Mintlemon Turkish NLP kütüphanesi kullanılarak Türkçe metinlerin çeşitli veri ön işleme adımlarından geçirilmesini sağlayan bir araçtır. Bu araç, metinlerin işlenmesi için kullanılan bir dizi yöntem sunar ve sayısal metinlerin normalleştirilmesi, noktalama işaretlerinin kaldırılması, Türkçe karakterlerin normalleştirilmesi, karakterlerin küçük harfe çevrilmesi ve kısa metinlerin kaldırılması gibi çeşitli veri ön işleme adımlarını içerir.

Ayrıca, FastAPI kullanılarak oluşturulan bir API tarafından desteklenmektedir. API, tek bir metin veya birden fazla metin içeren bir liste alır ve her metin için belirtilen ön işleme adımlarını uygular. API'nin `"single_preprocess"` ve `"bulk_preprocess"` olmak üzere iki endpoint'i vardır. `"single_preprocess"` endpoint'i, tek bir metni ön işleme adımlarına tabi tutar ve sonucu JSON formatında döndürür. `"bulk_preprocess"` endpoint'i ise birden fazla metni aynı anda işlemek için kullanılır ve sonuçları yine JSON formatında döndürür.

Bunun yanı sıra API, `"offensive_contractions"`, `"numeric_text_normalization"`, `"remove_short_text"`, `"mintelmon_preprocessing"` ve `"min_len"` gibi parametreler kullanarak, belirli ön işleme adımlarını etkinleştirmek veya devre dışı bırakmak için seçenekler sunar. Bu parametrelerin kullanımı, ön işleme adımlarının esnek bir şekilde yapılandırılmasını sağlar.

### Veri Ön İşleme Fonksiyonları

Aşağıda verilen fonksiyonlar ile bu servis veri ön işleme adımlarını gerçekleştirmektedir:

- `convert_offensive_contractions():` Metinde kısaltma halinde yer alan argo/aykırı/küfür kelimelerin açılımı ile standart dönüştürür. 
- `normalize_numeric_text():` Metinde geçen sayısal ifadeleri Türkçe karşılıklarına dönüştürür. (ör: 120 -> yüz yirmi)
- `mintlemon_data_preprocessing():` Metni Mintlemon Turkish NLP Kütüphanesinde önceden belirlenmiş adımlarla işleyerek (aksan işaretlerini veya bir başka ifadeyle düzeltme işaretlerini (şapkalı a vb.) orjinal harf karşılığı ile convert etme, noktalama vb işaretleri kaldırma, Türkçe karakterleri normalleştirme, karakterleri küçük harfe çevirme) gibi çeşitli veri ön işleme fonksiyonelliğe sahiptir. 
- `remove_short_text():` Metinde belirlenen uzunluğun altındaki kısa metinleri kaldırır.
Ayrıca, bu fonksiyonların tümünü birleştiren preprocess() fonksiyonu da mevcuttur. Bu fonksiyon, belirlenen parametrelere göre gerekli ön işleme adımlarını gerçekleştirir.

---

### Single | Endpoint 

<img width="1792" alt="Ekran Resmi 2023-03-31 23 09 16" src="https://user-images.githubusercontent.com/83168207/229220509-5d0d6aed-2fcf-4742-8743-f44c0e39c354.png">


### Bulk | Endpoint 

<img width="1792" alt="Ekran Resmi 2023-03-31 23 23 40" src="https://user-images.githubusercontent.com/83168207/229222411-cd9a8ee2-12f3-45d9-8c19-4da786112d43.png">

---

## Sonuç

Sonuç olarak, Preprocessing Service, Türkçe metinlerin veri ön işleme adımlarından geçirilmesini sağlayarak doğru ve tutarlı bir şekilde analiz edilmelerine olanak tanır. API, tek bir metin veya birden fazla metin içeren bir liste alarak her metin için belirtilen ön işleme adımlarını uygulayarak sonucu JSON formatında döndürür. Ayrıca, API'nin sunduğu parametreler, kullanıcıların veri ön işleme adımlarını esnek bir şekilde yapılandırmasına olanak tanır.


## Prerequisites

### Environment

Please set up your Python version to `3.10`

```bash
python --version
```
- Install Virtualenviroment
```bash
pip install virtualenv
```
- Create the virtualenv
```bash
virtualenv venv
```
- Activate the venv
```bash
source venv/bin/activate
```
- Install libraries
```bash
pip install -r requirements.txt
```

## Run App

```python
python main.py
```

