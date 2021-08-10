#~/catanddog-microservice/app/api/classifier.py

from fastapi import APIRouter, HTTPException
from app.models.models import PhotoList, PhotoOutList
from app.services import ml
import binascii


router = APIRouter(
    prefix="/classifier",
    tags=["classifier"],
)

@router.post('/{photos}')
async def predict(data: PhotoList) -> PhotoOutList:
    results = []
    for single_data in data.dict()['photos']:
        try:
            result = ml.predict_data(single_data["ID"], single_data["img_code"])
            results.append(result)
        except TypeError:
            return HTTPException(status_code=400, detail="TypeError")
        except binascii.Error:
            return HTTPException(status_code=400, detail="You've entered an invalid image base64")
    return {"results": results}
