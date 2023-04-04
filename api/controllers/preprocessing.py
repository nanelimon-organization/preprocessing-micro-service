from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, validator
from api.view.preprocessing import DataPreprocessor
from typing import List

preprocessing_router = APIRouter()


class Items(BaseModel):
    """
    Input model for preprocessor API.
    """

    texts: List[str]

    @validator("texts")
    def text_not_empty(cls, v):
        """
        Validator to ensure that text is not empty or contain only whitespace.
        """
        if len(v) == 0:
            raise ValueError("Text cannot be empty or contain only whitespace")
        return v


@preprocessing_router.post("/preprocess", response_model=dict)
async def preprocess(
    items: Items,
    tr_chars: bool = True,
    acc_marks: bool = True,
    punct: bool = True,
    lower: bool = True,
    offensive: bool = True,
    norm_numbers: bool = True,
    remove_numbers: bool = False,
    remove_spaces: bool = True,
    remove_stopwords: bool = True,
    min_len: int = None,
):
    """
    Preprocess multiple texts using Mintlemon Turkish NLP library.

    - This API takes in a list of texts and applies various preprocessing steps including offensive contraction replacement, Turkish character normalization, numeric text normalization, lowercase conversion and etc..


    Parameters
    ----------
    * items : Items
        - A Pydantic model for a list of input text values to be preprocessed.
    * tr_chars : bool, optional
        - Flag indicating whether to normalize Turkish characters, by default True.
    * acc_marks : bool, optional
        - Flag indicating whether to remove accent marks from text, by default True.
    * punct : bool, optional
        - Flag indicating whether to remove punctuation marks from text, by default True.
    * lower : bool, optional
        - Flag indicating whether to convert text to lowercase, by default True.
    * offensive : bool, optional
        - Flag indicating whether to convert offensive contractions to their original form, by default True.
    * norm_numbers : bool, optional
        - Flag indicating whether to convert numeric text to its normalized form, by default True.
    * remove_numbers : bool, optional
        - Flag indicating whether to remove numeric text from the input text values, by default False.
    * remove_spaces : bool, optional
        - Flag indicating whether to remove extra spaces from the input text values, by default True.
    * remove_stopwords : bool, optional
        - Flag indicating whether to remove stopwords from the input text values, by default True.
    * min_len : int, optional
        - The minimum length of text values to be considered as short text values, by default None.

    Returns
    -------
    * result : json
        - The preprocessed text.

    Raises
    ------
    * HTTPException
        -   If there is an error during preprocessing.
    """
    try:
        results = []
        for text in items.texts:
            preprocessor = DataPreprocessor(
                text,
                supported_turkish_chars=tr_chars,
                remove_accent_marks=acc_marks,
                remove_punctuations=punct,
                lowercase=lower,
                remove_numbers=remove_numbers,
                remove_more_space=remove_spaces,
                remove_stopwords=remove_stopwords,
            )
            result = preprocessor.preprocess(
                offensive_contractions=offensive,
                numeric_text_normalization=norm_numbers,
                min_len_short_text=min_len,
            )
            results.append(result)
        return {"result": results}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Error processing text: {ex}")
