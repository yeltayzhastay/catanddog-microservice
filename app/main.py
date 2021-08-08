from fastapi import FastAPI
from app.api.api import router as api_router


def get_application() -> FastAPI:
    application = FastAPI(title="CatAndDogClassifier", debug=True, version="0.0.1")

    application.include_router(api_router)

    return application


app = get_application()