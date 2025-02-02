import os
class Config:
    SECRET_KEY = 'magic_8bit_secret!'
    DEBUG = True
    #SSRF FLAGS
    FLAG_DISCOVERY = os.getenv('FLAG_DISCOVERY', 'flag{ssrf_discovery_123}')
    FLAG_TRYHARD = os.getenv('FLAG_TRYHARD', 'flag{ssrf_tryhard_456}')
    # XSLT Flags
    FLAG_XSLT_DISCOVERY = os.getenv('FLAG_XSLT_DISCOVERY', 'flag{XSLT_Element_Extraction}')
    FLAG_XSLT_TRYHARD = os.getenv('FLAG_XSLT_TRYHARD', 'flag{XSLT_Advanced_Execution}')
    #SSTI Flags
    FLAG_XSLT_DISCOVERY = os.getenv('FLAG_XSLT_DISCOVERY', 'flag{xslt_discovery_123}')
    FLAG_XSLT_TRYHARD = os.getenv('FLAG_XSLT_TRYHARD', 'flag{xslt_tryhard_456}')

@staticmethod
def flaggen(challenge):
        return getattr(Config, f'FLAG_{challenge.upper()}', 'FLAG{default}')