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
    preprocess() -> str:
        Apply all preprocessing steps to the request text and return the preprocessed text.

    """

    def __init__(self, text: str, supported_turkish_chars: bool = False):
        self.text = text
        with open("api/static/documents/sw_words.json", "r") as f:
            words_sw = json.load(f)
        self.words_sw = words_sw
        self.supported_turkish_chars = supported_turkish_chars

    def convert_offensive_contractions(self) -> str:
        """
        Replace offensive contractions in the specified request text.

        Returns
        -------
        text : str
            The request text with offensive contractions.
            
        Returns
        -------
        text : str
            The request text with offensive contractions replaced with their full forms.

        Examples
        --------
        >>> text = "doğduğun günün aq"
        >>> convert_offensive_contractions(text)

        output:
        doğduğun günün amına koyayım
        """
        text_list = [self.words_sw[word] if word in self.words_sw else word for word in self.text.lower().split()]
        self.text = ' '.join(text_list)
        
        return  self.text

    def normalize_numeric_text(self) -> str:
        """
        Normalize the text by converting all numbers to their word representations.

        Parameters
        ----------
        text : str
            The text to be normalized.

        Returns
        -------
        str
            The normalized text with numbers converted to their word representations.

        Notes
        -----
        This method replaces all numeric characters in the input text with their corresponding word representation.
        For example, the number 27 is converted to "yirmi yedi".
        This method uses the `Normalizer.convert_text_numbers()` function to perform the conversion.

        Examples
        --------
        >>> text_normalizer = TextNormalizer()
        >>> text = "Bugün hava 27 dereceydi."
        >>> text_normalizer.normalize_numeric_text(text)
        "Bugün hava yirmi yedi dereceydi."
        """
        if any(char.isdigit() for char in self.text):
            words = self.text.split()
            self.text = " ".join(
                [
                    Normalizer.convert_text_numbers(word)
                    if word.isdigit()
                    else word
                    for word in words
                ]
            )

            return self.text

    def mintlemon_data_preprocessing(self) -> str:
        """
        Apply all preprocessing steps to the request text and response the preprocessed text.
        Mintlemon Turkish NLP library is used to perform the preprocessing steps.
        
        Parameters
        ----------
        text : str
            The text to be normalized.
        
        Returns
        -------
        str
            The preprocessed text string.
        
        Notes
        -----
        This method applies the following preprocessing steps to the text:
        1. Remove accent marks.
        2. Remove all punctuations.
        3. Normalize Turkish characters (if enabled).
        4. Deasciify.
        5. Convert all characters to lowercase.

        Mintlemon Turkish NLP library is used to perform the preprocessing steps.
        
        Note to users:
        The `Normalizer.deasciify()` method has been removed from the preprocessing steps. If you still require the `deasciify()` method,
        you can uncomment it from the source code.
        """
        preprocessed_text = Normalizer.remove_accent_marks(self.text)
        preprocessed_text = Normalizer.remove_punctuations(preprocessed_text)
        if self.supported_turkish_chars:
            preprocessed_text = Normalizer.normalize_turkish_chars(preprocessed_text)
        # preprocessed_text = Normalizer.deasciify(preprocessed_text)
        self.text = Normalizer.lower_case(preprocessed_text)
        
        return self.text
    

    def remove_short_text(self, min_len: int = 5) -> None:
        """
        Remove short text values from the input text based on a minimum length threshold.

        Parameters
        ----------
        min_len : int, optional (default=5)
            The minimum length threshold for text values to be considered valid.

        Returns
        -------
        None

        Notes
        -----
        This method removes the short text values from the input text where the length of the text value is less than the
        specified minimum length threshold.

        """
        if len(str(self.text)) < min_len:
            self.text = None

    def preprocess(self) -> str:
        """
        Apply all preprocessing steps to the request text and response the preprocessed text.

        Returns
        -------
        str
            The preprocessed text.

        Notes
        -----
        This method applies all the preprocessing steps to the input text in the following order:
        1. Replace offensive contractions.
        2. Mintlemon data preprocessing.
        3. Normalize numeric text.
        4. Remove short text.

        Returns the preprocessed text.
        """
        self.convert_offensive_contractions()
        self.mintlemon_data_preprocessing()
        self.normalize_numeric_text()
        self.remove_short_text()

        return self.text
