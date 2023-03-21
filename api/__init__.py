from fastapi import APIRouter
from .controllers.preprocessing import preprocessing_router

router = APIRouter()

router.include_router(preprocessing_router, prefix='/preprocessing', tags=['preprocessing'])