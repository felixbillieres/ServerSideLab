from flask import Blueprint, request, render_template, render_template_string  # Added render_template
from urllib.parse import urlparse
import requests

ssti_bp = Blueprint('ssti', __name__)

def is_blocked_tryhard(input_str):
    blocked = ['import', 'os', 'subprocess', 'eval', 'request', 'popen', 'system', 'flag']
    return any(word in input_str.lower() for word in blocked)

@ssti_bp.route('/discovery', methods=['GET', 'POST'])
def discovery():
    result = error = None
    if request.method == 'POST':
        name = request.form.get('name', '')
        template = f"<div class='greeting'>Hello {name}</div>"
        try:
            result = render_template_string(template)
        except Exception as e:
            error = str(e)
    return render_template('labs/ssti_discovery.html', result=result, error=error)

@ssti_bp.route('/tryhard', methods=['GET', 'POST'])
def tryhard():
    result = error = None
    if request.method == 'POST':
        name = request.form.get('name', '')
        
        if is_blocked_tryhard(name):
            error = "Blocked input detected"
        else:
            try:
                filtered = name.replace('(', '').replace(')', '')
                template = f"<div class='greeting'>Hello {filtered}</div>"
                result = render_template_string(template)
            except Exception as e:
                error = str(e)
    
    return render_template('labs/ssti_tryhard.html', result=result, error=error)