import os

from flask import redirect, render_template, request, url_for
from flask_breadcrumbs import register_breadcrumb
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from .. import app, db
from ..models import Topic, ImageUpload

from .education import bp_education
from .form import Image_Upload

@bp_education.route("/file-upload", methods=['GET', 'POST'])
@login_required
def file_upload():
    form = Image_Upload()
    if form.validate_on_submit():
        file_up = form.file_up.data
        print(type(file_up))
        print(file_up.__dir__())
        print(file_up.content_type)
        print('image' in file_up.content_type)
        file_up.save(os.path.join(app.config['FILE_UPLOAD'], secure_filename(file_up.filename)))
    return render_template('image-upload.html', form=form)

def save_image(image, topic_id):
    # Check to see if the file is an image
    if not ('image' in image.content_type and image.filename.endswith(app.config['ALLOWED_IMG_EXTENSIONS'])):
        return {
            "status" : False,
            "message" : "File is not an image, allowed extensions are .png, .jpg, .jpeg and .gif"
        }

    # Check to see if topic directory exists
    if not os.path.exists(os.path.join(app.config['FILE_UPLOAD'], str(topic_id))):
        os.makedirs(os.path.join(app.config['FILE_UPLOAD'], str(topic_id)))

    # Check to see if the filename exists
    if os.path.exists(os.path.join(app.config['FILE_UPLOAD'], str(topic_id), secure_filename(image.filename))):
        return {
            "status" : False,
            "message" : "File name already in use, please check the uploaded images below to see if it has been already uploaded."
        }

    # Save the image
    image.save(os.path.join(app.config['FILE_UPLOAD'], str(topic_id), secure_filename(image.filename)))

    # Add details to the db for the image
    image = ImageUpload(
        user_id = current_user.id,
        topic_id = topic_id,
        filename = secure_filename(image.filename)
    )
    db.session.add(image)
    db.session.commit()

    return {
        "status" : True,
        "message" : "Image uploaded successfully",
        "name" : secure_filename(image.filename),
        "path" : url_for('static',filename=f'upload/{topic_id}/{secure_filename(image.filename)}')
    }

@bp_education.route("/topic/<string:title>/image-upload", methods=['POST'])
@login_required
def image_upload_topic(title):
    topic = Topic.query.filter_by(title=title).first_or_404()
    file_up = request.files['image']
    return save_image(file_up, topic.id)
