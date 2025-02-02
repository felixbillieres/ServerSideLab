# from flask import Blueprint, render_template

# ssrf_bp = Blueprint('ssrf', __name__)

# @ssrf_bp.route('/discovery')
# def discovery():
#     return render_template('labs/ssrf_discovery.html')

# @ssrf_bp.route('/tryhard')
# def tryhard():
#     return render_template('labs/ssrf_tryhard.html')

# magilab/routes/ssrf.py
from flask import Blueprint, request, render_template
import requests
from urllib.parse import urlparse
import socket

ssrf_bp = Blueprint('ssrf', __name__)

def is_blocked_tryhard(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ('http', 'https'):
            return True
            
        host = parsed.hostname
        if not host:
            return True

        # Check for textual matches
        blocked_hosts = {'localhost', '127.0.0.1', '::1', '0.0.0.0'}
        if host.lower() in blocked_hosts:
            return True

        # Check resolved IP
        ip = socket.gethostbyname(host)
        if ip in blocked_hosts:
            return True

        # Check for IPv6 localhost
        if host == '[::1]':
            return True

        return False
    except:
        return True

@ssrf_bp.route('/discovery', methods=['GET', 'POST'])
def discovery():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return render_template('labs/ssrf_discovery.html', error='URL is required')
        
        try:
            response = requests.get(url, timeout=5)
            return render_template('labs/ssrf_discovery.html', result=response.text)
        except Exception as e:
            return render_template('labs/ssrf_discovery.html', error=str(e))
    return render_template('labs/ssrf_discovery.html')

@ssrf_bp.route('/tryhard', methods=['GET', 'POST'])
def tryhard():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return render_template('labs/ssrf_tryhard.html', error='URL is required')
        
        if is_blocked_tryhard(url):
            return render_template('labs/ssrf_tryhard.html', error='Blocked URL detected')
        
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            return render_template('labs/ssrf_tryhard.html', result=response.text)
        except Exception as e:
            return render_template('labs/ssrf_tryhard.html', error=str(e))
    return render_template('labs/ssrf_tryhard.html')