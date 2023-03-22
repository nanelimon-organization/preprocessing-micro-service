import unittest
from fastapi.testclient import TestClient
from wsgi import app


class TestPreprocessorAPI(unittest.TestCase):
    """
    A unittest class to test the Preprocessor API.

    This class provides methods to test the preprocessing functionality of the Preprocessor API.
    The API takes in a text input, preprocesses it, and returns the preprocessed text.

    """
    def setUp(self):
        """
        Set up the TestClient instance for the unittest class.
        """
        self.client = TestClient(app)

    def test_preprocessor(self):
        """
        Test the preprocessing functionality of the Preprocessor API.

        This method tests the preprocessing functionality of the Preprocessor API by passing a sample text input to the API
        and comparing the preprocessed output to the expected output.
        """
        response = self.client.post("/preprocessing", json={"text": "Merhaba dünya! 123"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("result", response.json())
        self.assertEqual(response.json()["result"], "merhaba dünya yüz yirmi üç")

    def test_empty_text(self):
        """
        Test handling of empty text input by the Preprocessor API.

        This method tests the handling of empty text input by the Preprocessor API by passing an empty text input to the API
        and checking that the API returns a 422 Unprocessable Entity status code.
        """
        response = self.client.post("/preprocessing", json={"text": ""})
        self.assertEqual(response.status_code, 422)
