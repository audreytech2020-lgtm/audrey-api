from flask import Flask, request, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Audrey Tech API is running 🚀"

@app.route("/convert", methods=["POST"])
def convert():
    if 'video' not in request.files:
        return "No file uploaded"

    file = request.files['video']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    output_pdf = process_video(filepath)

    return send_file(output_pdf, as_attachment=True)

def process_video(path):
    from PIL import Image
    output_path = os.path.join(OUTPUT_FOLDER, "test.pdf")
    img = Image.new("RGB", (500, 500), color=(0, 0, 0))
    img.save(output_path)
    return output_path

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # 🔥 مهم
    app.run(host="0.0.0.0", port=port)