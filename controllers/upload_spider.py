import os
from app import app
from flask import Blueprint, render_template, redirect, request, url_for
from werkzeug import secure_filename
from helpers.config_reader import GLOBAL_PATH
from helpers.database import db, Scrapers

ALLOWED_EXTENSIONS = set(['py'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


uploadspider_bp = Blueprint('uploadspider_bp', __name__, template_folder='templates')

@uploadspider_bp.route('/upload-spider-form/')
def upload_spider_form():
    return render_template('upload-spider.html')

@uploadspider_bp.route('/upload-spider-post/', methods=['POST'])
def upload_spider_post():
    """
    Upload file to spiders/ directory and save the mapping
    in the spider_mapping file
    """
    spider_name = request.form['spider-name']
    spider_desc = request.form['spider-desc']
    spider_cls = request.form['spider-cls']
    spider_file = request.files['spider-file']

    if spider_file and allowed_file(spider_file.filename):

        # upload spider
        filename = secure_filename(spider_file.filename)
        spider_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # add spider to db
        new_spider = Scrapers(name=spider_name, description=spider_desc,
                              spidercls=spider_cls)
        db.session.add(new_spider)
        db.session.commit()

    return redirect(url_for('spiders_bp.list_spiders'))
