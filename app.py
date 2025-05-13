from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Assicurati che index.html sia nella cartella templates/

@app.route("/get-images")
def get_images():
    image_folder = os.path.join("static", "images")
    images = [f for f in os.listdir(image_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    return jsonify(images)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
