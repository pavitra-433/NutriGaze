from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load trained model
model = tf.keras.models.load_model("healthy_vs_rotten_model.h5")

class_names = [
'Apple___healthy','Apple___rotten',
'Banana___healthy','Banana___rotten',
'Bellpepper___healthy','Bellpepper___rotten',
'Carrot___healthy','Carrot___rotten',
'Cucumber___healthy','Cucumber___rotten',
'Grape___healthy','Grape___rotten',
'Guava___healthy','Guava___rotten',
'Mango___healthy','Mango___rotten',
'Orange___healthy','Orange___rotten',
'Potato___healthy','Potato___rotten',
'Strawberry___healthy','Strawberry___rotten',
'Tomato___healthy','Tomato___rotten'
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("blog-single.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        file = request.files["file"]

        if file.filename == "":
            return render_template("portfolio-details.html")

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        img = image.load_img(filepath, target_size=(224,224))
        img = image.img_to_array(img)
        img = preprocess_input(img)
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        confidence = float(np.max(prediction)) * 100
        predicted_class = class_names[np.argmax(prediction)]
        fruit, condition = predicted_class.split("___")

        return render_template("portfolio-details.html",
                               fruit=fruit,
                               condition=condition,
                               confidence=round(confidence,2),
                               image_path=filepath)

    return render_template("portfolio-details.html")

if __name__ == "__main__":
    app.run(debug=True)
