import os
from flask import Blueprint, flash, redirect, render_template, request, send_from_directory, url_for
from flask_login import current_user, login_required
from pathlib import Path
from werkzeug.utils import secure_filename
from .helper import validate_image, conv_jpeg_to_jpg
from . import db, app


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    # create folder for user if this is the first photo user uploads
    user_dir = os.path.join(app.config['UPLOAD_PATH'], str(current_user.id))
    Path(user_dir).mkdir(parents=True, exist_ok=True)
    files = os.listdir(user_dir)
    modify_time_sort = lambda f: os.stat(f"{user_dir}/{f}").st_ctime
    sorted_files = sorted(files, key=modify_time_sort)
    # display all photos owned by this user
    return render_template('profile.html', files=sorted_files)


@main.route('/upload', methods=['POST'])
@login_required
def upload():
    uploaded = False  # flag for showing success/error notification
    for uploaded_file in request.files.getlist('file'):
        fname = uploaded_file.filename
        if not fname:
            flash('Error: Invalid photo name. Please rename the file before uploading.')
            return redirect(url_for('main.profile'))
        
        ext = conv_jpeg_to_jpg(uploaded_file.mimetype.split('/')[1])
        # prevent going up directories attacks (../../config)
        # and then we generate our own filename to prevent weird filenames
        fname = f'shop_user_{str(current_user.id)}_{secure_filename(fname)}'
        # only images extension allowed
        if ext not in app.config['UPLOAD_EXTENSIONS']:
            flash('Error: Please choose a valid photo before uploading!')
            return redirect(url_for('main.profile'))

        # should be created the first time we access profile page
        # but just to make sure we have the directory
        user_dir = os.path.join(
            app.config['UPLOAD_PATH'], str(current_user.id))
        Path(user_dir).mkdir(parents=True, exist_ok=True)
        full_filepath = os.path.join(user_dir, fname)
        uploaded_file.save(full_filepath)
        img_type = validate_image(full_filepath)
        
        if not img_type:
            flash('Error: Please choose a valid photo before uploading!')
            os.remove(full_filepath)
            return redirect(url_for('main.profile'))

        if ext != img_type:
            print(f'file extension: {ext}, image type: {img_type}')
            os.remove(full_filepath)
            flash('Error: The photo doesn\'t match its extension. Try changing the file extension.')
            return redirect(url_for('main.profile'))

        uploaded = True

    flash('Success: Photo(s) uploaded!' if uploaded
          else 'Error: No photo uploaded. Please try again!')
    return redirect(url_for('main.profile'))


@main.route('/photo/<filename>')
@login_required
def photo(filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_PATH'], str(current_user.id)), filename)
