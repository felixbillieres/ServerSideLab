from flask import Blueprint, render_template, request
from config import Config
from lxml import etree

xslt_bp = Blueprint('xslt', __name__)

@xslt_bp.route('/discovery', methods=['GET', 'POST'])
def xslt_discovery():
    flag = None
    error = None
    result = None
    
    if request.method == 'POST':
        try:
            xslt_input = request.form.get('xslt')
            xml = f'''<?xml version="1.0"?>
                    <root>
                        <flag>{Config.FLAG_XSLT_DISCOVERY}</flag>
                        <content>Public Challenge</content>
                    </root>'''
            
            xslt_root = etree.fromstring(xslt_input)
            transform = etree.XSLT(xslt_root)
            result = str(transform(etree.fromstring(xml)))
            
            if Config.FLAG_XSLT_DISCOVERY in result:
                flag = Config.FLAG_XSLT_DISCOVERY
                
        except etree.XMLSyntaxError as e:
            error = f"Syntax Error: {str(e)}"
        except Exception as e:
            error = f"Processing Error: {str(e)}"
    
    return render_template('labs/xslt_discovery.html', 
                         flag=flag, 
                         error=error, 
                         result=result)

@xslt_bp.route('/tryhard', methods=['GET', 'POST'])
def xslt_tryhard():
    flag = None
    error = None
    result = None
    
    if request.method == 'POST':
        try:
            xslt_input = request.form.get('xslt')
            xml = f'''<?xml version="1.0"?>
                    <root>
                        <hash>7d8490c</hash>
                        <content>Advanced Challenge</content>
                    </root>'''
            
            xslt_root = etree.fromstring(xslt_input)
            transform = etree.XSLT(xslt_root)
            result = str(transform(etree.fromstring(xml)))
            
            # More complex flag verification
            if any([
                Config.FLAG_XSLT_TRYHARD in result,
                "etc/passwd" in result,
                "127.0.0.1" in result
            ]):
                flag = Config.FLAG_XSLT_TRYHARD
                
        except etree.XMLSyntaxError as e:
            error = f"Syntax Error: {str(e)}"
        except Exception as e:
            error = f"Processing Error: {str(e)}"
    
    return render_template('labs/xslt_tryhard.html', 
                         flag=flag, 
                         error=error, 
                         result=result)