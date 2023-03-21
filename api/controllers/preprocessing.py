from fastapi import APIRouter
from pydantic import BaseModel
from api.view.preprocessing import DataPreprocessor


preprocessing_router = APIRouter()


class Item(BaseModel):
    text: str


@preprocessing_router.post("/")
async def preprocessor(item: Item):

    preprocessor = DataPreprocessor(item.text)
    result = ''
    return {"result": result}


