from app import app

from controllers.spiders import spiders_bp
from controllers.update_spider import updatespider_bp

app.register_blueprint(spiders_bp)
app.register_blueprint(updatespider_bp)
