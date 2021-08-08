#~/catanddog_service/app/api/models.py

from pydantic import BaseModel
from typing import List


class Photo(BaseModel):
    ID: str
    img_code: str

class PhotoList(BaseModel):
    photos: List[Photo]

class PhotoOut(BaseModel):
    ID: str
    cat_prob: float
    dog_prob: float

class PhotoOutList(BaseModel):
    results: List[PhotoOut]