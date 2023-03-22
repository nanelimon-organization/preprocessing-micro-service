from fastapi import APIRouter
from .controllers.preprocessing import preprocessing_router

router = APIRouter()


router.include_router(
    preprocessing_router,
    prefix="/preprocessing",
    tags=["API endpoints for text preprocessing using Mintlemon Turkish NLP library."]
)
