from flask import Blueprint, render_template

xslt_bp = Blueprint('xslt', __name__)

@xslt_bp.route('/discovery')
def discovery():
    return render_template('labs/xslt_discovery.html')

@xslt_bp.route('/tryhard')
def tryhard():
    return render_template('labs/xslt_tryhard.html')
