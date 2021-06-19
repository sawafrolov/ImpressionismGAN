from app import app
from flask import flash, request, redirect, render_template, url_for


@app.route("/", methods=["GET", "POST"])
def index():
    # if request.method == "POST":
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(url_for("index"))
    #     file = request.files['file']
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(url_for("index"))
    #
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         return redirect(url_for('uploaded_file',
    #                                 filename=filename))
    return render_template("index.html")
