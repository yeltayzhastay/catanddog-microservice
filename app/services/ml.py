#~/catanddog-microservice/app/api/movies.py

from PIL import Image
import base64
import io
import numpy as np
import tensorflow as tf
import cv2

model = tf.keras.models.load_model("app/services/ml_models/model2.h5")

def predict_data(ID:str, img_code:str) -> dict:
    image = np.array(Image.open(io.BytesIO(base64.b64decode(img_code))))
    image = cv2.resize(image, (150, 150))/255.0
    result = model.predict(np.array([image]))[0][0]
    return {
        "ID": ID,
        "cat_prob": round(float(1-result), 1),
        "dog_prob": round(float(result), 1)
        }
