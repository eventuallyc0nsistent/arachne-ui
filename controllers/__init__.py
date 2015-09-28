from app import app
from functools import wraps
from flask_assets import Environment, Bundle
from flask import (session, flash, redirect)


from controllers.spiders import spiders_bp
from controllers.upload_spider import uploadspider_bp

app.register_blueprint(spiders_bp)
app.register_blueprint(uploadspider_bp)
