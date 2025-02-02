from flask import Blueprint, render_template

ssi_bp = Blueprint('ssi', __name__)

@ssi_bp.route('/discovery')
def discovery():
    return render_template('labs/ssi_discovery.html')

@ssi_bp.route('/tryhard')
def tryhard():
    return render_template('labs/ssi_tryhard.html')
