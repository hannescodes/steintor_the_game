import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.secret_key = 'some_secret_key'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        files = request.files.getlist('file')
        filenames = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filenames.append(filename)
            else:
                flash('Allowed image types are: png, jpeg, jpg, gif')
                return redirect(request.url)
        if filenames:
            flash('Images successfully uploaded and displayed below')
            return render_template('upload.html', filenames=filenames)
        else:
            flash('No images selected for uploading')
            return redirect(request.url)
    return render_template('upload.html')

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('uploaded_file', filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

