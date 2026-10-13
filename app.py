"""
Simple Background Remover  -  Open Source Workshop Project

Teen tareeke se background remove hota hai:
  1. rembg     -> Python library, locally chalti hai (koi API key nahi chahiye)
  2. removebg  -> remove.bg API (API key chahiye)
  3. clipdrop  -> ClipDrop API (API key chahiye)
"""
import io
import os

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, send_file
from PIL import Image

load_dotenv()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # max 10 MB upload

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

REMOVEBG_API_KEY = os.getenv("REMOVEBG_API_KEY", "")
CLIPDROP_API_KEY = os.getenv("CLIPDROP_API_KEY", "")


# ---------- Background removal functions ----------

_rembg_session = None  # model ek baar load hoga


def remove_with_rembg(image_bytes: bytes) -> bytes:
    """Local Python library se background remove karo."""
    global _rembg_session
    from rembg import new_session, remove

    if _rembg_session is None:
        _rembg_session = new_session("u2netp")  # chhota model (4 MB)
    return remove(image_bytes, session=_rembg_session)


def remove_with_removebg(image_bytes: bytes) -> bytes:
    """remove.bg API se background remove karo."""
    if not REMOVEBG_API_KEY:
        raise ValueError("REMOVEBG_API_KEY .env is not set in the File.")

    response = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": image_bytes},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVEBG_API_KEY},
        timeout=60,
    )
    if response.status_code != 200:
        raise RuntimeError(f"remove.bg error {response.status_code}: {response.text[:200]}")
    return response.content


def remove_with_clipdrop(image_bytes: bytes) -> bytes:
  
    if not CLIPDROP_API_KEY:
        raise ValueError("CLIPDROP_API_KEY .env file is not set.")

    response = requests.post(
        "https://clipdrop-api.co/remove-background/v1",
        files={"image_file": ("image.png", image_bytes, "image/png")},
        headers={"x-api-key": CLIPDROP_API_KEY},
        timeout=60,
    )
    if response.status_code != 200:
        raise RuntimeError(f"ClipDrop error {response.status_code}: {response.text[:200]}")
    return response.content


# method ka naam -> function
METHODS = {
    "rembg": remove_with_rembg,
    "removebg": remove_with_removebg,
    "clipdrop": remove_with_clipdrop,
}


# ---------- Routes ----------

def is_allowed(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template(
        "index.html",
        has_removebg=bool(REMOVEBG_API_KEY),
        has_clipdrop=bool(CLIPDROP_API_KEY),
    )


@app.route("/remove", methods=["POST"])
def remove_background():
    file = request.files.get("image")
    method = request.form.get("method", "rembg")

    if file is None or file.filename == "":
        return jsonify(error="Firstly select the Image."), 400
    if not is_allowed(file.filename):
        return jsonify(error="Only PNG, JPG or WEBP Image Allowed."), 400
    if method not in METHODS:
        return jsonify(error="Select the Wrong Method."), 400

    try:
        image_bytes = file.read()
        Image.open(io.BytesIO(image_bytes)).verify()  
        result = METHODS[method](image_bytes)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except Exception as e:
        return jsonify(error=f"Any Problem Occur: {e}"), 500

    return send_file(io.BytesIO(result), mimetype="image/png")


@app.errorhandler(413)
def too_large(_):
    return jsonify(error="File is Larger (max 10 MB)."), 413


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
