# Preprocessing Micro Service

|   |
| - |
| ![Ekran Resmi 2023-04-04 07 39 52](https://user-images.githubusercontent.com/83168207/229688573-35f195dd-790f-4064-b3fa-b4bb88a9162a.png) |


Preprocessing Micro Service - Mintlemon Turkish NLP kütüphanesi kullanılarak Türkçe metinlerin çeşitli veri ön işleme adımlarından geçirilmesini sağlayan bir araçtır. Bu araç, metinlerin işlenmesi için kullanılan bir dizi yöntem sunar ve sayısal metinlerin normalleştirilmesi, noktalama işaretlerinin kaldırılması, Türkçe karakterlerin normalleştirilmesi, karakterlerin küçük harfe çevrilmesi ve kısa metinlerin kaldırılması gibi çeşitli veri ön işleme adımlarını içerir. Veri ön işleme adımları, prepocessing-service kullanıcılarının tercihlerine göre özelleştirilebilir. Böylece, Türkçe metinlerin özelliklerine uygun bir şekilde işlenmesi sağlanır.

Ayrıca, FastAPI kullanılarak oluşturulan bir API tarafından desteklenmektedir. API, tek bir metin veya birden fazla metin içeren bir liste alır ve her metin için belirtilen ön işleme adımlarını uygular. API'nin `preprocess` endpoint'i, birden fazla metni aynı anda işlemek için kullanılır ve sonuçları JSON formatında döndürür.

### Veri Ön İşleme Fonksiyonları

Aşağıda verilen fonksiyonlar ile bu servis veri ön işleme adımlarını gerçekleştirmektedir:

<table><thead><tr><th>Fonksiyon</th><th>Açıklama</th></tr></thead><tbody><tr><td><code>mintlemon_data_preprocessing()</code></td><td>Bu fonksiyon, Mintlemon-Turkish-NLP kütüphanesinde yer alan 7 farklı fonksiyon (noktalama işaretlerinin kaldırılması, Türkçe karakterlerin normalleştirilmesi, remove stop words gibi fonksiyonları) kullanarak veri ön işleme adımlarını gerçekleştirir.</td></tr><tr><td><code>convert_offensive_contractions()</code></td><td>Bu fonksiyon veri ön işleme adımlarında daha temiz veri ve doğru sonuçlar elde etmek amacıyla, argo ve/veya küfürlü kelimelerin kısaltmalarını standart hale getirerek veriyi belirli bir formata dönüştürür. Bu işlem, <code>api/static/documents/sw_words.json</code> dosyasında yer alan <code>655</code> kısaltılmış küfürlü kelime kullanılarak gerçekleştirilir. Oluşturulan bu dosya, train/test verilerinde olası geçebilecek kısaltma halinde geçen küfürlerin önlenmesine yönelik olarak hazırlanmıştır. Bu sayede, veri ön işleme adımlarında daha doğru sonuçlar elde edilebilir ve Türkçe metinlerin analizi daha etkili bir şekilde yapılabilir.</td></tr><tr><td><code>normalize_numeric_text()</code></td><td>Metinde geçen sayısal ifadeleri Türkçe karşılıklarına dönüştürür. (ör: 120 -&gt; yüz yirmi)</td></tr><tr><td><code>remove_short_text()</code></td><td>Metinde belirlenen uzunluğun altındaki kısa metinleri kaldırır.</td></tr></tbody></table>


Ayrıca, `tr_chars`, `acc_marks`, `punct`, `lower`, `offensive`, `norm_numbers`, `remove_numbers`, `remove_spaces`, `remove_stopwords` ve `min_len` gibi parametreler kullanarak, belirli ön işleme adımlarını etkinleştirmek veya devre dışı bırakmak için özelleştirilebilir parametrik seçenekler sunduğumuzu yukarıdada ifade etmiştik... Bu sayede; özelleştirilebilir parametrelerin kullanımı, ön işleme adımlarının esnek bir şekilde yapılandırılmasını sağlar. 

### İşte Parametrelerin Açılımı: 

<table><thead><tr><th>Parametre İsmi</th><th>Varsayılan Değer</th><th>Açıklama</th></tr></thead><tbody><tr><td>texts</td><td>-</td><td>Önişleme yapılacak metinlerin listesi.</td></tr><tr><td>tr_chars</td><td>True</td><td>Türkçe karakterlerin kaldırılması durumudur. <code>False</code> değer ataması Türkçe karakterlerin kullanılabileceğini ifade etmektedir.</td></tr><tr><td>acc_marks</td><td>True</td><td>Metinden aksan işaretlerini kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>punct</td><td>True</td><td>Metinden noktalama işaretlerini kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>lower</td><td>True</td><td>Metni küçük harfe dönüştürmek için <code>True</code> olarak ayarlanır.</td></tr><tr><td>offensive</td><td>True</td><td>Küfürlü kelimeleri temizlemek için <code>True</code> olarak ayarlanır.</td></tr><tr><td>norm_numbers</td><td>True</td><td>Rakamları normalize etmek için <code>True</code> olarak ayarlanır.</td></tr><tr><td>remove_numbers</td><td>False</td><td>Rakamları kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>remove_spaces</td><td>True</td><td>Metindeki ekstra boşlukları kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>remove_stopwords</td><td>True</td><td>Metindeki stop word'leri (belirli kelimeler, örneğin "bir", "iki", "ve" vb.) kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>min_len</td><td>None</td><td>Minmum metin uzunluğu -> "" Replace edilir.. İşlem yapmak için belirli treshold girilmesi gerek, örneğin: <code>5</code> Değeri ayarlanabilir.</td></tr></tbody></table>

---

## API Kullanımı | Örnek İstek: 

```python
import requests
import json
import numpy as np

def preprocess_text(texts, tr_chars=False, acc_marks=True, punct=True, lower=True, offensive=True, norm_numbers=True, remove_numbers=False, remove_spaces=True, remove_stopwords=True, min_len=4):
    """
    Applies preprocessing steps to input texts using an external API.

    Parameters
    ----------
    texts : list
        List of input texts to be preprocessed.
    tr_chars : bool, optional
        Flag indicating whether to normalize Turkish characters, by default False.
    acc_marks : bool, optional
        Flag indicating whether to remove accent marks from text, by default True.
    punct : bool, optional
        Flag indicating whether to remove punctuation marks from text, by default True.
    lower : bool, optional
        Flag indicating whether to convert text to lowercase, by default True.
    offensive : bool, optional
        Flag indicating whether to convert offensive contractions to their original form, by default True.
    norm_numbers : bool, optional
        Flag indicating whether to convert numeric text to its normalized form, by default True.
    remove_numbers : bool, optional
        Flag indicating whether to remove numeric text from the input text values, by default False.
    remove_spaces : bool, optional
        Flag indicating whether to remove extra spaces from the input text values, by default True.
    remove_stopwords : bool, optional
        Flag indicating whether to remove stopwords from the input text values, by default True.
    min_len : int, optional
        The minimum length of text values to be considered as short text values, by default 4.

    Returns
    -------
    list
        The preprocessed texts.

    Raises
    ------
    Exception
        If there is an error during preprocessing.
    """

    base_url = "https://cryptic-oasis-68424.herokuapp.com/preprocess"
    payload = {
        "tr_chars": tr_chars,
        "acc_marks": acc_marks,
        "punct": punct,
        "lower": lower,
        "offensive": offensive,
        "norm_numbers": norm_numbers,
        "remove_numbers": remove_numbers,
        "remove_spaces": remove_spaces,
        "remove_stopwords": remove_stopwords,
        "min_len": min_len
    }
    data = {"texts": texts}
    headers = {'Content-type': 'application/json'}
    response = requests.post(base_url, params=payload, data=json.dumps(data), headers=headers)
    if response.ok:
        preprocessed_text = response.json()['result']
        return preprocessed_text
    else:
        raise Exception(f"Error: {response.status_code} - {response.reason}")
```

## API Kullanımı | Örnek Çıktı: 

```bash
['merhaba dünya örnek cümledir', 'python öğrenmek keyifli']
```
---

## Preprocess | Endpoint


<img width="1423" alt="Ekran Resmi 2023-04-04 08 04 12" src="https://user-images.githubusercontent.com/83168207/229692297-c4f6f88c-36f5-49e6-8c16-1caf8b234d55.png">

<img width="1407" alt="Ekran Resmi 2023-04-04 08 08 41" src="https://user-images.githubusercontent.com/83168207/229692532-df18615f-dc36-466c-96a1-e65ef7112d4e.png">


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

