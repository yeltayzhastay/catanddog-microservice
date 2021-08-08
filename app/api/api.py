from fastapi import APIRouter

from app.api import classifier

router = APIRouter()
router.include_router(classifier.router)