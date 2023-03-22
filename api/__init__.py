from fastapi import APIRouter
from .controllers.preprocessing import preprocessing_router

router = APIRouter(
    prefix="/api",
    tags=["API"],
    description="API Endpoints for Preprocessing Micro Service",
)

router.include_router(
    preprocessing_router,
    prefix="/preprocessing",
    tags=["Preprocessing"],
    description="API endpoints for text preprocessing using Mintlemon Turkish NLP library",
)
