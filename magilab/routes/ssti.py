from flask import Blueprint, render_template

ssti_bp = Blueprint('ssti', __name__)

@ssti_bp.route('/discovery')
def discovery():
    return render_template('labs/ssti_discovery.html')

@ssti_bp.route('/tryhard')
def tryhard():
    return render_template('labs/ssti_tryhard.html')
