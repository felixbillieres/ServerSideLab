from flask import Flask
from config import Config
from routes.main import main_bp
from routes.ssrf import ssrf_bp
from routes.ssti import ssti_bp
from routes.xslt import xslt_bp
from routes.ssi import ssi_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(main_bp)
app.register_blueprint(ssrf_bp, url_prefix='/ssrf')
app.register_blueprint(ssti_bp, url_prefix='/ssti')
app.register_blueprint(xslt_bp, url_prefix='/xslt')
app.register_blueprint(ssi_bp, url_prefix='/ssi')

if __name__ == '__main__':
    app.run()
