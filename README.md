# Preprocessing Micro Service

|   |
| - |
| ![Ekran Resmi 2023-04-04 07 39 52](https://user-images.githubusercontent.com/83168207/229688573-35f195dd-790f-4064-b3fa-b4bb88a9162a.png) |


Preprocessing Micro Service - Mintlemon Turkish NLP kütüphanesi kullanılarak Türkçe metinlerin çeşitli veri ön işleme adımlarından geçirilmesini sağlayan bir araçtır. Bu araç, metinlerin işlenmesi için kullanılan bir dizi yöntem sunar ve sayısal metinlerin normalleştirilmesi, noktalama işaretlerinin kaldırılması, Türkçe karakterlerin normalleştirilmesi, karakterlerin küçük harfe çevrilmesi ve kısa metinlerin kaldırılması gibi çeşitli veri ön işleme adımlarını içerir. Veri ön işleme adımları, prepocessing-service kullanıcılarının tercihlerine göre özelleştirilebilir. Böylece, Türkçe metinlerin özelliklerine uygun bir şekilde işlenmesi sağlanır.

Ayrıca, FastAPI kullanılarak oluşturulan bir API tarafından desteklenmektedir. API, tek bir metin veya birden fazla metin içeren bir liste alır ve her metin için belirtilen ön işleme adımlarını uygular. API'nin `preprocess` endpoint'i, birden fazla metni aynı anda işlemek için kullanılır ve sonuçları JSON formatında döndürür.

---

### Veri Ön İşleme Fonksiyonları

Aşağıda verilen fonksiyonlar ile bu servis veri ön işleme adımlarını gerçekleştirmektedir:

<table><thead><tr><th>Fonksiyon</th><th>Açıklama</th></tr></thead><tbody><tr><td><code>mintlemon_data_preprocessing()</code></td><td>Bu fonksiyon, Mintlemon-Turkish-NLP kütüphanesinde yer alan 7 farklı fonksiyon (noktalama işaretlerinin kaldırılması, Türkçe karakterlerin normalleştirilmesi, remove stop words gibi fonksiyonları) kullanarak veri ön işleme adımlarını gerçekleştirir.</td></tr><tr><td><code>convert_offensive_contractions()</code></td><td>Bu fonksiyon veri ön işleme adımlarında daha temiz veri ve doğru sonuçlar elde etmek amacıyla, argo ve/veya küfürlü kelimelerin kısaltmalarını standart hale getirerek veriyi belirli bir formata dönüştürür. Bu işlem, <code>api/static/documents/sw_words.json</code> dosyasında yer alan <code>655</code> kısaltılmış küfürlü kelime kullanılarak gerçekleştirilir. Oluşturulan bu dosya, train/test verilerinde olası geçebilecek kısaltma halinde geçen küfürlerin önlenmesine yönelik olarak hazırlanmıştır. Bu sayede, veri ön işleme adımlarında daha doğru sonuçlar elde edilebilir ve Türkçe metinlerin analizi daha etkili bir şekilde yapılabilir.</td></tr><tr><td><code>normalize_numeric_text()</code></td><td>Metinde geçen sayısal ifadeleri Türkçe karşılıklarına dönüştürür. (ör: 120 -&gt; yüz yirmi)</td></tr><tr><td><code>remove_short_text()</code></td><td>Metinde belirlenen uzunluğun altındaki kısa metinleri kaldırır.</td></tr></tbody></table>


Ayrıca, `tr_chars`, `acc_marks`, `punct`, `lower`, `offensive`, `norm_numbers`, `remove_numbers`, `remove_spaces`, `remove_stopwords` ve `min_len` gibi parametreler kullanarak, belirli ön işleme adımlarını etkinleştirmek veya devre dışı bırakmak için özelleştirilebilir parametrik seçenekler sunduğumuzu yukarıdada ifade etmiştik... Bu sayede; özelleştirilebilir parametrelerin kullanımı, ön işleme adımlarının esnek bir şekilde yapılandırılmasını sağlar. 

### İşte Parametrelerin Açılımı: 

<table><thead><tr><th>Parametre İsmi</th><th>Varsayılan Değer</th><th>Açıklama</th></tr></thead><tbody><tr><td>texts</td><td>-</td><td>Önişleme yapılacak metinlerin listesi.</td></tr><tr><td>tr_chars</td><td>True</td><td>Türkçe karakterlerin kaldırılması durumudur. <code>False</code> değer ataması Türkçe karakterlerin kullanılabileceğini ifade etmektedir.</td></tr><tr><td>acc_marks</td><td>True</td><td>Metinden aksan işaretlerini kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>punct</td><td>True</td><td>Metinden noktalama işaretlerini kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>lower</td><td>True</td><td>Metni küçük harfe dönüştürmek için <code>True</code> olarak ayarlanır.</td></tr><tr><td>offensive</td><td>True</td><td>Küfürlü kelimeleri temizlemek için <code>True</code> olarak ayarlanır.</td></tr><tr><td>norm_numbers</td><td>True</td><td>Rakamları normalize etmek için <code>True</code> olarak ayarlanır.</td></tr><tr><td>remove_numbers</td><td>False</td><td>Rakamları kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>remove_spaces</td><td>True</td><td>Metindeki ekstra boşlukları kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>remove_stopwords</td><td>True</td><td>Metindeki stop word'leri (belirli kelimeler, örneğin "bir", "iki", "ve" vb.) kaldırmak için <code>True</code> olarak ayarlanır.</td></tr><tr><td>min_len</td><td>None</td><td>Minmum metin uzunluğu -> "" Replace edilir.. İşlem yapmak için belirli treshold girilmesi gerek, örneğin: <code>5</code> Değeri ayarlanabilir.</td></tr></tbody></table>

---

## Preprocess | Endpoint

Sonuç olarak **Preprocessing Service** API, Türkçe metinlerin veri ön işleme adımlarından geçirilmesini sağlayarak daha doğru ve tutarlı bir şekilde analiz edilmelerine olanak tanır. API, tek bir metin veya birden fazla metin içeren bir liste alarak her metin için belirtilen ön işleme adımlarını uygulayarak sonucu JSON formatında döndürür. Bu sayede, doğal dil işleme uygulamalarında kullanılmak üzere tasarlanmış bir veri ön işleme hizmeti sunulur. Ayrıca, API'nin sunduğu esnek parametreler sayesinde, veri ön işleme adımları özelleştirilebilir ve kullanıcılar, ihtiyaçlarına göre özelleştirilmiş veri ön işleme işlemleri yapabilirler.

<img width="1423" alt="Ekran Resmi 2023-04-04 08 04 12" src="https://user-images.githubusercontent.com/83168207/229692297-c4f6f88c-36f5-49e6-8c16-1caf8b234d55.png">


  İstek Gövdesi - Boş      |  Yanıt Gövdesi - Örnek
:-------------------------:|:-------------------------:
<img width="1407" alt="Ekran Resmi 2023-04-04 08 08 41" src="https://user-images.githubusercontent.com/83168207/229692532-df18615f-dc36-466c-96a1-e65ef7112d4e.png">| <img width="1581" alt="Ekran Resmi 2023-04-04 08 35 38" src="https://user-images.githubusercontent.com/83168207/229697301-92c3d03c-8f3a-4f27-9fa4-2dcca735a257.png">

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

```python
texts = ["Merhaba dünya! Bu bir örnek cümledir.", "Python öğrenmek çok keyifli."]
preprocessed_texts = preprocess_text(texts, 
                                    tr_chars=False, 
                                    acc_marks=True, 
                                    punct=True, 
                                    lower=True, 
                                    offensive=True, 
                                    norm_numbers=True, 
                                    remove_numbers=False, 
                                    remove_spaces=True, 
                                    remove_stopwords=True, 
                                    min_len=4)
print(preprocessed_texts)
```

```bash
['merhaba dünya örnek cümledir', 'python öğrenmek keyifli']
```

---

## Preprocessing Service’ in Parametrik Yapısının Model Üzerindeki Etkisinin Araştırılması

[Preprocessing Service](https://cryptic-oasis-68424.herokuapp.com/docs)'nin parametrik yapısı kullanılarak, `teknofest_train_final.csv` veri kümesi %80 eğitim ve %20 test olarak bölünmüş ve baseline bir modelin hangi veri ön işleme adımları kullanıldığında daha iyi sonuçlar verdiği belirlenmiştir. Bu doğrultuda parametre tuning çalışmaları yürütülmüştür. Model tercihi olarak dbmdz/bert-base-turkish-uncased kullanıldı. Model parametreleri arasında **max_length**: 64, **batch_size**: 32, **learning_rate**: 5e-5, **optimizer**: AdamW, **eps**: 1e-8 ve **epoch**: 8 bulunmaktadır.
Modelin uncased seçilme nedeni veri seti incelendiğinde yer yer büyük harf ile başlayan yer yer küçük harf ile başlayan kelimelerin olması ve büyük küçük harf kuralına doğru bir şekilde uyulmaması nedeniyle bu kuralın görmezden gelinmesinin sağlanmasıdır. 
Model minlemon_preprocessing parametresi ile veri ön işleme yaparken kullandığı adımlardan biri de bütün harfları lower case hale getirmektir. Bu işlem büyük küçük harf uyumuna dikkat edilen veri setlerinde (Genellikle haber veya akademik çalışmalar) yapılmayarak modelin dbmdz/bert-base-turkish-cased versiyonu kullanılmaktadır. Bu sayede uncased a göre genellikle daha iyi sonuçlar üretmektedir.


### Case [1]: Türkçe karakterlerin kullanımının ve ya kaldırılmasının model performansına etkisi 

Bu denemede, 
- Türkçe karakter içeren model ile içermeyen modelin başarısı karşılaştırıldı. 
- Türkçe Karakter Destekli Preprocessing Service ile veri ön işleme adımları belirlendi. 
- **tr_chars** parametresi False olarak ayarlandı ve Türkçe karakterlerin kullanılması sağlandı. 
- **acc_marks** parametresine True verilerek ASCII karakterler Türkçeye uygun hale getirildi. 
- **punct** parametresine True verilerek noktalama işaretleri kaldırıldı. 
- **lower** parametresine True verilerek tüm harfler küçük hale getirildi. 
- **remove_spaces** parametresine True verilerek fazla boşluklar giderildi. 
- **offensive** parametresine false değeri verilerek kısaltılmış/sansürlenmiş argo ve saldırgan kelimelerin orjinal haline dönüştürülmesi sağlandı. 
- **norm_numbers** false olarak belirlendi ve sayılar normalize edilmedi. 
- **remove_numbers** parametresi true olarak ayarlandı ve sayılar metinden kaldırıldı. 
- **remove_spaces** parametresi true ile fazla boşluklar ortadan kaldırıldı. 
- **remove_stopwords** false değeriyle durdurma kelimelerinin korunması sağlandı. 

Bu parametrelerle mintlemon-turkish-nlp kütüphanesi kullanılarak veri seti ön işleme işlemi gerçekleştirildi ve dbmdz/bert-base-turkish-uncased modeli ile modelleme yapıldı. Ayrıca, **min_len** parametresine 4 verilerek veri setindeki 4'ten küçük karakterli verilerin kaldırılması sağlandı.


<img width="777" alt="Ekran Resmi 2023-04-04 23 40 52" src="https://user-images.githubusercontent.com/83168207/229915456-fa98d251-b952-421a-ac54-bffa8e87b481.png"> |

Bu denemede, 
- Belirtilen parametrelerle veri ön işleme adımları gerçekleştirildi. 
- **tr_chars** parametresine true değeri verilerek Türkçe karakterlerin kaldırılması sağlandı. 
- **acc_marks** ile ASCII karakterler Türkçeye uygun hale getirildi. 
- **punct** parametresi true olarak belirlendi ve böylece noktalama işaretleri kaldırıldı. 
- **lower** parametresine true verilerek tüm harfler küçük hale getirildi.
- **offensive** parametresine false değeri verilerek kısaltılmış/sansürlenmiş argo ve saldırgan kelimelerin orjinal haline dönüştürülmesi sağlandı. 
- **norm_numbers** false olarak belirlendi ve sayılar normalize edilmedi. 
- **remove_numbers** parametresi true olarak ayarlandı ve sayılar metinden kaldırıldı. 
- **remove_spaces** parametresi true ile fazla boşluklar ortadan kaldırıldı. 
- **remove_stopwords** false değeriyle durdurma kelimelerinin korunması sağlandı. 
- **min_len** parametresine 4 verilerek veri setinde 4'ten küçük karakterli verilerin kaldırılması sağlandı. 
Bu parametrelerle gerçekleştirilen ön işleme adımları sonucunda veri seti hazırlandı.


<img width="777" alt="Ekran Resmi 2023-04-05 00 49 43" src="https://user-images.githubusercontent.com/78956836/229930412-0bb9ae0b-20a2-4d6f-9636-5e523d1566f1.png">

İlk iki case incelendiğinde alınan sonuçlar aşağıdaği tabloda gösterilmektedir. Bu tabloya göre aynı model kullanıldığında Türkçe karakter ile yapılan eğitim Türkçe karakterin kaldırılmış olduğu durumda yapılan eğitime göre daha başarılı sonuçlar vermektedir.

|        | tr_char:True | tr_char:False | 
| ------ | ------  | ------ | 
| F1 Score | 0.94735 | 0.9396 | 


### Case [2]: Türkçe Karakterli Metinlerde Sayıların Model Performansına Etkisi:

Bu denemede başarılı oldugunu bildiğimiz Türkçe karakterli veri seti kullanılarak, numeric değerleri kaldırdığımız da mı yoksa aynen bıraktıgımızda mı ya da Türkçe olarak yazıya dönüştürdüğümüzde mi daha iyi sonuç aldıgımızı tespit etmeye çalışacağız.

Bunun için 3 preprocessing isteği ayrı ayrı denendi.

- A. Sayıları corpustan çıkarmak.
- B. Sayıları corpusta numerik olarak bırakmak.
- C. Sayıları mintlemon-nlp-turkish kütüphanesine ait convert_text_numbers fonksiyonu ile numerik sayıları text sayılara dönüştürmek.

Bu denemelerden alınan sonuçlara göre aşağıdaki tablo çıkarılmıştır.

|        | A denemesi | B denemesi | C Denemesi|
| ------ | ------  | ------ | ------ | 
| F1 Score | 0.94735 | 0.9516 | 0.9526 |

Tabloda gösterilen sonuca bakıldığında numerik degerlerin kaldırılması performansı olumlu etkilemektedir. Fakat Sayıların kaldırılması yerine sayıların metinleştirilmesi çok daha iyi bir performans elde edilmesine neden olmaktadır. (Bu kıyas bu çalışma kapsamında ortaya çıkarmış olduğumuz [mintlemon-nlp-turkish](https://pypi.org/project/mintlemon-turkish-nlp/#description) kütüphanesinin Türkçe doğal dil işlemeye katkısıdır.)


### Case [3]: Sayıların Metine Dönüştürüldüğü Türkçe Karakterli Metinlerde, Kısaltma İçeren Küfürlerin Orjinale Dönüştürülmesinin Model Performansına Etkisi:

Bu case denemesinin amacı bazı küfür veya hakaretlerin çeşitli varyanslarını ve noktalama işaretleri ile sansürlenmiş hallerini orjinal haline çevirerek ve diğer case denemelerine göre en başarılı veri seti kullanılarak, küfürlü kelimelerde geçen noktalama işaretlerinin  orjinal haline dönüşümünün etkisini inceledik. 

Ön işleme adımlarında, 
- Türkçe karakterlerin korunması, 
- ASCII karakterlerin Türkçeye uygun hale getirilmesi, 
- noktalama işaretlerinin kaldırılması, 
- tüm harflerin küçük hale getirilmesi, 
- küfürlü kelimelerin korunması, 
- sayıların normalleştirilmesi, 
- metindeki sayıların korunması, 
- fazla boşlukların kaldırılması, 
- durdurma kelimelerinin korunması ve 4'ten küçük karakterli verilerin kaldırılması sağlandı.

Bu parametrelerle yapılan ön işleme sonucunda, küfürlü kelimelerin noktalama işaretlerinin dönüşümü üzerindeki etki analiz edildi. Model confusion matrisi aşağıda yer almaktadır. Bu Matrise göre; Küfürlü kelimeleri orijinal haliyle değiştirmenin iyi bir fikir olmadığı sonucuna varıldı.

<img width="777" alt="Ekran Resmi 2023-04-05 01 00 23" src="https://user-images.githubusercontent.com/78956836/229932374-bd223605-6b72-4761-9c5a-f14e0451cca0.png">

|        | offensive:True | offensive:False | 
| ------ | ------  | ------ | 
| F1 Score | 0.9449 | 0.9526 | 


### Case [4]: Sayıların Metine Dönüştürüldüğü Türkçe Karakterli Metinlerde, Stopwordslerin Kaldırılmasının Model Performansına Etkisi:

Türkçe doğal dil işleme çalışmalarında stopwordslerin kaldırılması model başarısına önemi herkesce billinen ve sıklıkla kullanılan bir yöntemdir. Bu nedenle preprocessing service içerisinde yer alan stopwords lerin kullanımının BERT üzerindeki etkisini elimizdeki veri setine göre değerlendirdik.


<img width="777" alt="Ekran Resmi 2023-04-05 01 06 53" src="https://user-images.githubusercontent.com/78956836/229933321-3edf652e-7e17-4057-b37e-c97b4385cb01.png">

Aşağıdaki tabloda stopwords: true ve stopwords: false durumlarının f1 skor değerlendirmesine göre sonuçları tablo halinde gösterilmektedir.
|        | stopwords:True | stopwords:False | 
| ------ | ------  | ------ | 
| F1 Score | 0.9375 | 0.9526 | 

Çalışmada elde ettiğimiz sonuçlar, durdurma kelimelerinin kaldırılmasının, cümlelerin anlam bütünlüğünü olumsuz etkilediğini ve BERT gibi encoder temelli derin öğrenme modellerinde başarıyı önemli ölçüde düşürdüğünü göstermektedir. Bu nedenle, dil modellemesi projelerinde durdurma kelimelerini muhafaza etmeyi düşünmelisiniz.

--- 


## Gereksinimler

### Ortam

Lütfen Python sürümünüzü `3.10` olarak ayarlayın:

```bash
python --version
```

- Virtualenv kurulumu:
```bash
pip install virtualenv
```
- Virtualenv oluşturma:
```bash
virtualenv venv
```
- Virtualenv'i aktif hale getirme:
```bash
source venv/bin/activate
```
- Kütüphanelerin kurulumu:
```bash
pip install -r requirements.txt
```

## Uygulamayı Çalıştırma

```python
python main.py
```

--- 

