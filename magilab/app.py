from flask import Flask
from config import Config
from routes.main import main_bp
from routes.ssrf import ssrf_bp
from routes.ssti import ssti_bp
from routes.xslt import xslt_bp
from routes.ssi import ssi_bp
import os

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(main_bp)
app.register_blueprint(ssrf_bp, url_prefix='/ssrf')
app.register_blueprint(ssti_bp, url_prefix='/ssti')
app.register_blueprint(xslt_bp, url_prefix='/xslt')
app.register_blueprint(ssi_bp, url_prefix='/ssi')

# Internal endpoints for flags
@app.route('/internal/flag_discovery')
def flag_discovery():
    if request.remote_addr not in ['127.0.0.1', '::1']:
        abort(403)
    return os.getenv('FLAG_DISCOVERY', 'flag{ssrf_discovery_123}')

@app.route('/internal/flag_tryhard')
def flag_tryhard():
    if request.remote_addr not in ['127.0.0.1', '::1']:
        abort(403)
    return os.getenv('FLAG_TRYHARD', 'flag{ssrf_tryhard_456}')

@app.route('/internal/flag_xslt_discovery')
def flag_xslt_discovery():
    if request.remote_addr not in ['127.0.0.1', '::1']:
        abort(403)
    return Config.FLAG_XSLT_DISCOVERY

@app.route('/internal/flag_xslt_tryhard')
def flag_xslt_tryhard():
    if request.remote_addr not in ['127.0.0.1', '::1']:
        abort(403)
    return Config.FLAG_XSLT_TRYHARD

@app.route('/internal/flag_ssti_discovery')
def flag_ssti_discovery():
    if request.remote_addr not in ['127.0.0.1', '::1']:
        abort(403)
    return os.getenv('FLAG_SSTI_DISCOVERY', 'flag{ssti_easy_123}')

@app.route('/internal/flag_ssti_tryhard')
def flag_ssti_tryhard():
    if request.remote_addr not in ['127.0.0.1', '::1']:
        abort(403)
    return os.getenv('FLAG_SSTI_TRYHARD', 'flag{ssti_hard_456}')

if __name__ == '__main__':
    app.run()
