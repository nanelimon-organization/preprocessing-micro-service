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

    @validator('text')
    def text_not_empty(cls, v):
        """
        Validator to ensure that text is not empty or contain only whitespace.
        """
        if not v.strip():
            raise ValueError('Text cannot be empty or contain only whitespace')
        return v


@preprocessing_router.post("/single_preprocess", response_model=dict)
async def preprocessor(item: Item, turkish_char: bool):
    """
    Preprocess text using Mintlemon Turkish NLP library.

    This API takes in a text and applies various preprocessing steps including offensive contraction replacement,
    Turkish character normalization, numeric text normalization, lowercase conversion, and short text removal.


    Parameters
    ----------
    item : Item
        The input text to be preprocessed.
    turkish_char : bool
        If True, supported Turkish characters will be used, otherwise only ASCII characters will be used.

    Returns
    -------
    dict
        The preprocessed text.

    Raises
    ------
    HTTPException
        If there is an error during preprocessing.

    """
    try:
        preprocessor = DataPreprocessor(item.text, supported_turkish_chars=turkish_char)
        result = preprocessor.preprocess()
        return {"result": result}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f'Error processing text: {ex}')


@preprocessing_router.post("/bulk_preprocess", response_model=dict)
async def bulk_preprocess(texts: List[str], turkish_char: bool):
    """
    Preprocess multiple texts using Mintlemon Turkish NLP library.

    This API takes in a list of texts and applies various preprocessing steps including offensive contraction
    replacement, Turkish character normalization, numeric text normalization, lowercase conversion,
    and short text removal.


    Parameters
    ----------
    texts : List[str]
        The list of texts to be preprocessed.
    turkish_char : bool
        If True, supported Turkish characters will be used, otherwise only ASCII characters will be used.

    Returns
    -------
    dict
        The preprocessed texts.

    Raises
    ------
    HTTPException
        If there is an error during preprocessing.

    """
    try:
        results = []
        for text in texts:
            preprocessor = DataPreprocessor(text, supported_turkish_chars=turkish_char)
            result = preprocessor.preprocess()
            results.append(result)
        return {"result": results}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f'Error processing text: {ex}')

