import pandas as pd
import re
import ipaddress
from tld import get_tld
from urllib.parse import urlparse

def havingIP(url):
    try:
        ipaddress.ip_address(urlparse(url).netloc)
        return 1 
    except:
        return 0  

shortening_services = r"bit\\.ly|goo\\.gl|shorte\\.st|go2l\\.ink|x\\.co|ow\\.ly|t\\.co|tinyurl|tr\\.im|is\\.gd|cli\\.gs|" \
                      r"yfrog\\.com|migre\\.me|ff\\.im|tiny\\.cc|url4\\.eu|twit\\.ac|su\\.pr|twurl\\.nl|snipurl\\.com|" \
                      r"short\\.to|BudURL\\.com|ping\\.fm|post\\.ly|Just\\.as|bkite\\.com|snipr\\.com|fic\\.kr|loopt\\.us|" \
                      r"doiop\\.com|short\\.ie|kl\\.am|wp\\.me|rubyurl\\.com|om\\.ly|to\\.ly|bit\\.do|t\\.co|lnkd\\.in|db\\.tt|" \
                      r"qr\\.ae|adf\\.ly|goo\\.gl|bitly\\.com|cur\\.lv|tinyurl\\.com|ow\\.ly|bit\\.ly|ity\\.im|q\\.gs|is\\.gd|" \
                      r"po\\.st|bc\\.vc|twitthis\\.com|u\\.to|j\\.mp|buzurl\\.com|cutt\\.us|u\\.bb|yourls\\.org|x\\.co|" \
                      r"prettylinkpro\\.com|scrnch\\.me|filoops\\.info|vzturl\\.com|qr\\.net|1url\\.com|tweez\\.me|v\\.gd|" \
                      r"tr\\.im|link\\.zip\\.net"

def tinyURL(url):
    match = re.search(shortening_services, url)
    return 1 if match else 0

def tldLength(url):
    try:
        tld = get_tld(url, fail_silently=True)
        if tld:
            return len(tld)
        else:
            return 0
    except:
        return 0
    
def digitCount(url):
    return sum(1 for c in url if c.isnumeric())


def dotCount(url):
    return url.count('.')

def wwwCount(url):
    return url.count('www')

def atSignCount(url):
    return url.count('@')

def hyphenCount(url):
    return url.count('-')

def perCount(url):
    return url.count('%')

def equalCount(url):
    return url.count('=')

def fdLength(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

def getDepth(url):
    s = urlparse(url).path.split('/')
    depth = 0
    for j in range(len(s)):
        if len(s[j]) != 0:
            depth = depth+1
    return depth
def redirection(url):
    pos = url.rfind('//')
    if pos > 6:
        if pos > 7:
            return 1  
        else:
            return 0 
    else:
        return 0 

def extract_features(url):
    features = {
        'Having_IP': havingIP(url),
        'Tiny_URL': tinyURL(url),
        'TLD_Length': tldLength(url),
        'Digit_Count': digitCount(url),
        'Dot_Count': dotCount(url),
        'www_Count': wwwCount(url),
        'At_Count': atSignCount(url),
        'Hyphen_Count': hyphenCount(url),
        'Per_Count': perCount(url),
        'Equal_Count': equalCount(url),
        'Redirection': redirection(url),
        'Depth': getDepth(url),
        'FD_Length': fdLength(url),
    }
    return features

feature_columns = [
    'Having_IP',
    'Tiny_URL',
    'TLD_Length',
    'Digit_Count',
    'Dot_Count',
    'At_Count',
    'Hyphen_Count',
    'Per_Count',
    'Equal_Count',
    'Redirection',
    'Depth',
    'FD_Length',
]
