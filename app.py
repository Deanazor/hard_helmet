import os
from datetime import datetime
from flask import Flask, request, render_template, json
from werkzeug.utils import secure_filename
from detection import Predict

UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    response = {}
    pred_path = ""
    if request.method=="POST":
        file = request.files.get('image')

        if not file:
            return {
                "error": "Image is required"
            }, 400

        supported_mimetypes = ["image/jpeg", "image/png"]
        mimetype = file.content_type
        if mimetype not in supported_mimetypes:
            return {
                "error": "Unsupported image type"
            }, 415
        
        current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        filename = current_time + '-' + file.filename
        filename = secure_filename(filename)

        response["filename"] = filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        response["status"] = "OK"

        Predict(file_path)
        pred_path = "darknet/predictions.jpg"
        os.remove(file_path)
        os.rename(pred_path, "static/predictions.jpg")

        return render_template("index.html", response=json.dumps(response), pred_img="static/predictions.jpg")

    return render_template("index.html", response=json.dumps(response))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")