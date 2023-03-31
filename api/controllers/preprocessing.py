from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, validator
from api.view.preprocessing import DataPreprocessor
from typing import List

preprocessing_router = APIRouter()


class Item(BaseModel):
    """
    Input model for preprocessor API.
    """

    text: str

    @validator("text")
    def text_not_empty(cls, v):
        """
        Validator to ensure that text is not empty or contain only whitespace.
        """
        if not v.strip():
            raise ValueError("Text cannot be empty or contain only whitespace")
        return v


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


@preprocessing_router.post("/single_preprocess", response_model=dict)
async def single_preprocess(
    item: Item,
    turkish_char: bool = True,
    offensive_contractions: bool = True,
    numeric_text_normalization: bool = True,
    remove_short_text: bool = True,
    mintelmon_preprocessing: bool = True,
    min_len: int = 5,
):
    """
    Preprocess single text using Mintlemon Turkish NLP library.

    - This API takes in a text and applies various preprocessing steps including offensive contraction replacement, Turkish character normalization, numeric text normalization, lowercase conversion, and short text removal.

    Parameters
    ----------
    * item : Item
        - The input text to be preprocessed.

    * turkish_char : bool, optional
        - If True, supported Turkish characters will be used, otherwise only ASCII characters will be used. Default is True.

    * offensive_contractions : bool, optional
        - Whether to replace offensive contractions or not. Default is True.

    * numeric_text_normalization : bool, optional
        - Whether to normalize numeric text or not. Default is True.

    * remove_short_text : bool, optional
        - Whether to remove short text or not. Default is True.

    * mintelmon_preprocessing : bool, optional
        - Whether to apply Mintlemon Turkish NLP library preprocessing steps or not. Default is True.

    * min_len : int, optional
        - The minimum length threshold for text values to be considered valid. Default is 5.

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
        preprocessor = DataPreprocessor(item.text, supported_turkish_chars=turkish_char)
        result = preprocessor.preprocess(
            offensive_contractions=offensive_contractions,
            numeric_text_normalization=numeric_text_normalization,
            remove_short_text=remove_short_text,
            mintelmon_preprocessing=mintelmon_preprocessing,
            min_len=min_len,
        )
        return {"result": result}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Error processing text: {ex}")


@preprocessing_router.post("/bulk_preprocess", response_model=dict)
async def bulk_preprocess(
    items: Items,
    turkish_char: bool = True,
    offensive_contractions: bool = True,
    numeric_text_normalization: bool = True,
    remove_short_text: bool = True,
    mintelmon_preprocessing: bool = True,
    min_len: int = 5,
):
    """
    Preprocess multiple texts using Mintlemon Turkish NLP library.

    - This API takes in a list of texts and applies various preprocessing steps including offensive contraction replacement, Turkish character normalization, numeric text normalization, lowercase conversion and short text removal.

    Parameters
    ----------
    * item : Item
        - The input text to be preprocessed.

    * turkish_char : bool, optional
        - If True, supported Turkish characters will be used, otherwise only ASCII characters will be used. Default is True.

    * offensive_contractions : bool, optional
        - Whether to replace offensive contractions or not. Default is True.

    * numeric_text_normalization : bool, optional
        - Whether to normalize numeric text or not. Default is True.

    * remove_short_text : bool, optional
        - Whether to remove short text or not. Default is True.

    * mintelmon_preprocessing : bool, optional
        - Whether to apply Mintlemon Turkish NLP library preprocessing steps or not. Default is True.

    * min_len : int, optional
        - The minimum length threshold for text values to be considered valid. Default is 5.

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
            preprocessor = DataPreprocessor(text, supported_turkish_chars=turkish_char)
            result = preprocessor.preprocess(
                offensive_contractions=offensive_contractions,
                numeric_text_normalization=numeric_text_normalization,
                remove_short_text=remove_short_text,
                mintelmon_preprocessing=mintelmon_preprocessing,
                min_len=min_len,
            )
            results.append(result)
        return {"result": results}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Error processing text: {ex}")
