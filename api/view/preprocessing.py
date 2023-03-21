from mintlemon import Normalizer
import json


class DataPreprocessor:
    """
    A class to preprocess text data in request.

    This class provides methods to perform various preprocessing steps on a given text data.
    The preprocessing steps include normalizing numeric text, removing punctuations,
    normalizing Turkish characters, converting characters to lowercase, removing short text.

    Attributes
    ----------
    text : str
        The request text data to preprocess.

    Methods
    -------
    preprocess() -> Response: dict:
        Apply all preprocessing steps to the request text and response the preprocessed text.

    """

    def __init__(self,   text: str):
        self.text = text
        with open("api/static/documents/sw_words.json", "r") as f:
            words_sw = json.load(f)
        self.words_sw = words_sw

    def convert_offensive_contractions(self) -> str:
        """
        Replace offensive contractions in the specified DataFrame column.

        Returns
        -------
        text : str
            The input with offensive contractions replaced in the specified text.

        Examples
        --------
        >>> text = "doğduğun günün aq"
        >>> convert_offensive_contractions(text)

        output:
        doğduğun günün amına koyayım
        """
        text_list = [self.words_sw[word] if word in self.words_sw else word for word in self.text.lower().split()]

        return ' '.join(text_list)

    def normalize_for_numeric_text(self) -> str:
        """
        description yazılcak..
        """
        if any(char.isdigit() for char in self.text):
            words = self.text.split()
            revised_text = " ".join(
                [
                    Normalizer.convert_text_numbers(word)
                    if word.isdigit()
                    else word
                    for word in words
                ]
            )

            return revised_text

