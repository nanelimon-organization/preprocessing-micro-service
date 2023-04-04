import pytest
from api.controllers.preprocessing import preprocessing_router
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    return TestClient(preprocessing_router)


def test_preprocess_default_params(client):
    input_text = {"texts": ["Merhaba Dünya, 2022 yılında Python 4.0 sürümü çıktı mı?"]}
    response = client.post("/preprocess", json=input_text)
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "merhaba dunya iki bin yirmi iki yilinda python kırk surumu cikti mi"
        ]
    }


def test_preprocess_punct_params(client):
    input_text = {"texts": ["Merhaba Dünya, 2022 yılında Python 4.0 sürümü çıktı mı?"]}
    params = {
        "tr_chars": False,
        "acc_marks": False,
        "punct": True,
        "lower": False,
        "offensive": False,
        "norm_numbers": False,
        "remove_spaces": False,
    }
    response = client.post("/preprocess", json=input_text, json=params)
    assert response.status_code == 200
    assert response.json() == {
        "result": ["Merhaba Dünya 2022 yılında Python 40 sürümü çıktı mı"]
    }


def test_preprocess_remove_spaces(client):
    input_text = {
        "texts": ["Merhaba   Dünya, 2022   yılında    Python 4.0 sürümü çıktı mı?"]
    }
    params = {
        "tr_chars": False,
        "acc_marks": False,
        "punct": True,
        "lower": False,
        "offensive": False,
        "norm_numbers": False,
        "remove_spaces": True,
    }
    response = client.post("/preprocess", json=input_text, json=params)
    assert response.status_code == 200
    assert response.json() == {
        "result": ["Merhaba Dünya, 2022 yılında Python 4.0 sürümü çıktı mı?"]
    }


def test_preprocess_remove_numbers(client):
    input_text = {"texts": ["Merhaba Dünya, 2022 yılında Python 4.0 sürümü çıktı mı?"]}
    params = {"remove_numbers": True}
    response = client.post("/preprocess", json=input_text, json=params)
    assert response.status_code == 200
    assert response.json() == {
        "result": ["Merhaba Dünya, yılında Python sürümü çıktı mı?"]
    }
