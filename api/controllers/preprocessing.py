from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, validator
from api.view.preprocessing import DataPreprocessor


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


@preprocessing_router.post("/", response_model=dict)
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
        "POST /preprocessing/?turkish_char=true HTTP/1.1" 200 OK
        "POST /preprocessing/?turkish_char=false HTTP/1.1" 200 OK

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
        raise HTTPException(status_code=400, detail=f'Error processing text, {ex}')
