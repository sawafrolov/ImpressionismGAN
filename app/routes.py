from app import app
from app.image_processing import restyle_image
from flask import flash, request, redirect, render_template, url_for


def is_allowed_file_format(filename):
    file_format = filename.split(".")[-1]
    return file_format in app.config["ALLOWED_FORMATS"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            flash("No file selected.")
            return redirect(url_for("index"))
        image = request.files["image"]
        if image.filename == "":
            flash("No file selected.")
            return redirect(url_for("index"))
        if not is_allowed_file_format(image.filename):
            flash("Not allowed file format. Please upload png, jpg or bmp image.")
            return redirect(url_for("index"))
        restyle_image(image)
        return render_template("result.html", title="Restyled image")
    return render_template("index.html", title="Upload image")
