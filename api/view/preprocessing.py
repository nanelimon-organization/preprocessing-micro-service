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
        Apply other functions, preprocessing steps to the request text and return the preprocessed text.

    """

    def __init__(
        self,
        text: str,
        supported_turkish_chars: bool,
        remove_accent_marks: bool,
        remove_punctuations: bool,
        lowercase: bool,
        remove_numbers: bool,
        remove_more_space: bool,
    ):
        self.text = text
        with open("api/static/documents/sw_words.json", "r") as f:
            words_sw = json.load(f)
        self.words_sw = words_sw
        self.supported_turkish_chars = supported_turkish_chars
        self.remove_accent_marks = remove_accent_marks
        self.remove_punctuations = remove_punctuations
        self.lowercase = lowercase
        self.remove_numbers = remove_numbers
        self.remove_more_space = remove_more_space

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
        text_list = [
            self.words_sw[word] if word in self.words_sw else word
            for word in self.text.lower().split()
        ]
        self.text = " ".join(text_list)

        return self.text

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
                    Normalizer.convert_text_numbers(word) if word.isdigit() else word
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
        if self.remove_accent_marks:
            self.text = Normalizer.remove_accent_marks(self.text)
        if self.remove_punctuations:
            self.text = Normalizer.remove_punctuations(self.text)
        if self.supported_turkish_chars:
            self.text = Normalizer.normalize_turkish_chars(self.text)
        if self.remove_numbers:
            self.text = Normalizer.remove_numbers(self.text)
        if self.remove_more_space:
            self.text = Normalizer.remove_more_space(self.text)
        # preprocessed_text = Normalizer.deasciify(preprocessed_text)
        if self.lowercase:
            self.text = Normalizer.lower_case(self.text)

        return self.text

    # def remove_short_text(self, min_len = None) -> None:
    #     """
    #     Remove short text values from the input text based on a minimum length threshold.

    #     Parameters
    #     ----------
    #     min_len : int, optional (default=None)
    #         The minimum length threshold for text values to be considered valid.

    #     Returns
    #     -------
    #     None

    #     Notes
    #     -----
    #     This method removes the short text values from the input text where the length of the text value is less than the
    #     specified minimum length threshold.

    #     """
    #     try:
    #         if not (min_len == None) or (min_len == 0):
    #             if len(str(self.text)) < int(min_len):
    #                 self.text = ""
    #     except Exception as e:
    #         print(e)

    def preprocess(
        self,
        offensive_contractions: bool = True,
        numeric_text_normalization: bool = True,
    ) -> str:
        """
        Apply preprocessing steps to the request text and return the preprocessed text.

        Parameters
        ----------
        offensive_contractions : bool, optional
            Whether to replace offensive contractions or not. Default is True.
        numeric_text_normalization : bool, optional
            Whether to normalize numeric text or not. Default is True.

        Returns
        -------
        str
            The preprocessed text.

        Notes
        -----
        This method applies preprocessing steps to the input text based on the specified parameters.
        """
        if offensive_contractions:
            self.convert_offensive_contractions()
        self.mintlemon_data_preprocessing()
        if numeric_text_normalization:
            self.normalize_numeric_text()
        return self.text
