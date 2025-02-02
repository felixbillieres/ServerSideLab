from flask import Blueprint, render_template

ssrf_bp = Blueprint('ssrf', __name__)

@ssrf_bp.route('/discovery')
def discovery():
    return render_template('labs/ssrf_discovery.html')

@ssrf_bp.route('/tryhard')
def tryhard():
    return render_template('labs/ssrf_tryhard.html')